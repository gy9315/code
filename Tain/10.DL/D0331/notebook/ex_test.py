from abc import ABC,abstractmethod
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset,DataLoader,Dataset
 
class Mybase(ABC):
    def __init__(self):
        super().__init__()
        self.name='강재훈'
        self.number=1
    @abstractmethod
    def my_method(self):
        pass
    
class Base():
    def __init__(self):
        self.name='바보'
        self.number=7
    def __getitem__(self):
        return self.name, self.number

class Number(Mybase,Base):
    def __init__(self):
        Mybase.__init__(self)
    def my_method(self):
        return 0
    
        
class CustomDataset(Dataset):
    def __init__(self):
        self.x_data=[[73,80,75],[93,88,93],[89,91,90],[96,98,100],[73,66,70]]
        self.y_data=[[152],[185],[180],[196],[142]]
    def __len__(self):
        return len(self.x_data)
    def __getitem__(self, index):
        return torch.FloatTensor(self.x_data[index]),torch.FloatTensor(self.y_data[index])

# a=CustomDataset()
# print(f'a의 원소 갯수: {len(a.y_data)}')
# print(f'x_data의 1번째 idx: {(a.x_data.__getitem__(1))}')
a=torch.tensor([[1,2,3]],dtype=torch.float32)
b=torch.tensor([[1]],dtype=torch.float32)
c=TensorDataset(a,b)
# print(c.tensors[0])
print(len(c.tensors[0]))
# print(len(a))