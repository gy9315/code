import torch.nn as nn
import torch.nn.functional as F
import torch
from torchinfo import summary
class Mymodel(nn.Module):
    def __init__(self,in_,out_,h_in,h_cnt):
        super().__init__()
        self.input=nn.Linear(in_,h_in)
        self.h1_layer=nn.ModuleList([nn.Linear(h_in,h_in) for x in range(h_cnt)])
        self.output=nn.Linear(h_in,out_)
    def forward(self,data):
        y=F.relu(self.input(data))
        for x in self.h1_layer:
            y=F.relu(x(y))
        return self.output(y)        

model=Mymodel(3,1,5,2)
# prinmodel(torch.FloatTensor([1,2,3])))
summary(model,input_size=(100,3))


