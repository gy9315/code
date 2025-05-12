# 데이터 셋: fish.csv
# 주제: 2가지 생선 분류
# target: species
# feature: length, weigth 중 1개
# =============================
import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.utils import all_estimators
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report
from sklearn.exceptions import *
from sklearn.naive_bayes import GaussianNB
import warnings

warnings.filterwarnings('ignore',category=UndefinedMetricWarning) 
warnings.filterwarnings('ignore',category=ConvergenceWarning) 


fishDF=pd.read_csv('../DATA/fish.csv',usecols=[0,1,2])
DATA=fishDF[(fishDF['Species']=='Bream') | (fishDF['Species']=='Smelt')]
DATA.reset_index(drop=True,inplace=True)
y_label=DATA['Species']
label=LabelEncoder()
label.fit(y_label)
y_label=label.transform(y_label)
print(label.classes_)
x_label=DATA[['Weight','Length']]
x_train,x_test,y_train,y_test=train_test_split(x_label,y_label,stratify=y_label)
classfiers=all_estimators(type_filter='classifier')
dict1={}
# ============================================================================
for name,class_ in classfiers:   
    try:
        model=class_()
        model.fit(x_train,y_train)
        score=model.score(x_train,y_train)
        pred=model.predict(x_test)
    except ConvergenceWarning as e:
        model=class_()
        model.set_params(max_iter=100000)
        model.fit(x_train,y_train)
        score=model.score(x_train,y_train)
        pred=model.predict(x_test)
    except Exception as e:
        pass
    except ValueError as e: pass

    # pred_proba=model.predict_proba(x_test)
    dict1[name]=[score,precision_score(y_test,pred),recall_score(y_test,pred)]
DF=pd.DataFrame(dict1,index=['점수','정밀도','재현율'])
print(DF)
DF=DF.T
print(DF.sort_values(by='점수'))
