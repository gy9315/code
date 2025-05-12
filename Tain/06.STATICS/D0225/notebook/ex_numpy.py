import matplotlib.pyplot as plt
import random as rd
import numpy as np
import pandas as pd
a=np.array([10,13])
print(a)
print(a.dtype)
b=np.arange(10,13)
d=np.arange(0,3)
print(np.linalg.norm(b-d))
a=np.arange(1,60,5).reshape(3,4)
print(a)
print(a[:2,...])
a=np.arange(0,12)
a=np.arange(0,12)
print(a)
print(np.logical_and(a,a))
a=a.reshape(2,6)
print(a)
print(a[np.ix_([0,1],[0,1])])