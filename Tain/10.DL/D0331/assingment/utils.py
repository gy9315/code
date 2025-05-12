import numpy as np
import torch
import pandas as pd
import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim.sgd import SGD 
import torch.optim as optim
from torchmetrics.classification import Accuracy
from torch.utils.data import DataLoader, TensorDataset,Dataset
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import koreanize_matplotlib


class MyDataset(Dataset):
    def __init__(self,path,label_position:int=0,mode='all'):
        super().__init__()
        DF=pd.read_csv(path)
        target=DF.iloc[:,label_position]
        feature=DF.iloc[:,label_position+1:]
        self.feature=torch.from_numpy(feature)
        self.feature=self.feature.to(torch.float32)
        self.target=torch.from_numpy(target)
        self.target=self.target.to(torch.int64)
        self.mode=mode
        self.split=False
    def train_test_data(self):
        if not self.split:
            self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.feature,self.target)
            self.split=True
            return (self.x_train,self.y_train),(self.x_test,self.y_test)
    def __len__(self):
        if self.mode=='all':
            return self.feature.size(0)
        if self.mode=='train':
            self.train_test_data()
            return self.x_train.size(0)
        if self.mode=='test':
            self.train_test_data()
            return self.x_test.size(0)
    def __getitem__(self, index):
        if self.mode=='all':
            return self.feature[index],self.target[index] 
        if self.mode=='train':
            self.train_test_data()
            return self.x_train[index],self.y_train[index]
        if self.mode=='test':
            self.train_test_data()
            return self.x_test[index],self.y_test[index]



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
    
    def fit(self,train_loader,test_loader,epoch_num=100,model_save=False):
        metrics=Accuracy(task='multiclass',num_classes=10)
        optimizer=optim.Adam(self.parameters(),lr=0.01)
        device= 'cuda' if torch.cuda.is_available() else 'cpu'
        self.epoch_num=epoch_num
        self.to(device)
        self.best_train_score=0
        self.train_score=[]
        self.best_test_score=0
        self.test_score=[]
        self.test_loss=[]
        self.train_loss=[]
        self.best_state=[]
        for epoch in range(epoch_num):
            total_loss=0
            pred_=torch.Tensor()
            fact_=torch.Tensor()
            self.train()
            for x,y in train_loader:
                x=x.to(dtype=torch.float32,device=device);y=y.to(device=device)
                output=self(x)
                optimizer.zero_grad()
                loss=F.cross_entropy(output,y)
                loss.backward()
                optimizer.step()
                total_loss+=loss
                pred1=torch.argmax(output,dim=1)
                pred_=torch.hstack((pred_,pred1))
                fact_=torch.hstack((fact_,y))
            accuracy_train=metrics(pred_,fact_)
            self.train_score.append(accuracy_train.item())
            self.train_loss.append(total_loss.item())
            print(f'epoch: {epoch}')
            print(f'[Train]: total loss: {total_loss}, accarcy: {accuracy_train:.2f}')        
            self.eval() 
            total_loss=0
            pred_=torch.Tensor()
            fact_=torch.Tensor()
            for x,y in test_loader:
                with torch.no_grad():
                    x=x.to(dtype=torch.float32,device=device);y=y.to(device=device)
                    output=self(x)
                    loss=F.cross_entropy(output,y)
                    total_loss+=loss
                    pred=torch.argmax(output,dim=1)
                    pred_=torch.hstack((pred_,pred))
                    fact_=torch.hstack((fact_,y))
            accuracy=metrics(pred_,fact_)
            self.test_score.append(accuracy)
            self.test_loss.append(total_loss.item())
            print(f'[Test]: total loss: {total_loss}, accarcy: {accuracy}')  
            print('='*50)
        if self.best_train_score<accuracy_train and self.best_test_score<accuracy:
            self.best_train_score=accuracy_train;self.best_test_score=accuracy
            del self.best_state[:]
            self.best_state.append(self.state_dict())
        else: pass
        if model_save: torch.save(self.best_state[0],'./model1.pkl')      
        return {'train':[self.train_score,self.train_loss],'test':[self.test_score,self.test_loss],'state_dict':self.best_state[0]}
    
    def matplotlib(self,title,epoch_num=None,traindata=None,testdata=None,figsize=(10,5)):
        if epoch_num==None:
            epoch=self.epoch_num
        else:
            epoch=epoch_num
        if traindata==None:
            train_loss=self.train_loss
            train_score=self.train_score
        else:
            train_loss=traindata[0]
            train_score=traindata[1]
        if testdata==None:
            test_loss=self.test_loss
            test_score=self.test_score
        else:
            test_loss=testdata[0]
            test_score=testdata[1]
            # ===================================
        fig,axes=plt.subplots(1,2,figsize=figsize)
        plt.suptitle(title)
        for x,y,z in zip(axes.flatten(),[(train_loss,test_loss),(train_score,test_score)],['loss','accuarcy']):
            x.set_title(z)
            x.plot(range(epoch),y[0],'ro-',label='train')
            x.plot(range(epoch),y[1],'bo-',label='test')
        plt.show()

    
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
    acc=correct / total * 100
    print(f"[TEST] Accuracy: {acc:.2f}%")



if __name__=='__main__':
    train_loader=DataLoader(MyDataset('../DATA/fashion-mnist_train.csv',mode='train'),batch_size=40)
    test_loader=DataLoader(MyDataset('../DATA/fashion-mnist_train.csv',mode='test'),batch_size=40)
    model=classification()
    a=model.fit(train_loader,test_loader,epoch_num=5,model_save=True)
    model.matplotlib('fashion-mnist')