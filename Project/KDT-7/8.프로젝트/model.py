from sklearn.utils import all_estimators
from sklearn.metrics import classification_report,precision_score,recall_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegressionCV
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
normal=pd.read_csv('./DATA/normal_cup.csv')
normal_nomask=pd.read_csv('./DATA/normal_nomask_cup.csv') 
damage=pd.read_csv('./DATA/damage_cup.csv') 
damage_nomask=pd.read_csv('./DATA/damage_nomask_cup.csv') 
dataDF=pd.concat([normal,normal_nomask,damage,damage_nomask])
print(dataDF.shape)
featureDF=dataDF.iloc[:,:-1]
scale=MinMaxScaler()
featureDF=scale.fit_transform(featureDF.values)
# featureDF=featureDF*featureDF
targetSR=dataDF.iloc[:,-1]
#=======================================================
test=pd.read_csv('./DATA/test_damage_nomask.csv')
#=======================================================
# # print(test)
test=scale.transform(test.values)
# test=test*test
# print(a)
x_train,x_test,y_train,y_test=train_test_split(featureDF,targetSR.values,stratify=targetSR)
# classfiers=all_estimators(type_filter='classifier')
# dict1={}
# # ============================================================================
# for name,class_ in classfiers:   
#     try:
#         model=class_()
#         if 'Logistic' in name or 'SGD' in name or 'MLP' in name:
#             model.set_params(max_iter=10000)
#         if 'SV' in name:
#             model.set_params(max_iter=100000, dual='auto')   
#         model.fit(x_train,y_train)
#         score=model.score(x_train,y_train)
#         pred=model.predict(x_test)
#         a=model.predict(test)
#     except Exception as e:
#         pass
#     except ValueError as e: pass

#     # pred_proba=model.predict_proba(x_test)
#     dict1[name]=[score,precision_score(y_test,pred),recall_score(y_test,pred)]
#     print(class_,a)
# DF=pd.DataFrame(dict1,index=['점수','정밀도','재현율'])
# print(DF.T)

# print('*'*50)
# ==============================================================================
model=QuadraticDiscriminantAnalysis()
model.fit(x_train,y_train)
# score=model.score(x_train,y_train)
# pred=model.predict(x_test)
# print(classification_report(y_test,pred))
# # print(test)
# # test=test*test
a=model.predict(test)
print(a)