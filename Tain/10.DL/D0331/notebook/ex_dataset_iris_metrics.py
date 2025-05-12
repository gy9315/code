from torch.utils.data import Dataset,DataLoader
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.optim as optim
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from torchmetrics.classification import Accuracy,confusion_matrix
import matplotlib.pyplot as plt

irisDF=pd.read_csv('../DATA/iris.csv')
pd.set_option('future.no_silent_downcasting', True)
# print(irisDF)
# print(irisDF.info())
# print(irisDF.describe())
print(irisDF['variety'].unique())
for x,y in zip(irisDF['variety'].unique(),[0,1,2]):
    irisDF=irisDF.replace(x,y).copy()
feature=irisDF.iloc[:,:-1].values
target=irisDF['variety'].values
class Mymodel(nn.Module):
    def __init__(self):
        super().__init__()
        self.drop=nn.Dropout(0.2)
        self.layer1=nn.Linear(4,128)
        self.bn1=nn.BatchNorm1d(128)
        self.layer2=nn.Linear(128,64)
        self.bn2=nn.BatchNorm1d(64)
        self.layer3=nn.Linear(64,8)
        self.bn3=nn.BatchNorm1d(8)
        self.layer4=nn.Linear(8,3)
    def forward(self,data):
        out=self.layer1(data)
        # out=self.bn1(out)
        out=F.relu(out)
        # out=self.drop(out)
        out=self.layer2(out)
        # out=self.bn2(out)
        out=F.relu(out)
        # out=self.drop(out)
        out=self.layer3(out)
        # out=self.bn3(out)
        out=F.relu(out)
        return self.layer4(out)
    
class CustomDataset(Dataset):
    def __init__(self,feature,target):
        super().__init__()
        self.feature=feature
        self.target=target
    def __len__(self):
        return self.feature.shape[0]
    
    def __getitem__(self, index):
        return torch.tensor(self.feature[index]),torch.tensor(self.target[index])

dataset=CustomDataset(feature,target)
loader=DataLoader(dataset,batch_size=3)
sr=StandardScaler()
feature=sr.fit_transform(feature)
x_train,x_test,y_train,y_test=train_test_split(feature,target,stratify=target)
train_dataset=CustomDataset(x_train,y_train)
test_dataset=CustomDataset(x_test,y_test)
train_loader=DataLoader(train_dataset,batch_size=4,shuffle=True)
test_loader=DataLoader(test_dataset,batch_size=4)
print(x_train.shape)
print(x_test.shape)
metrics=Accuracy(task='multiclass',num_classes=3)
model=Mymodel()
optimizer=optim.Adam(model.parameters(),lr=0.01)
device= 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

accuracy_train=[]
loss_train=[]
accuracy_test=[]
loss_test=[]
for epoch in range(30):
    pred_train=torch.Tensor()
    fact_train=torch.Tensor()
    model.train()
    loss_score=0
    for x,y in train_loader:
        x=x.to(dtype=torch.float32,device=device);y=y.to(device=device)
        output=model(x)
        optimizer.zero_grad()
        loss=F.cross_entropy(output,y)
        loss.backward()
        optimizer.step()
        pred1=torch.argmax(output,dim=1)
        pred_train=torch.hstack((pred_train,pred1))
        fact_train=torch.hstack((fact_train,y))
        loss_score+=loss.item()
    accuracy_train.append(metrics(pred_train,fact_train).item())
    loss_train.append(loss_score)
    # print(f'accuracy: {metrics(pred_train,fact_train).item()}')
    model.eval()
    loss_score=0
    pred_test=torch.Tensor()
    fact_test=torch.Tensor()
    for x,y in test_loader:
        with torch.no_grad():
            x=x.to(dtype=torch.float32,device=device);y=y.to(device=device)
            output=model(x)
            loss=F.cross_entropy(output,y)
            pred=torch.argmax(output,dim=1)
            pred_test=torch.hstack((pred_test,pred))
            fact_test=torch.hstack((fact_test,y))
            loss_score+=loss.item()
    accuracy_test.append(metrics(pred_test,fact_test).item())
    loss_test.append(loss_score)
    
# ==========================================================================================================
fig,axes=plt.subplots(1,2,figsize=(10,5))
plt.suptitle('IRIS Deep Learning Result')
for x,y,z in zip(axes.flatten(),[(loss_train,loss_test),(accuracy_train,accuracy_test)],['loss','accuarcy']):
    x.set_title(z)
    x.plot(range(30),y[0],'ro-',label='train')
    x.plot(range(30),y[1],'bo-',label='test')
plt.show()

