import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.utils import all_estimators
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report,root_mean_squared_error,mean_absolute_error
from sklearn.exceptions import *
from sklearn.naive_bayes import GaussianNB
import warnings
from statsmodels.tsa.arima import *
import koreanize_matplotlib
pd.options.display.float_format = '{:.6f}'.format

targetDF=pd.read_excel('./DATA/평균매매가격_아파트.xlsx')

targetDF['자료시점']=targetDF['자료시점'].str.replace('년 ','.')
targetDF['자료시점']=targetDF['자료시점'].str.replace('월','.')
targetDF=targetDF.T
targetDF.columns=targetDF.loc['자료시점']
targetDF=targetDF.drop(index=['자료시점'])
targetDF.columns.name=None
targetDF.drop(index=['노원구','강서구','영등포구'],inplace=True)
targetDF.rename(index={'양천구':'서울 양천구'},inplace=True)
targetDF=targetDF.sort_index()
x1=pd.read_csv('./DATA/잠재적 매매인원.csv',header=0,index_col=0)
x2=pd.read_csv('./DATA/순이동인원.csv',header=0,index_col=0)
x3=pd.read_csv('./DATA/tax.csv',header=0,index_col=0)
x1.rename(columns={'지역':'구분'},inplace=True)
x2.rename(columns={'지역':'구분'},inplace=True)
featurDF=pd.concat([x1.T,x2.T,x3.T],axis=1)
featurDF.columns=featurDF.loc['구분']
featurDF.drop(index='구분', inplace=True)
# count=0
# for x in featurDF.index:
#     if x=='2012.01':
#         print(f'{count}: 2012.1')
#     count+=1
# print(featurDF['서울 양천구'][132:].shape)
# print(targetDF.T['서울 양천구'][:-2].shape)
# x_train,x_test,y_train,y_test=train_test_split(featurDF[['서울 양천구']][132:],targetDF.T['서울 양천구'][:-2])
# regressor=all_estimators(type_filter='regressor')
# dict1={}
# # ============================================================================
# for name,class_ in regressor:   
#     try:
#         model=class_()
#         model.fit(x_train,y_train)
#         score=model.score(x_test,y_test)
#         pred=model.predict(x_test)
#     except ConvergenceWarning as e:
#         model=class_()
#         model.set_params(max_iter=100000)
#         model.fit(x_train,y_train)
#         score=model.score(x_test,y_test)
#         pred=model.predict(x_test)
#     except Exception as e:
#         pass
#     except ValueError as e: pass

#     # pred_proba=model.predict_proba(x_test)
#     dict1[name]=[score,root_mean_squared_error(y_test,pred),mean_absolute_error(y_test,pred)]
# DF=pd.DataFrame(dict1,index=['R2','RMSE','MAE'])
# print(DF)
# DF=DF.T
# # DF=DF.astype('float')
# print(DF.sort_values(by='RMSE'))
fig,axes=plt.subplots(5,2,figsize=(5,10),constrained_layout=True)

count=0
for x,city in zip(axes.flatten(),['서울 양천구','서울 양천구','대전 유성구','대전 유성구','광주 남구','광주 남구','부산 남구','부산 남구','대구 달서구','대구 달서구']):
    tx=x.twinx()
    if count%2==0:
        x.scatter(targetDF.T[city][:-2],featurDF[city].iloc[132:,0],s=2,c='b')
        x.set_ylabel('potential traders')
        tx.scatter(targetDF.T[city][:-2],featurDF[city].iloc[132:,1],s=2,c='red')
        tx.set_ylabel('pure movement')
        x.set_title(city)
    else:
        x.scatter(featurDF[city].iloc[132:,0],featurDF[city].iloc[132:,1],s=2)
        x.set_xlabel('potential traders')
        x.set_ylabel('pure movement')
        x.set_title(city)
    count+=1
plt.show()
# print(featurDF['서울 양천구'].iloc[132:,0])