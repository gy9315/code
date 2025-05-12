import torch 
from torchmetrics.classification import BinaryAccuracy, Accuracy, MulticlassAccuracy,ConfusionMatrix
y=torch.tensor([0,1,0,1,0,1])
x=torch.tensor([0.11,0.22,0.33,0.44,0.55,0.66])
x_logic=[[5,7],[3,2],[4,6],[7,3],[2,1],[10,11]]
a=torch.tensor(x_logic,dtype=torch.float32)
logit=a[:,1]-a[:,0]
proba_sigmoid=torch.nn.functional.sigmoid(logit)
proba_softmax=torch.nn.functional.softmax(torch.tensor(x_logic,dtype=torch.float32),dim=1)
proba_sigmoid[proba_sigmoid>=0.5]=1
proba_sigmoid[proba_sigmoid<0.5]=0
print(proba_sigmoid)
print(proba_softmax.argmax(dim=1))
metrics=ConfusionMatrix(task='binary')
print(metrics(proba_sigmoid,y))
# metrics=BinaryAccuracy(threshold=0.4)
# print(metrics(x,y))
# metrics1=Accuracy(task='binary',threshold=0.4)
# print(metrics1(x,y))