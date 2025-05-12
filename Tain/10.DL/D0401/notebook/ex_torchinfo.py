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
from torchinfo import summary

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

model=Mymodel()
optimizer=optim.Adam(model.parameters(),lr=0.01)
device= 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

best_train_score=0
best_test_score=0
best_state=[]
for epoch in range(50):
    total_loss=0
    score_train=0
    total_train=0
    model.train()
    for x,y in train_loader:
        x=x.to(dtype=torch.float32,device=device);y=y.to(device=device)
        output=model(x)
        optimizer.zero_grad()
        loss=F.cross_entropy(output,y)
        loss.backward()
        optimizer.step()
        total_loss+=loss
        pred1=torch.argmax(output,dim=1)
        score_train+=(pred1==y).sum().item()
        total_train+=len(x)
    accuracy_train=(score_train/total_train)*100
    # print(score_train)
    # print(total_train)
    print(f'epoch: {epoch}')
    print(f'[Train]: total loss: {total_loss}, accarcy: {accuracy_train:.2f}')        
    model.eval() 
total_loss=0
score=0
total=0
for x,y in test_loader:
    with torch.no_grad():
        x=x.to(dtype=torch.float32,device=device);y=y.to(device=device)
        output=model(x)
        loss=F.cross_entropy(output,y)
        total_loss+=loss.item()
        pred=torch.argmax(output,dim=1)
        score+=(pred==y).sum().item()
        total+=len(x)
# print(score)
# print(total)
accuracy=(score/total)*100
print(f'[Test]: total loss: {total_loss}, accarcy: {accuracy}')  
print('='*50)
if best_train_score<accuracy_train and best_test_score<accuracy:
    best_train_score=accuracy_train;best_test_score=accuracy
    del best_state[:]
    best_state.append(model.state_dict())
else: pass
# torch.save(best_state[0],'./model.pkl')
print(best_state[0])