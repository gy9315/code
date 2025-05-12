## 생성된 MyDummyClassifier를 이용해 타이타닉 생존자 예측 수행
import pandas as pd
from sklearn.linear_model import Ridge,LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.base import BaseEstimator
import numpy as np
from sklearn.datasets import load_digits
from sklearn.preprocessing import Binarizer
from sklearn.linear_model import LogisticRegression
import numpy as np



df=pd.read_csv('../DATA/titanic_train.csv')

## Null 처리 함수
def fillna(df):
    df['Age']=df['Age'].fillna(df['Age'].mean())
    df['Cabin']=df['Cabin'].fillna('N')
    df['Embarked']=df['Embarked'].fillna('N')
    df['Fare']=df['Fare'].fillna(0)
    return df

# ## 머신러닝에 불필요한 피처 제거
def drop_features(df):
    df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
    return df

# ## Label Encoding 수행
def format_features(df):
    df['Cabin'] = df['Cabin'].str[:1]
    features = ['Cabin', 'Sex', 'Embarked']
    for feature in features:
        le = LabelEncoder()
        le.fit(df[feature])
        df[feature] = le.transform(df[feature])
    return df

# ## 앞에서 실행한 Data Preprocessing 함수 호출
def transform_features(df):
    df = fillna(df)
    df = drop_features(df)
    df = format_features(df)
    return df

DF=transform_features(df)

class MyDummyClassfier(BaseEstimator):
    def fit(self,x, y=None):
        pass
    def predict(self,x):
        pred=np.zeros((x.shape[0],1))
        for i in range(x.shape[0]):
            if x['Sex'].iloc[i]==1:
                pred[i]=0
            else: 
                pred[i]=1
        return pred
    
y_DF=DF['Survived']
DF=DF.drop(columns={'Survived'})
# train_test_split()
x_train,x_test,y_train,y_test=train_test_split(DF,y_DF,random_state=0)
md=MyDummyClassfier()
md.fit(x_train,y_train)
pred=md.predict(x_test)
print(f'myDummyclassfier: {accuracy_score(y_test,pred):.4f}')

class MyDummyClassfier(BaseEstimator):
    def fit(self,x, y=None):
        pass
    def predict(self,x):
        return np.zeros((len(x),1))

digits=load_digits()
y=(digits.target==7).astype('int')
print(y)
x_train,x_test,y_train,y_test=train_test_split(digits.data,y,random_state=0)
md=MyDummyClassfier()
md.fit(x_train,y_train)
pred=md.predict(x_test)
print(f'myDummyclassfier: {accuracy_score(y_test,pred):.4f}')

# print(confusion_matrix(y_test,pred))
# =======================================================================
def get_clf_eval(y_test,pred):
    confusion=confusion_matrix(y_test,pred)
    accuracy=accuracy_score(y_test,pred)
    precision=precision_score(y_test,pred)
    recall=recall_score(y_test,pred)
    print('오차행렬')
    print(confusion)
    print(f'정확도: {accuracy}, 정밀도: {precision}, 재현율: {recall}')
    
    
logist1=LogisticRegression(solver='liblinear')
x_train,x_test,y_train,y_test=train_test_split(DF,y_DF,random_state=0)
logist1.fit(x_train,y_train)
pred=logist1.predict(x_test)
get_clf_eval(y_test,pred)

x=[[1,-1,2],[2,0,0],[0,1.1,1.2]]
b=Binarizer(threshold=1.1)
print(b.fit_transform(x))

a=logist1.predict_proba(x_test)[:,1]
# print(a)
# print(pred)
b=Binarizer(threshold=0.51)
pred_proba=b.fit_transform(a)
get_clf_eval(y_test,pred_proba)
get_clf_eval(y_test,pred)
