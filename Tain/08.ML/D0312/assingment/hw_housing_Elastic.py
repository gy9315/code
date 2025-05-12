import pandas as pd
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.metrics import mean_absolute_error,root_mean_squared_error,mean_squared_error 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.model_selection import KFold
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

DF=pd.read_csv('../DATA/housing.csv',header=None,sep=r'\s+')

DF.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
# print(DF.corr())
# print(DF.isna().sum())
# =====================================
# ['CRIM','INDUS','NOX','RM','TAX','LSTAT','ZN' 'B']
#   -0.38   -0.48  -0.42  0.69  -0.5 -0.73 0.36  0.33
x_train,x_test,y_train, y_test=train_test_split(DF.loc[:,['CRIM','ZN','INDUS','NOX','RM','DIS','TAX','PTRATIO','B','LSTAT']],DF['MEDV'])
score_rmse_dict={}
# ================================================================
# 이상치 처리
# lof=LocalOutlierFactor(n_neighbors=14,contamination=0.15)
# outlier=lof.fit_predict(pd.DataFrame(y_train))
# x_train=x_train[(outlier>=1) & (outlier<=1.1) ]
# y_train=y_train[(outlier>=1) & (outlier<=1.1) ]
# print(x_train)
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
print(x_train.shape)
# ===============================================================
for alpha in np.arange(0,1,0.01):
    kf=KFold()
    train_rmse=[]
    train_score=[]
    test_rmse=[]
    test_score=[]
    #=================================================================
    for train_idx,test_idx in kf.split(x_train):
        # ============================================================
        kx_train=x_train[train_idx]
        ky_train=y_train.iloc[train_idx]
        kx_test=x_train[test_idx]
        ky_test=y_train.iloc[test_idx]
#         #=============================================================
        model=make_pipeline(PolynomialFeatures(degree=2),ElasticNet(alpha=alpha,max_iter=3000)) 
        model.fit(kx_train,ky_train)
        score_train=model.score(kx_train,ky_train)
        score_test=model.score(kx_test,ky_test)
        ma_train=mean_absolute_error(ky_train,model.predict(kx_train))
        ma_test=mean_absolute_error(ky_test,model.predict(kx_test))
        rmse_train=root_mean_squared_error(ky_train,model.predict(kx_train))
        rmse_test=root_mean_squared_error(ky_test,model.predict(kx_test))
        train_rmse.append(rmse_train)
        train_score.append(score_train)
        test_rmse.append(rmse_test)
        test_score.append(score_test)
    score_rmse_dict[alpha]=[np.mean(train_rmse),np.mean(train_score),np.mean(test_rmse),np.mean(test_score)]
DF=pd.DataFrame(score_rmse_dict,index=['train_rmse','train_score','test_rmse','test_score'])
print(DF)
plt.plot(DF.columns,DF.loc['train_score'],'g--')
plt.plot(DF.columns,DF.loc['test_score'],'y--')
print(model.score(x_test,y_test))
# print(model.named_steps['lasso'].coef_)
# print(model.named_steps["polynomialfeatures"].get_feature_names_out())
plt.show()