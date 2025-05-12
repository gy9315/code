import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset,TensorDataset
import torchvision.transforms as transforms
from torchvision.datasets import FashionMNIST 
import matplotlib.pyplot as plt
import koreanize_matplotlib
from torch.optim.lr_scheduler import ReduceLROnPlateau 
import torch.optim as optim
from torchmetrics.classification import Accuracy  
from torchinfo import summary
from sklearn.model_selection import train_test_split

# IMG_ROOT='../DATA/'
# trainDS=FashionMNIST(root=IMG_ROOT, download=True, train=True, transform=transforms.ToTensor())
# testDS=FashionMNIST(root=IMG_ROOT, download=True, train=False, transform=transforms.ToTensor())

def type_check(data:FashionMNIST):
    print(f'type: {type(data)}')
    print(f'classes : {data.classes}')
    print(f'class_to_idx: {data.class_to_idx}')
    print(f'target: {data.targets}')
    print(f'data: {data.data.shape}')    
EPOCH=10
BATCH_SIZE=100
LR=0.001
DEVICE='cuda' if torch.cuda.is_available() else 'cpu'

class DNNModel(nn.Module):
    def __init__(self,in_in,out_out,hd_in,hd_cnt):
        super().__init__()
        self.hd_layer1=nn.ModuleList([nn.Linear(hd_in,hd_in)for x in range(hd_cnt)])
        self.input_layer=nn.Linear(in_in,hd_in)
        self.output_layer=nn.Linear(hd_in,out_out)
        self.drop=nn.Dropout1d(0.25)
        
    def forward(self,data):
        out=self.input_layer(data)
        out=F.relu(out)
        for x in self.hd_layer1:
            out=x(out)
            out=F.relu(out)
            self.drop(out)
        out=self.output_layer(out)
        return out


class CNNModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1=nn.Sequential(
            nn.Conv2d(1,32,3,1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2,2)
        )
        self.layer2=nn.Sequential(
            nn.Conv2d(32,64,3),
            nn.BatchNorm2d(64),
            nn.MaxPool2d(2,2)            
        )
        self.fc1=nn.Linear(64*11*11,600)
        self.drop=nn.Dropout2d(0.25)
        self.fc2=nn.Linear(600,120)
        self.fc3=nn.Linear(120,2)
        
    def forward(self,data):
        data=data.view(-1,1,50,50)
        out=self.layer1(data)
        out=self.layer2(out)
        out=out.view(out.size(0),-1)
        out=self.fc1(out)
        out=F.relu(out)
        self.drop(out)
        out=self.fc2(out)
        out=F.relu(out)
        self.drop(out)
        out=self.fc3(out)
        return out

class CustomDataset(Dataset):
    def __init__(self,feature,target,mode=None):
        super().__init__()
        self.feature=feature
        self.target=target
        self.mode=mode
        if mode!=None:
            self.feature=self.feature.view(self.feature.size(0),-1)
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
        

def normal_train(feature,target):
    model=DNNModel(2500,2,300,1)
    optimizer=optim.Adam(model.parameters(),lr=0.001)
    LR=ReduceLROnPlateau(optimizer=optimizer,mode='min',patience=10)
    train_dataset=CustomDataset(feature,target,'train')
    test_dataset=CustomDataset(feature,target,'test')
    train_loader=DataLoader(train_dataset,batch_size=40)
    test_lodaer=DataLoader(test_dataset,batch_size=40)
    accur=Accuracy(task='multiclass',num_classes=2)
    for epoch in range(EPOCH):
        loss_list=[]
        total_loss=0
        pred_=[]
        fact_=[]
        model.train()
        model.to(DEVICE)
        for x, y in train_loader:
            x,y=x.to(DEVICE),y.to(DEVICE)
            y=y.view(-1)
            optimizer.zero_grad()
            output=model(x)
            loss=F.cross_entropy(output,y) 
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
        
def CNN_train(feature,target):
    model=CNNModel()
    optimizer=optim.Adam(model.parameters(),lr=0.001)
    LR=ReduceLROnPlateau(optimizer=optimizer,mode='min',patience=10)
    train_dataset=CustomDataset(feature,target,'train')
    test_dataset=CustomDataset(feature,target,'test')
    train_loader=DataLoader(train_dataset,batch_size=40)
    test_lodaer=DataLoader(test_dataset,batch_size=40)
    accur=Accuracy(task='multiclass',num_classes=2)
    for epoch in range(EPOCH):
        loss_list=[]
        total_loss=0
        pred_=[]
        fact_=[]
        model.train()
        model.to(DEVICE)
        for x, y in train_loader:
            x,y=x.to(DEVICE),y.to(DEVICE)
            y=y.view(-1)
            optimizer.zero_grad()
            output=model(x)
            loss=F.cross_entropy(output,y) 
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
    
