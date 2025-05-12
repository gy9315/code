import torch.nn as nn
import torch 
a=torch.FloatTensor([[[1,2,3],[1,2,3]],[[5,6,3],[3,2,1]]])
print(a.shape)
b=a.flatten(start_dim=0)
f=nn.Flatten()
print(f(a))