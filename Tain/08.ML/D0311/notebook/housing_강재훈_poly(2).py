import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,root_mean_squared_error,mean_squared_error 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.model_selection import KFold
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

DF=pd.read_csv('../DATA/housing.csv',header=None,sep=r'\s+')

DF.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
# print(DF.corr())
# print(DF.isna().sum())
# =====================================
x_train,x_test,y_train, y_test=train_test_split(DF.loc[:,['CRIM','INDUS','NOX','RM','TAX','LSTAT']],DF['MEDV'])
# ================================================================
# 이상치 처리
lof=LocalOutlierFactor(n_neighbors=10,contamination=0.1)
outlier=lof.fit_predict(pd.DataFrame(y_train))
print(outlier)
x_train=x_train[(outlier>=1) & (outlier<=1.1) ]
y_train=y_train[(outlier>=1) & (outlier<=1.1) ]
# print(x_train)
#=================================================================
poly=PolynomialFeatures(degree=2,include_bias=False)
poly.fit(x_train)
poly_train=poly.transform(x_train)
poly_test=poly.transform(x_test) 
model=LinearRegression()
model.fit(poly_train,y_train)
score=model.score(poly_train,y_train)
score_test=model.score(poly_test,y_test)
ma=mean_absolute_error(y_train,model.predict(poly_train))
ma_test=mean_absolute_error(y_test,model.predict(poly_test))
rmse=root_mean_squared_error(y_train,model.predict(poly_train))
rmse_test=root_mean_squared_error(y_test,model.predict(poly_test))
print(f'학습데이터\nR^2: {score},rmse: {rmse}, ma: {ma}')
print(f'테스트데이터\nR^2: {score_test},rmse: {rmse_test}, ma: {ma_test}')
print('='*80)