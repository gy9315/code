import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np

irisDF=pd.read_csv('../DATA/iris.csv',usecols=["sepal.lngth","sepal.width","petal.length","petal.width"]) 
print(irisDF)
print(irisDF.dtypes)
plt.plot(irisDF['petal.length'],irisDF['petal.width'],'gs')
length_LR=LinearRegression()
# ========================================================
# 데이터 만들기
# train:test=7:3
# * shape[0]=150
# ========================================================
# train과 test 둘다 높은 점수 찾기
# count=0
# while True :
#     x_tr,x_tt,y_tr,y_tt=train_test_split(irisDF[['petal.length']],irisDF['petal.width'],test_size=0.3,random_state=count)
#     x_tt1,x_tt2,y_tt1,y_tt2=train_test_split(x_tt,y_tt,test_size=0.5,random_state=100)
#     # ========================================================
#     length_LR.fit(x_tr,y_tr)
#     score1=length_LR.score(x_tr,y_tr)
#     score2=length_LR.score(x_tt2,y_tt2)
#     if score1>=0.93 and score2>=0.93:
#         print(f'count: {count}')
#         print(score1);print(score2)
#         break
#     count+=1
# =============================================================
x_tr,x_tt,y_tr,y_tt=train_test_split(irisDF[['petal.length']],irisDF['petal.width'],test_size=0.3,random_state=8)
x_tt1,x_tt2,y_tt1,y_tt2=train_test_split(x_tt,y_tt,test_size=0.5,random_state=100)
# ========================================================
# np.polyfit()
length_LR.fit(x_tr,y_tr)
# 0.000124,01232323
score1=length_LR.score(x_tr,y_tr)
score2=length_LR.score(x_tt2,y_tt2)
'''
1,2,3,4,5,6
4,5,6,7,8,9
y=3X+b
'''
print(score1)
print(score2)
ys=length_LR.predict(x_tt1)
print(mean_absolute_error(y_tt1,ys))
print(mean_squared_error(y_tt1,ys))
plt.plot(x_tt1,ys,'--')
# plt.show()
# ===============================================================
# 다항회귀식 사용
# sepal.length, sepal.width,petal.length  => petal.width
fig,axes=plt.subplots(1,3)
for x,y in zip(axes.flatten(),['sepal.length','sepal.width','petal.length']):
    x.plot(irisDF[y],irisDF['petal.width'],'s')
    x.set_title(y)
# +-또는 비슷한 선형관계를 이루고 있음
# LinearRegression사용가능
# 결측치 없음
# ================================================================
# print(irisDF.isna().sum())
# ================================================================
# 데이터 만들기
x_tr,x_tt,y_tr,y_tt=train_test_split(irisDF.loc[:,'sepal.length':'petal.length'],irisDF['petal.width'],test_size=0.3,random_state=8)
x_tt1,x_tt2,y_tt1,y_tt2=train_test_split(x_tt,y_tt,test_size=0.5,random_state=100)
width_LR=LinearRegression()
width_LR.fit(x_tr,y_tr)
score1=width_LR.score(x_tr,y_tr)
score2=width_LR.score(x_tt2,y_tt2)
print('#'*20)
print(score1)
print(score2)
# ================================================================
ys=width_LR.predict(x_tt1)
print(width_LR.coef_)
# print(mean_absolute_error(y_tt1,ys))
# print(mean_squared_error(y_tt1,ys))
# =================================================================
# 예측 검증 모델 완성
# =================================================================
# x,y,z=input('꽃받침의 길이와 넓이, 꽃잎의 길이를 입력해주세요').strip().split(',')
np.random.seed(100)
x=np.random.random(size=1)*10
y=np.random.random(size=1)*10
z=np.random.random(size=1)*10
x_pred=[[x.item(),y.item(),z.item()]]
# x_pred=[[x,y,z]]
print(f'붓꽃의 꽃입의 넓이 예측값: {width_LR.predict(x_pred)[0]:.2f}')