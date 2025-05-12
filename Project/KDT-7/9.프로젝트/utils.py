import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset,TensorDataset
import torchvision.transforms as transforms
from torchvision.datasets import FashionMNIST 
import matplotlib.pyplot as plt
from torch.optim.lr_scheduler import ReduceLROnPlateau 
import torch.optim as optim
from torchmetrics.classification import Accuracy  
from torchinfo import summary
from sklearn.model_selection import train_test_split
import cv2
import numpy as np
from skimage.feature import hog
from skimage import exposure
import torchvision.transforms.functional as TF
import albumentations as A
from albumentations.pytorch import ToTensorV2

EPOCH=300
BATCH_SIZE=100
LR=0.0001
DEVICE='cuda' if torch.cuda.is_available() else 'cpu'


class CNNModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1=nn.Sequential(
            nn.Conv2d(10,100,3,1),
            nn.BatchNorm2d(100),
            nn.ReLU(),
            nn.MaxPool2d(2,2)
        )
        self.layer2=nn.Sequential(
            nn.Conv2d(100,200,3,1,1),
            nn.BatchNorm2d(200),
            nn.MaxPool2d(2,2)            
        )
        self.layer3=nn.Sequential(
            nn.Conv2d(200,100,3,1,1),
            nn.BatchNorm2d(100),
            nn.MaxPool2d(2,2)            
        )
        self.fc1=nn.Linear(100*12*12,600)
        self.drop=nn.Dropout2d(0.4)
        self.fc2=nn.Linear(600,120)
        self.fc3=nn.Linear(120,21)
        
    def forward(self,data):
        data=data.view(-1,10,100,100)
        out=self.layer1(data)
        out=self.layer2(out)
        out=self.layer3(out)
        out=out.view(out.size(0),-1)
        out=self.fc1(out)
        out=F.relu(out)
        out=self.drop(out)
        out=self.fc2(out)
        out=F.relu(out)
        out=self.drop(out)
        out=self.fc3(out)
        return out

class CustomDataset(Dataset):
    def __init__(self,imgfolder,mode=None):
        super().__init__()
        self.feature=torch.stack([ x[0] for x in imgfolder])
        self.target=torch.tensor([x[1] for x in imgfolder])
        self.mode=mode
        if mode!=None:
            # self.feature=self.feature.view(self.feature.size(0),-1)
            self.target=self.target.view(-1)
            self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.feature,self.target,stratify=self.target)
    def __len__(self):
        if self.mode=='train':
            return self.x_train.size(0)           
        if self.mode=='test':
            return self.x_test.size(0)
        if self.mode==None:
            return self.feature.size(0)
    def __getitem__(self, index):
        if self.mode=='train':
            return self.x_train[index,:], self.y_train[index]         
        if self.mode=='test':
            return self.x_test[index,:], self.y_test[index]     
        if self.mode==None:
            return self.feature[index,:], self.target[index,:]
        
def test_data_convert(path):
    img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    img.resize((100,100))
    img=torch.tensor(img)/255.0
    img=img.unsqueeze(0)
    return [(img,0)]

        
def CNN_train(imgfolder,weight=None):
    global LR
    model=CNNModel()
    optimizer=optim.Adam(model.parameters(),lr=LR)
    LR=ReduceLROnPlateau(optimizer=optimizer,mode='min',patience=10)
    train_dataset=CustomDataset(imgfolder,'train')
    # train_dataset=ExpandedAugmentDataset(train_dataset)
    test_dataset=CustomDataset(imgfolder,'test')
    train_loader=DataLoader(train_dataset,batch_size=40)
    test_lodaer=DataLoader(test_dataset,batch_size=40)
    accur=Accuracy(task='multiclass',num_classes=21)
    for epoch in range(EPOCH):
        loss_list=[]
        total_loss=0
        pred_=[]
        fact_=[]
        model.train()
        model.to(DEVICE)
        accuracy=0
        best_state_dict=[]
        for x, y in train_loader:
            x,y=x.to(DEVICE),y.to(DEVICE)
            y=y.view(-1)
            optimizer.zero_grad()
            output=model(x)
            loss=F.cross_entropy(output,y,weight=weight) 
            total_loss+=loss.item()
            loss.backward()
            optimizer.step()
            pred_train=torch.argmax(output,dim=1).tolist()
            pred_.extend(pred_train)
            fact_.extend(y.tolist())
        score=accur(torch.tensor(pred_) ,torch.tensor(fact_))
        print(f'epoch: {epoch}')
        print(f'[train] score: {score}, total loss: {total_loss}')
        model.eval()
        loss_list=[]
        total_loss=0
        pred_=[]
        fact_=[]
        with torch.no_grad():
            for x,y  in test_lodaer:
                print(x.shape,y.shape)
                x,y=x.to(DEVICE),y.to(DEVICE)
                y=y.view(-1)
                output=model(x)
                loss=F.cross_entropy(output,y) 
                total_loss+=loss.item()
                pred_train=torch.argmax(output,dim=1).tolist()
                pred_.extend(pred_train)
                fact_.extend(y.tolist())
        score=accur(torch.tensor(pred_) ,torch.tensor(fact_))
        print(f'epoch: {epoch}')
        print(f'[test] score: {score}, total loss: {total_loss}')
        LR.step(total_loss)
        if accuracy<score:
            accuracy=score
            del best_state_dict[:]
            best_state_dict.append(model.state_dict())
    torch.save(best_state_dict[0],'./model.pkl')
    return pred_,fact_

