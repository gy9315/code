from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error,root_mean_squared_error
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
DF=pd.read_csv('../DATA/fish.csv',usecols=[1,2],skiprows=73,skipfooter=31,header=None,engine='python')
x_train,x_test,y_train,y_test=train_test_split(DF[[2]],DF[1])
# ==================================================================
# make_pipline -> 다항변환 및 fit 할 필요가 없음
model=make_pipeline(PolynomialFeatures(degree=2),LinearRegression())
# ==================================================================
model.fit(x_train,y_train)
score1=model.score(x_train,y_train)
score2=model.score(x_test,y_test)
pre_=model.predict(x_test)
test_score=model.score(x_test,y_test)
rmse1=root_mean_squared_error(y_train,model.predict(x_train))
rmse2=root_mean_squared_error(y_test,pre_)
print(f'학습데이터 훈련\nR^2:{score1}, RMSE: {rmse1} ')
print(f'테스트\nR^2: {score2}, RMSE: {rmse2}')
plt.plot(x_train,y_train,'ro')
plt.plot(x_test,y_test,'ys')
xs=np.linspace(x_train.min(),x_train.max(),100)
print(model.predict([[35]]))
plt.plot(xs,model.predict(xs),'green')
plt.xlabel("fish's Length")
plt.ylabel("fish's Weight")
plt.show()