import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,root_mean_squared_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np

irisDF=pd.read_csv('../DATA/iris.csv',usecols=["sepal.length","sepal.width","petal.length","petal.width"]) 
x_tr,x_tt,y_tr,y_tt=train_test_split(irisDF[['petal.length']],irisDF['petal.width'],test_size=0.3,random_state=None)
model=LinearRegression()
kf=KFold()
list1=[]
score_list=[]
for train_idx,test_idx in kf.split(x_tr):
    # print(f'train_idx: {train_idx}\ntest_idx: {test_idx}')
    x_train=x_tr.iloc[train_idx]
    y_train=y_tr.iloc[train_idx]
    x_test=x_tr.iloc[test_idx]
    y_test=y_tr.iloc[test_idx]
    model.fit(x_train,y_train)
    score=model.score(x_test,y_test)
    rmse=root_mean_squared_error(y_test,model.predict(x_test))
    list1.append(rmse)
    score_list.append(score)
print(np.mean(list1))
print(np.mean(score_list))

# ===============================================================
print('품종조회')
new_data=list(map(float,input('').split(',')))
print(model.predict(pd.DataFrame(new_data,columns=x_test.columns))[0])