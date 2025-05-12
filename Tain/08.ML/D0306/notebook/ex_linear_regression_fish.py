from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np
import pandas as pd
# 데이터셋: fish.csv
#   * 피쳐: 길이 컬럼
#   * 타겟: 무게 컬럼
# - 학습종류: 지도학습
fsDF=pd.read_csv('../DATA/fish.csv',skiprows=73,skipfooter=31,usecols=[1,2],header=None)
print(fsDF)
plt.plot(fsDF[1],fsDF[2],'s')
# plt.show()
lr=LinearRegression()
length=fsDF[1].values.reshape(-1,1)
weight=fsDF[2].values
lr.fit(length,weight)
print(lr.coef_)
print(lr.score(length,weight))
a=np.polyfit(fsDF[1],fsDF[2],1)
poly_1d=np.poly1d(a)
# plt.plot(fsDF[1],poly_1d(fsDF[1]),'r')
# plt.show()
# =========================================================================================
# 데이터셋 준비-> 학습용,검증용,테스트용
# - 학습용: 모델 학습 즉, 규칙과 패턴을 찾기 위해 사용되는 데이터셋
# - 검증용: 모델 학습 진행이 제대로 되고 있는지 확인용 데이터셋
# - 테스트용: 학습 완료 후 검사용 데이터 셋
# =========================================================================================
# 전체 데이터셋 -> 학습용:테스트용=70:30
x_train,x_test,y_train,y_test=train_test_split(fsDF[[2]],fsDF[1],test_size=0.2,random_state=100)
# print(f'x_train: {x_train.shape}\n, x_test: {x_test.shape}')
# print(f'y_train: {y_train.shape}\n, y_test: {y_test.shape}')
x_train,x_val,y_train,y_val=train_test_split(x_train,y_train,test_size=0.2,random_state=100)
# print(f'x_train: {x_train.shape}\n, x_val: {x_val.shape}')
# print(f'y_train: {y_train.shape}\n, y_val: {y_val.shape}')

lr1=LinearRegression()
lr1.fit(x_train,y_train)
print(f'{lr1.coef_}')
print(lr1.score(x_val,y_val))
pred=lr1.predict(x_val)
a=mean_squared_error(y_val,pred)
b=mean_absolute_error(y_val,pred)
print(a)
print(b)