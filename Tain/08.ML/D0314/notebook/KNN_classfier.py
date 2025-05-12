# 데이터 셋: fish.csv
# 주제: 2가지 생선 분류
# target: species
# feature: length, weigth 중 1개
# =============================
import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report
fishDF=pd.read_csv('../DATA/fish.csv',usecols=[0,1,2])
DATA=fishDF[(fishDF['Species']=='Bream') | (fishDF['Species']=='Smelt')]

y_label=DATA['Species']
label=LabelEncoder()
label.fit(y_label)
y_label=label.transform(y_label)
print(label.classes_)
x_label=DATA[['Weight','Length']]
x_train,x_test,y_train,y_test=train_test_split(x_label,y_label,stratify=y_label)
knc=KNeighborsClassifier()
knc.fit(x_train,y_train)
score=knc.score(x_train,y_train)
pred=knc.predict(x_test)
pred_proba=knc.predict_proba(x_test)
print(pred_proba)
print(f'점수: {score}')
print(classification_report(y_test,pred))
# x값이 두개이고
# y값이 두개인데
# x값에 순서 y 값에 순서
plt.scatter(x_train['Weight'],x_train['Length'],c=y_train)
# ======================================================
new_data=pd.DataFrame([[200,24]],columns=x_train.columns)
pred_data=knc.predict(new_data)
print(label.classes_[pred_data][0])
# ======================================================
a,b=knc.kneighbors(new_data)
x=x_train['Weight'].iloc[b[0]]
y=x_train['Length'].iloc[b[0]]
color=y_train[b[0]]
plt.scatter(x,y,c='red')
plt.show()