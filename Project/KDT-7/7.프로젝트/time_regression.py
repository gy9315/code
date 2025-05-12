import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.utils import all_estimators
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report,root_mean_squared_error,mean_absolute_error
from sklearn.exceptions import *
from sklearn.naive_bayes import GaussianNB
import warnings
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.api import VAR
import koreanize_matplotlib
from statsmodels.tsa.stattools import adfuller
import itertools

# from pmdarima import *
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
targetDF=targetDF.astype('int')
# ============================================================================
# # 데이터 정제
# def target_scale(targetDF):
#     mean=targetDF.mean()
#     std=targetDF.std()
#     return (targetDF-mean)/std
# ============================================================================
result=adfuller(targetDF.loc['대전 유성구'].diff().dropna())
print(result[0],result[1])
targetDF.loc['대전 유성구'].diff()
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sm.graphics.tsa.plot_acf(targetDF.loc['대전 유성구'], lags=20, ax=axes[0])
sm.graphics.tsa.plot_pacf(targetDF.loc['대전 유성구'], lags=20, ax=axes[1])

axes[0].set_title("Autocorrelation Function (ACF)")
axes[1].set_title("Partial Autocorrelation Function (PACF)")
# ===============================================================================
# P=3, I=2, Q=1
arima=ARIMA(targetDF.loc['대전 유성구'],order=(2,1,2))
arima_fit=arima.fit()
print(arima_fit.summary())
