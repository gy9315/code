import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.utils import all_estimators
from sklearn.linear_model import LogisticRegression,RidgeCV,Ridge,ElasticNetCV,ElasticNet
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler,PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report,root_mean_squared_error,mean_absolute_error
from sklearn.exceptions import *
from sklearn.naive_bayes import GaussianNB
import warnings
from statsmodels.tsa.arima.model import ARIMA
import koreanize_matplotlib
from statsmodels.tsa.stattools import adfuller

# from pmdarima import *


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
targetDF=targetDF.astype('int')
# ============================================================================
# # 데이터 정제
def target_scale(targetDF):
    mean=targetDF.mean()
    std=targetDF.std()
    return (targetDF-mean)/std
# ============================================================================
s=MinMaxScaler()
# xlabel=s.fit_transform(featurDF[['대구 달서구']][132:].values)
xlabel=(featurDF[['서울 양천구']][132:].values)
x_train,x_test,y_train,y_test=train_test_split(xlabel,(targetDF.T['서울 양천구'][:-2].values))
print(y_train.dtype)
model=make_pipeline(PolynomialFeatures(degree=2),LogisticRegression(C=1))
model.fit(x_train,y_train)
# print(model.named_steps['ridgecv'].alpha_)
# model=make_pipeline(PolynomialFeatures(degree=2),Ridge(alpha=model.named_steps['ridgecv'].alpha_,random_state=100))
# model.fit(x_train,y_train)
score=model.score(x_train,y_train)
score1=model.score(x_test,y_test)
pred=model.predict(x_train)
pred1=model.predict(x_test)
print(f'score: {score}, RMSE: {root_mean_squared_error(y_train,pred)}, RMSE: {mean_absolute_error(y_train,pred)}')
print(f'score: {score1}, RMSE: {root_mean_squared_error(y_test,pred1)}, RMSE: {mean_absolute_error(y_test,pred1)}')
# ============ 선형회귀 제한===========================
for x in ['대전 유성구','부산 남구','광주 남구','대구 달서구']:
    pred=model.predict(featurDF[x][132:].values)
    score=model.score(featurDF[x][132:].values,targetDF.T[x][:-2].values)
    print(score)
    print(f'score: {score}, RMSE: {root_mean_squared_error(targetDF.T[x][:-2].values,pred)}, RMSE: {mean_absolute_error(targetDF.T[x][:-2].values,pred)}')