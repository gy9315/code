import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader,Dataset
import scipy as sci
import numpy as np
from sklearn.preprocessing import OneHotEncoder 


def softmax(logic):
    list1=[]
    prob_=[]
    for x in logic:
        list1.append(torch.e**x)
    for x in logic:
        prob=torch.e**x/sum(list1)    
        prob_.append(prob)
    # value=np.array(prob_).max()
    # proba_value=[y for x,y in enumerate(prob_) if y==value]
    return torch.stack(prob_)

# print(softmax(5,1,2))
# a=torch.tensor([5,1,2],dtype=torch.float32)
# b=F.softmax(a,dim=0)
# print(b)

def MSE(y_pred,y):
    # 수정
    mse=((y_pred-y)**2).mean()
    return mse


class mymodel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_input=nn.Linear(3,3)
        self.layer_output=nn.Linear(3,3)

        
    def forward(self,data):
        logic=self.layer_input(data)
        out=[]
        for log in logic:
            out.append(softmax(log))
        data=torch.stack(out)
        logic=self.layer_output(data)
        out=[]
        for log in logic:
            out.append(softmax(log))
        return torch.stack(out)
        

model=mymodel()
x_data=torch.tensor([[7,3,5],[1,2,3],[5,4,3]],dtype=torch.float32,requires_grad=True)
y_data=np.array([['0'],['1'],['2']])
en=OneHotEncoder(sparse_output=False)
y_data=en.fit_transform(y_data)
y_data=torch.tensor(y_data,dtype=torch.float32,requires_grad=True)

count=0
for x in range(10000):
    logic=model(x_data)
    optimize=optim.SGD(model.parameters(),lr=0.1)
    optimize.zero_grad()
    mse=MSE(logic,y_data)
    mse.backward()
    optimize.step()
    print(f'[{count}]')
    print(f'손실함수 값: {mse}')
    for x, y in model.named_parameters():
        print(x,y)
    print('*'*40)
    count+=1



     