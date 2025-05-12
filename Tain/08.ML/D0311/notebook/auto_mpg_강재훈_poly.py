import pandas as pd
from sklearn.linear_model import LinearRegression
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
DF['horsepower']=DF['horsepower'].replace('?',np.nan)
DF.dropna(inplace=True)
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
for x,y in zip(axes.flatten(),DF["displacement",'horsepower',"weight"]):
    x_train,x_test,y_train, y_test=train_test_split(DF[[y]],DF['mpg'])
    poly=PolynomialFeatures(degree=2,include_bias=True)
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
    print(f'[{y}] 학습데이터\nR^2: {score},rmase: {rmse}, ma: {ma}')
    print(f'테스트데이터\nR^2: {score_test},rmse: {rmse_test}, ma: {ma_test}')
    print('='*80)
    # ========================================================
    x.set_title(f'[{y}]')
    x.plot(DF[y],DF['mpg'],'o')
    xs=np.linspace(DF[y].min(),DF[y].max(),100)
    # 오류해결
    xs_DF=pd.DataFrame(xs, columns=x_train.columns)
    xs_poly = poly.transform(xs_DF)
    x.plot(xs,model.predict(xs_poly),'r-')
    x.set_xlabel(y)
    x.set_ylabel('MPG')
plt.show()