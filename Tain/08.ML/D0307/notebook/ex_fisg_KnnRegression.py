import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

fsDF=pd.read_csv('../DATA/fish.csv',skiprows=73,skipfooter=31,usecols=[1,2],header=None)
# 1번 weight 2번 weight
# print(fsDF)
# print(fsDF[range(1,3)])
x_train,x_test,y_train,y_test=train_test_split(fsDF[[2]],fsDF[1],random_state=100,train_size=0.8)
# ===========================================================================
list1=[]
list2=[]
for x in [x_train,x_test]:
    list1.append(x.sort_values(by=2).reset_index(drop=True))
for x in [y_train,y_test]:
    list2.append(x.sort_values().reset_index(drop=True))
x_train,x_test=list1
y_train,y_test=list2
# ===========================================================================
model=KNeighborsRegressor()
model.fit(x_train,y_train)
# ==============================
# fit 후 학습데이터 확인
# print(x_train)
print(model.n_features_in_)
print(model.n_samples_fit_)
# print(model.effective_metric_)
# print(model.predict(x_train[:3]))
# print(y_train[:3])
print(model.score(x_train,y_train))
print(mean_squared_error(y_train,model.predict(x_train)))
#==============================
print('#'*30)
print(model.predict(x_test[:3]))
print(y_test[:3])
print(model.score(x_test,y_test))
print(mean_squared_error(y_test,model.predict(x_test)))

# =======================================================
# 최근접이웃 알고리즘의 동작원리 확인
# - K개 만큼 가까이 있는 데이터를 추출
print(x_train)
x,y=model.kneighbors([[19.0]])
print(model.predict([[19.0]]))
print(y_train)
print(f'distance: {x} idex: {y}')
print(x_train.iloc[y.reshape(-1)])
print(x_train.values[y.reshape(-1)].reshape(-1))
plt.plot(fsDF[2],fsDF[1],'bs')
plt.plot(x_train.iloc[y.reshape(-1)],y_train.iloc[y.reshape(-1)],'ro')
plt.plot(x_train.iloc[y.reshape(-1)],model.predict(x_train.iloc[y.reshape(-1)]),'y^')
# =================================================================
print(model.predict(x_train.iloc[y.reshape(-1)]))
print(y_train.iloc[y.reshape(-1)].mean())
# 다섯개의 값을 평균 값 반환
plt.show()
