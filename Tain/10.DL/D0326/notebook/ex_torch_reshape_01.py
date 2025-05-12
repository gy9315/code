import pandas as pd
import numpy as np
import torch

# ================================
# shape변경
t2=torch.tensor([[[[1,2,3],[4,5,6]],[[11,22,33],[4,5,6]]],
                [[[11,22,33],[44,55,66]],[[1,2,3],[4,5,6]]],
                [[[13,23,33],[43,53,63]],[[1,2,3],[4,5,6]]]])
a=np.arange(1,26)
a=a.reshape(5,1,5)
# print(t2.view(3,2))
# # ================================
# # squeeze() method
# x=torch.ones(10,5,3,1)
# # print(x)
# t1=torch.tensor([[1,2,3,4,5,6]])
# t4=t1.reshape(-1,1,1,1)
# print(t4)
# ================================
# 축변경
# print(t2)
# a=torch.tensor(a)
print(a)
a=np.transpose(a,[0,2,1])
print(a)
print(np.reshape(a,(1,1,5,1,5)))