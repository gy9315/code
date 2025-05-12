from sklearn.linear_model import LogisticRegressionCV
from sklearn.preprocessing import LabelEncoder,StandardScaler,MinMaxScaler
from sklearn.neighbors import LocalOutlierFactor
from sklearn.model_selection import train_test_split,KFold
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
import pandas as pd
import numpy as np
DF=pd.read_csv('../DATA/iris.csv')
# 2개 feature
# print(DF['variety'].unique())
encoder=LabelEncoder()
DF['variety']=encoder.fit_transform(DF['variety'])
print(DF.corr())
# 3개 feature: ['petal.length','petal.width','sepal.length']
# scale 진행
model=make_pipeline(MinMaxScaler(),LogisticRegressionCV(Cs=np.arange(0.1,10,0.1),cv=5))
x_label=DF[['petal.length','petal.width','sepal.length']]
y_label=DF['variety']
# ===========================================================
x_train,x_test,y_train,y_test=train_test_split(x_label,y_label,stratify=y_label)
model.fit(x_train,y_train)
# print(model.score(x_train,y_train))
print(classification_report(y_test,model.predict(x_test)))
# ==========================================================


