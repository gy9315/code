'''
개발환경 VERSION
'''
import pandas as pd
import numpy as np
import sklearn
import matplotlib
import cv2
import bs4
import re
import koreanize_matplotlib
import collections
import torch
def version_check():
    print(f'pandas: {pd.__version__}')
    print(f'numpy: {np.__version__}')
    print(f'sklearn: {sklearn.__version__}')
    print(f'matplotilb: {matplotlib.__version__}')
    print(f'cv2: {cv2.__version__}')
    print(f'bs4: {bs4.__version__}')
    print(f'torch: {torch.__version__}')


t0=torch.tensor(77,dtype=torch.uint8)
t1=torch.tensor([77],dtype=torch.int8)
t2=torch.tensor([[77]],dtype=torch.int16)
t3=torch.tensor([[[77]]],dtype=torch.int64)

def feature_check(x:torch.Tensor):
    print(f'shape: {x.shape}')
    print(f'ndim: {x.ndim}')
    print(f'device: {x.device}')         
    print(f'dtype: {x.dtype}')
    print(f'scalar: {x}')

# for x in [t0,t1,t2,t3]:
#     feature_check(x)
#     print('*'*30)
    
# t0=torch.zeros(2,2,dtype=torch.uint8)
# t1=torch.ones(2,2,dtype=torch.int8)
# t2=torch.full((2,2),4,dtype=torch.int16)
# t3=torch.eye(2,2)

torch.manual_seed(10)
a=torch.rand(2,3)
b=torch.randn(2,3)
c=torch.randint(1,10,(2,3))
d=np.random.randint(1,10,(2,3))
# for x in [a,b,c]:
#     feature_check(x)
#     print('*'*30)
    
# # tensor원소 변경
# print(c[0])
# =================================
# scalar값만 추출: instance.item()
# =================================
float64=torch.DoubleTensor([[1,2]])
float32=torch.FloatTensor([2,3])
float16=torch.HalfTensor([2,3])
uint8=torch.ByteTensor([1,2])
int8=torch.CharTensor([1,2])
int16=torch.ShortTensor([1,2])
int32=torch.IntTensor([[1,2]])
int64=torch.LongTensor([[1,2]])
c=torch.FloatTensor([[1,2]])
d=torch.FloatTensor([[5],[6]])
# ================================
# 행렬 곱
a=c.matmul(d)
print(a,a.shape)
# ================================
# shape변경
t2=torch.tensor([[1,2,3],[4,5,6]])
print(t2.view(3,2))
# ================================
# squeeze() method
x=torch.ones(10,5,3,1)
print(x)
