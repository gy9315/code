import pandas as pd
from sklearn.linear_model import Ridge,Lasso,ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,root_mean_squared_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np
# Ridge&Lassso&Elastic_N 정규화 모델 사용
# =============================================================================================================
irisDF=pd.read_csv('../DATA/iris.csv',usecols=["sepal.length","sepal.width","petal.length","petal.width"]) 
x_tr,x_tt,y_tr,y_tt=train_test_split(irisDF.iloc[:,:-1],irisDF['petal.width'],test_size=0.3,random_state=None)
dict1={}
for x in [0.01,0.5,1.0,1.5,2]:
    model=Ridge(alpha=x)
    kf=KFold()
    train_rmse=[]
    train_score=[]
    test_rmse=[]
    test_score=[]
    for train_idx,test_idx in kf.split(x_tr):
        # print(f'train_idx: {train_idx}\ntest_idx: {test_idx}')
        x_train=x_tr.iloc[train_idx]
        y_train=y_tr.iloc[train_idx]
        x_test=x_tr.iloc[test_idx]
        y_test=y_tr.iloc[test_idx]
        model.fit(x_train,y_train)
        score_train=model.score(x_train,y_train)
        score_test=model.score(x_test,y_test)
        rmse_train=root_mean_squared_error(y_train,model.predict(x_train))
        rmse_test=root_mean_squared_error(y_test,model.predict(x_test))
        train_rmse.append(rmse_train)
        train_score.append(score_train)
        test_rmse.append(rmse_test)
        test_score.append(score_test)
    dict1[x]=[np.mean(train_rmse),np.mean(train_score),np.mean(test_rmse),np.mean(test_score)]
DF=pd.DataFrame(dict1,index=['train_rmse','train_score','test_rmse','test_score'])
print(DF)
plt.plot(DF.columns,DF.loc['train_score'],'g--')
plt.plot(DF.columns,DF.loc['test_score'],'y--')
plt.show()
# # ===============================================================