def model_test(data,model_path):
    model_dict={0: 'EV6',1: 'EV9',2: 'K3',3: 'K5',4: 'K7',5: 'K8',6: 'K9',7: '니로', 8: '레이', 9: '모닝', 10: '모하비', 11: '셀토스',
    12: '스토닉',13: '스팅어', 14: '스포티지',15: '쏘렌토',16: '쏘울', 17: '카니발',18: '카렌스',19: '포르테', 20: '프라이드'}
    model=CNNModel()
    model.load_state_dict(torch.load(model_path,weights_only=True))
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for x,y in data:
            x=x.to(device)
            output=model(x)
            pred=torch.argmax(output, dim=1).item()
            # correct+=(pred == y).sum().item()
            # total+=y.size(0)
            a=F.softmax(output, dim=1)
    return model_dict[pred],a
    
def cat_canny(imgDS):
    img=torch.stack([x[0] for x in imgDS])
    img=torch.as_tensor(img*255,dtype=torch.uint8)
    img=img.squeeze(1)
    img1=img.numpy()
    canny_img=[]
    for x in img1:
        clahe=cv2.createCLAHE(clipLimit=1, tileGridSize=(16,16))
        x=clahe.apply(x)
        a=cv2.Canny(x,30,100)
        b=torch.from_numpy(a).float()
        canny_img.append(b)
    canny_img=torch.stack(canny_img).unsqueeze(1)
    newimg=torch.cat([img.unsqueeze(1),canny_img],dim=1)
    imgfolder=[]
    for x,y in zip(newimg,[x[1] for x in imgDS]):
        imgfolder.append([x,y])
    return imgfolder



def weight_eval(imgDS):
    a=[x[1] for x in imgDS]
    dict1={}
    for x in range(21):
        count=0
        for y in a:
            if x==y:
                count+=1
        dict1[x]=count
    weight=np.array(list(dict1.values()))
    weight=weight.sum()/weight
    return torch.tensor(weight).to(DEVICE,dtype=torch.float32)

def cat_canny_hog(imgDS):
    new_imgfolder = []
    for img_tensor, label in imgDS:
        img_np = img_tensor.squeeze(0).numpy()
        img_uint8 = np.clip(img_np * 255, 0, 255).astype(np.uint8)
        clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
        img_clahe = clahe.apply(img_uint8)
        canny = cv2.Canny(img_clahe, 30, 100).astype(np.float32) / 255.0
        canny_tensor = torch.from_numpy(canny).unsqueeze(0) 
        hog_features = hog(
            img_clahe,
            orientations=9,
            pixels_per_cell=(8, 8),
            cells_per_block=(2, 2),
            visualize=False,
            feature_vector=False
        )
        hog_features = hog_features.mean(axis=(2, 3))  
        hog_channels = np.moveaxis(hog_features, -1, 0)  
        hog_resized = np.array([cv2.resize(h, (100, 100)) for h in hog_channels])  
        hog_tensor = torch.from_numpy(hog_resized).float() / 255.0  
        gray_tensor = TF.to_tensor(img_clahe).float() 
        merged_tensor = torch.cat([gray_tensor,hog_tensor], dim=0)
        new_imgfolder.append([merged_tensor, label])
    return new_imgfolder

class ExpandedAugmentDataset(Dataset):
    def __init__(self, tensor_label_list, img_size=100, n_aug=2):
        self.samples = tensor_label_list
        self.img_size = img_size
        self.n_aug = n_aug
        self.total = len(self.samples) * (1 + n_aug)

        self.base_transform = A.Compose([
            A.Resize(img_size, img_size),
            ToTensorV2()
        ])

        self.aug_transform = A.Compose([
            A.Resize(img_size, img_size),
            A.HorizontalFlip(p=0.5),
            A.RandomBrightnessContrast(p=0.5),
            A.Rotate(limit=15, p=0.5),
            A.GaussianBlur(3, p=0.3),
            A.ShiftScaleRotate(p=0.5),
            ToTensorV2()
        ])

    def __len__(self):
        return self.total

    def __getitem__(self, idx):
        base_idx = idx // (1 + self.n_aug)
        aug_idx = idx % (1 + self.n_aug)
        img_tensor, label = self.samples[base_idx]
        if img_tensor.ndim == 3 and img_tensor.shape[0] == 1:
            img_np = img_tensor.squeeze(0).numpy()
        else:
            img_np = img_tensor.numpy()
        img_np = np.clip(img_np * 255, 0, 255).astype(np.uint8)

        if img_np.ndim == 2:
            img_np = img_np[:, :, None]
        if img_np.shape[0] == 0 or img_np.shape[1] == 0:
            raise ValueError(f"잘못된 이미지 shape: {img_np.shape}, idx: {idx}")

        if aug_idx == 0:
            img = self.base_transform(image=img_np)['image']
        else:
            img = self.aug_transform(image=img_np)['image']
        return img.float(), label
