import pandas as pd
from sklearn.utils import all_estimators
from sklearn.linear_model import LogisticRegressionCV,LogisticRegression
from sklearn.metrics import root_mean_squared_error,classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np
import koreanize_matplotlib
import os
from collections import Counter
# 각 언어마다 알파벳의 사용 빈도가 다르다
# 언어마다 자주 쓰이는 단어를 기준으로 데이터 프레임을 만들자
file_train=os.listdir('./DATA/train')
# print(file_train)
lanDF=pd.DataFrame()
for file_name in file_train:
    with open(f'./DATA/train/{file_name}',encoding='utf-8') as file:
        data=file.readlines()
        # print(type(data))
        data=[z for x in data if x !='\n' for y in x.replace('\n','') if y!=' ' for z in y if z.isalpha()]
    alpha=list(map(chr,list(range(ord('A'),ord('Z')+1))+list(range(ord('a'),ord('z')+1))))
    dict_total={}
    dict_alpha=dict(Counter(data))
    for x in alpha:
        try:
            dict_total[x]=dict_alpha[x]
        except:
            dict_total[x]=0
    DF=pd.DataFrame(dict_total,index=[0])
    DF.sort_index()
    DF=(DF-DF.values.min())/DF.values.max()
    DF=DF.sort_index(axis=1)
    DF['country']=file_name.split('-')[0]
    lanDF=pd.concat([lanDF,DF])
lanDF.reset_index(drop=True,inplace=True)
#==================================================================================
# 시각화 확인
#==================================================================================
# fig,axes=plt.subplots(2,2,figsize=(10,10))
# country=lanDF['country'].unique()
# # enDF=lanDF[lanDF['country']=='en']
# for x,y in zip(axes.flatten(),country):
#     enDF=lanDF[lanDF['country']==y]
#     for idx in enDF.index:
#         x.plot(enDF.columns[:-1],enDF.loc[idx][:-1])
#==================================================================================
lb=LabelEncoder()
targetDF=lb.fit_transform(lanDF['country'])
# print(targetDF.shape)
# print(lanDF.iloc[:,:-1])
x_train,x_test,y_train,y_test=train_test_split(lanDF.iloc[:,:-1],targetDF,stratify=targetDF)
# name=all_estimators('classifier')
# for x,y in name:
#     try:
#         model=y()
#         if 'Logistic' in x or 'SGD' in name or 'MLP' in name:
#             model.set_params(max_iter=10000)
#         if 'SV' in x:
#             model.set_params(max_iter=100000, dual='auto')   
#         model.fit(x_train,y_train)
#         score=model.score(x_train,y_train)
#         score1=model.score(x_test,y_test)
#         pred=model.predict(x_train)
#         pred1=model.predict(x_test)
#         class1=classification_report(y_train,pred)
#         class2=classification_report(y_test,pred1)
#         print(f'모델: {x}')
#         print(f'train score: {score}, testscore: {score1}')
#         print('train report')
#         print(class1)

#         print('test report')
#         print(class2)
#         print('*'*40)
    
#     except Exception:
#         pass
# 성능 좋은 Classifier
# ================================================================================================================
# extratreesClassfier,GradientBoostingClassifier,KNeighborsClassifier,LabelPropagation,LinearSVC,RidgeClassifierCV
# ================================================================================================================
# logistRegression 확인인
model=LogisticRegressionCV(cv=3)
model.fit(x_train,y_train)
# score=model.score(x_train,y_train)
# score1=model.score(x_test,y_test)
# pred=model.predict(x_train)
# pred1=model.predict(x_test)
# class1=classification_report(y_train,pred)
# class2=classification_report(y_test,pred1)
# print(f'train score: {score}, testscore: {score1}')
# print('train report')
# print(class1)
# print('test report')
# print(class2)
# ================================================================================================================
# TEST DATA 확인
file_test=os.listdir('./DATA/test')
# print(file_test)
lan_testDF=pd.DataFrame()
for file_name in file_test:
    with open(f'./DATA/test/{file_name}',encoding='utf-8') as file:
        data=file.readlines()
        # print(type(data))
        data=[z for x in data if x !='\n' for y in x.replace('\n','') if y!=' ' for z in y if z.isalpha()]
    alpha=list(map(chr,list(range(ord('A'),ord('Z')+1))+list(range(ord('a'),ord('z')+1))))
    dict_total={}
    dict_alpha=dict(Counter(data))
    for x in alpha:
        try:
            dict_total[x]=dict_alpha[x]
        except:
            dict_total[x]=0
    DF=pd.DataFrame(dict_total,index=[0])
    DF.sort_index()
    DF=(DF-DF.values.min())/DF.values.max()
    DF=DF.sort_index(axis=1)
    DF['country']=file_name.split('-')[0]
    lan_testDF=pd.concat([lan_testDF,DF])
lan_testDF.reset_index(drop=True,inplace=True)
target_testDF=lb.transform(lan_testDF['country'])
feature_testDF=lan_testDF.iloc[:,:-1]
# =================================================================================================
score1=model.score(feature_testDF,target_testDF)
pred=model.predict(feature_testDF)
class1=classification_report(target_testDF,pred)
print(f'score: {score1}')
print(class1)