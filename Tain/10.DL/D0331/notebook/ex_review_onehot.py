import torch
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import OneHotEncoder 
import pandas as pd
a=[['바보'],['보'],['남'],['바바'],['남']]
b=[[2],[2],[1],[2],[1]]
en=OneHotEncoder(sparse_output=False)
en1=en.fit_transform(b)
en=OneHotEncoder(sparse_output=False,drop='first')
en2=np.hstack((en1,a))
en3=en.fit_transform(en2)
# for x,y in zip(en1,a):
#     print(x+y)
print(en3)
DF=pd.DataFrame([[1,2,3,4,5]])
print(DF)