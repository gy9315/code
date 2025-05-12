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
import joblib
from sklearn.pipeline import make_pipeline 
MODEL_FILE = './cgi-bin/damage.pkl'

normal=pd.read_csv('../DATA/normal_cup.csv')
normal_nomask=pd.read_csv('../DATA/normal_nomask_cup.csv') 
damage=pd.read_csv('../DATA/damage_cup.csv') 
damage_nomask=pd.read_csv('../DATA/damage_nomask_cup.csv') 
dataDF=pd.concat([normal,normal_nomask,damage,damage_nomask])
print(dataDF.shape)
featureDF=dataDF.iloc[:,:-1]
targetSR=dataDF.iloc[:,-1]
model=make_pipeline(MinMaxScaler(), QuadraticDiscriminantAnalysis(reg_param=0.001))
x_train,x_test,y_train,y_test=train_test_split(featureDF,targetSR.values,stratify=targetSR)
model.fit(x_train,y_train)
joblib.dump(model, MODEL_FILE)