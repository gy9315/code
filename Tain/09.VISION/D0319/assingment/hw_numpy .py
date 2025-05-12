import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import koreanize_matplotlib
import os
from collections import Counter
# numpy 병합과 분리
a=np.arange(4).reshape(2,2)
b=np.arange(10,14).reshape(2,2)
# print(a)
# print(b)
c=np.vstack((a,b))
# c=np.hstack((a,b))
c=np.concatenate((a,b),1)
a=np.arange(12).reshape(4,3)
b=np.arange(10,130,10).reshape(4,3)
c=np.stack((a,b),1)

# print(c.shape)
# print(c)
# 배열 분리
a=np.arange(12)
c=np.split(a,(3,6))
c=np.split(a,(3,6,9))
# indice부분에 그냥 숫자: 몇개 분할 # indice 부분에 list는 인덱스 몇번 기준준
b=np.arange(12).reshape(4,3)
c=np.hsplit(b,[2])
# print(c)
a=np.arange(10,20)
b=np.where(a>15)

a=np.arange(12).reshape(3,4)
b=np.where(a>6)
# print(b)
# 2,1,5
# 1,5,2
b=np.stack((b[0],b[1]),0)
b=np.hstack((b[0].reshape(-1,1),b[1].reshape(-1,1)))
# print(b)
a=np.zeros((360,366,3))
print(a.shape)
# np.
a,b,c=np.split(a,[1,2],2)
print(b.shape)