import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error,root_mean_squared_error,mean_squared_error 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

DF=pd.read_csv('../DATA/auto_mpg.csv')
# ======================================
# 데이터 확인
# print(DF)
# print(DF.isna().sum())
# print(DF.dtypes)
# print(DF['horsepower'])
DF['horsepower']=DF['horsepower'].str.replace('?','0')
DF['horsepower']=DF['horsepower'].astype('int')
# print(DF.dtypes)
# ======================================
# target column: mpg[1]
# feature column 확인
# print(DF.iloc[:,:-1].corr())
# cylinder,displacement,horsepower,weight
fig,axes=plt.subplots(1,3,figsize=(10,5))
plt.suptitle('Feature & Target(MPG)',size=15)
# =====================================
# 학습(일차 회귀선) cylinders 제외
for x,y,z in zip(axes.flatten(),["displacement",'horsepower',"weight"],[6,6,11]):
    x_train,x_test,y_train, y_test=train_test_split(DF[[y]],DF['mpg'],random_state=10)
    model=KNeighborsRegressor(n_neighbors=z)
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
    # ========================================================
    x.set_title(f'[{y}]')
    x.plot(DF[y],DF['mpg'],'o')
    xs=np.linspace(DF[y].min(),DF[y].max(),100)
    x.plot(xs,model.predict(xs.reshape(-1,1)),'r-')
    x.set_xlabel(y)
    x.set_ylabel('MPG')
plt.show()