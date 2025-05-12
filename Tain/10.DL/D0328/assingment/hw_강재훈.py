import numpy as np
import torch
import pandas as pd
import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim.sgd import SGD 
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import koreanize_matplotlib
# ===========================================================
# DF=pd.read_csv('../DATA/fashion-mnist_train.csv')
# print(DF.label.unique())
# print(DF.shape)
# info={2:'upcloth',9:'boots',6:'outer',0:' shirts',3:'dress',4:'jacket',5:'sandles',8:'bag',7:'shoes',1:'pants'}
# for x in DF.label.unique(): 
#     SR=DF[DF['label']==x].iloc[2,1:]
#     SR=SR.values.reshape(28,28)
#     SR=SR.astype('uint8')
#     print(x)
#     SR=cv2.resize(SR,(100,100),interpolation=cv2.INTER_CUBIC)
#     img=cv2.imshow('img',SR)
#     cv2.waitKey()
# ============================================================
def train_test_data(path):
    DF=pd.read_csv(path)
    targetSR=DF['label'].values
    featureDF=DF.iloc[:,1:].values
    x_train,x_test,y_train,y_test=train_test_split(featureDF,targetSR,stratify=targetSR)  
    x_train=torch.tensor(x_train,dtype=torch.float32)/255.0
    y_train=torch.tensor(y_train,dtype=torch.int64)
    x_test=torch.tensor(x_test,dtype=torch.float32)/255.0
    y_test=torch.tensor(y_test,dtype=torch.int64)
    train_data=TensorDataset(x_train,y_train)
    test_data=TensorDataset(x_test,y_test)
    train_load=DataLoader(train_data,batch_size=50)
    test_load=DataLoader(test_data,batch_size=50)
    return train_load, test_load


class classification(nn.Module):
    def __init__(self):
        super().__init__()
        self.input_layer=nn.Linear(784,512)
        self.dropout=nn.Dropout(0.3)
        self.bn1=nn.BatchNorm1d(512)
        self.layer1=nn.Linear(512,256)
        self.bn2=nn.BatchNorm1d(256)
        self.layer2=nn.Linear(256,10)
        
    def forward(self,data):
        out=self.input_layer(data)
        out=self.bn1(out)
        out=F.leaky_relu(out)
        out=self.dropout(out)
        out=self.layer1(out)
        out=self.bn2(out)
        out=F.silu(out)
        out=self.dropout(out)
        out=self.layer2(out)
        return F.silu(out)
    
def model_train_valuate(train_data,test_data,epoch_num):
    model=classification()
    active_loss=nn.CrossEntropyLoss()
    optimizer=optim.SGD(model.parameters(),lr=0.1)
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    for epoch in range(epoch_num):
        total_loss=0
        loss_list=[]
        correct=0
        total=0
        accuracy_list=[]
        # lost1=[]
        for x,y in train_data:
            x=x.to(device);y=y.to(device)
            model.train()
            optimizer.zero_grad()    
            output=model(x)
            loss=F.cross_entropy(output,y)
            loss.backward()
            optimizer.step()
            total_loss+=loss.item()
            # lost1.append(loss.item())
            pred=torch.argmax(output,dim=1)
            correct+=(pred==y).sum().item()
            total+=len(y)
        print(f'epoch: {epoch}, loss: {total_loss}, accuracy: {(correct/total)*100:.2f}')
        loss_list.append(total_loss);accuracy_list.append(round((correct/total)*100,2))
        # print(lost1)
        model.eval()
        correct=0
        total=0
        with torch.no_grad():
            for x, y in test_data:
                x, y=x.to(device), y.to(device)
                output=model(x)
                pred=torch.argmax(output, dim=1)
                correct+=(pred == y).sum().item()
                total+=y.size(0)

        acc = correct / total * 100
        print(f"[TEST] Accuracy: {acc:.2f}%")
    # torch.save(model.state_dict(),'./model.pkl')
    return epoch_num,loss_list,accuracy_list  
    
def model_test(data,model_path):
    model=classification()
    model.load_state_dict(torch.load(model_path,weights_only=True))
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for x, y in data:
            x, y=x.to(device), y.to(device)
            output=model(x)
            pred=torch.argmax(output, dim=1)
            correct+=(pred == y).sum().item()
            total+=y.size(0)
    acc = correct / total * 100
    print(f"[TEST] Accuracy: {acc:.2f}%")

def dataset(path):
    DF=pd.read_csv(path)
    targetSR=DF['label'].values
    featureDF=DF.iloc[:,1:].values
    featureDF=torch.tensor(featureDF,dtype=torch.float32)/255.0
    targetSR=torch.tensor(targetSR,dtype=torch.int64)
    data_set=TensorDataset(featureDF,targetSR)
    train_load=DataLoader(data_set,batch_size=50)
    return train_load


def matplotlib(*info):
    epoch_num,loss_list,accuracy_list=info
    plt.title('model-training')
    plt.plot(range(epoch_num),np.array(loss_list),'ro-',label='loss')
    plt.plot(range(epoch_num),np.array(accuracy_list),'bo-',label='accuarcy')
    plt.show()
    
data=dataset('../DATA/fashion-mnist_test.csv')
model_test(data,'./model.pkl')