import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error,root_mean_squared_error,mean_squared_error 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import LocalOutlierFactor
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

DF=pd.read_csv('../DATA/housing.csv',header=None,sep=r'\s+')

DF.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
print(DF.corr())
print(DF.isna().sum())
# ====================================================================
fig,axes=plt.subplots(2,3,figsize=(10,5))
plt.suptitle('Feature & Target(MEDV)',size=15)
# # =====================================
# # 학습(일차 회귀선) cylinders 제외
for x,y in zip(axes.flatten(),['CRIM','INDUS','NOX','RM','TAX','LSTAT']):
    x_train,x_test,y_train, y_test=train_test_split(DF[[y]],DF['MEDV'])
    # ================================================================
    # 이상치 처리
    lof=LocalOutlierFactor(n_neighbors=5,contamination=0.15)
    outlier=lof.fit_predict(x_train)
    x_train=x_train[(outlier>=1) & (outlier<=1.2) ]
    y_train=y_train[(outlier>=1) & (outlier<=1.2) ]
    # print(x_train)
    #=================================================================
    model=LinearRegression()
    model.fit(x_train,y_train)
    score=model.score(x_train,y_train)
    score_test=model.score(x_test,y_test)
    ma=mean_absolute_error(y_train,model.predict(x_train))
    ma_test=mean_absolute_error(y_test,model.predict(x_test))
    rmse=root_mean_squared_error(y_train,model.predict(x_train))
    rmse_test=root_mean_squared_error(y_test,model.predict(x_test))
    print(f'[{y}] 학습데이터\nR^2: {score},rmase: {rmse}, ma: {ma}')
    print(f'테스트데이터\nR^2: {score_test},rmse: {rmse_test}, ma: {ma_test}')
    print('='*80)
#     # ========================================================
    x.set_title(f'[{y}]')
    x.plot(x_train,y_train,'o')
    xs=np.linspace(DF[y].min(),DF[y].max(),100)
    xs_DF=pd.DataFrame(xs, columns=x_train.columns)
    print(xs_DF.columns)
    # xs=xs_DF[x_train]
    x.plot(xs_DF,model.predict(xs_DF),'r-')
    x.set_xlabel(y)
    x.set_ylabel('MEDV')
plt.show()