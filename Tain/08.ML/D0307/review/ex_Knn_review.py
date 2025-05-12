import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
x=np.array([1,2,3,4]).reshape(-1,1)
y=[1,2,3,4]
#1
a=KNeighborsRegressor(n_neighbors=2)
#2
a.fit(x,y)
x,y=a.kneighbors([[2]])
print(f'distance:{x} idx: {y}')
print(a.predict([[2]]))
#3
# print(a.score(x,y))
#4
# y=x
# ==================================
# 너는 언제 죽을거니니
# print(a.predict([[5]]))
