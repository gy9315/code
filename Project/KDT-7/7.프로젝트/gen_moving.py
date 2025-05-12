import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from moving import * 
DF=pd.read_csv('./DATA/전입전출.csv',encoding='euc-kr')
DF['구분']=DF['구분'].str.replace('[명]','')
DF.columns=DF.columns.str.replace(' 월','')
count_all=DF[DF['연령별']=='계']
DF=DF[(DF['연령별']!='계') & (DF['구분']!='총전출')]
# print(DF)
DF['연령별']=DF['연령별'].apply(lambda x:x.split('-')).str[1]
DF['연령별']=DF['연령별'].fillna('80세')
DF['연령별']=DF['연령별'].str.replace('세','')
DF['연령별']=DF['연령별'].astype('int')
# print(DF)
newDF=pd.DataFrame()
indexDF=pd.DataFrame()
for x in ['총전입','순이동']:
    for y in ['양천구','남  구1','달서구','남  구','유성구']:
        for count in [[1,20],[21,30],[31,40],[41,50],[51,60],[61,70],[70,100]]:
            a=DF[(DF['지역']==y) & ( DF['구분']==x) & ( DF['연령별'] >=count[0] ) & ( DF['연령별'] <count[1])].iloc[:,3:].sum()
            indexD=pd.DataFrame([y,count[1]-10,x])
            # print(a)
            conDF=pd.DataFrame(list(a))
            newDF=pd.concat([newDF,conDF.T],axis=0)
            indexDF=pd.concat([indexDF,indexD.T])

personDF=pd.concat([indexDF,newDF],axis=1)
personDF.columns=DF.columns
personDF.replace({'남  구1':'남구1','남  구':'남구'},inplace=True)
# print(personDF)
personDF['연령별'].replace(90,70,inplace=True)
personDF.sort_values(by=['지역','연령별'],inplace=True)
personDF.reset_index(drop=True,inplace=True)
personDF1=personDF[personDF['구분']=='총전입']
# print(personDF)
a=personDF[personDF['구분']=='총전입'].iloc[:,3:]
b=ratio_DF.iloc[:,2:]
c=a*(b.values/100)
personDF1=pd.concat([personDF1.iloc[:,:2],c],axis=1)
# print(personDF1)
ylabel=personDF1.iloc[:,-1:-289:-1].rolling(window=3,min_periods=1,axis=1).sum()-personDF1.iloc[:,-1:-289:-1]
ylabel.iloc[:,0]=ylabel.iloc[:,1]*2
ylabel.iloc[:,1]=ylabel.iloc[:,0]
# ylabel=ylabel[-1::-1]
ylabel=ylabel.iloc[:,::-1]
# print(ylabel)
# ==========================================================================================
personDF1=pd.concat([personDF1.iloc[:,:2],ylabel],axis=1)
person_in=pd.DataFrame()
person_out=pd.DataFrame()
for x in ['남구','남구1','달서구','양천구','유성구']:
    sum_in=personDF1[personDF1['지역']==x].sum()
    sum_out=personDF[personDF['구분']=='순이동'][personDF['지역']==x].sum()
    sum_in=pd.DataFrame(sum_in).T
    sum_out=pd.DataFrame(sum_out).T
    sum_in['지역']=x
    sum_out['지역']=x
    person_in=pd.concat([person_in,sum_in])
    person_out=pd.concat([person_out,sum_out])
person_in_totalDF=person_in.reset_index(drop=True)
person_out_totalDF=person_out.reset_index(drop=True)
person_in_totalDF.iloc[:,1:]=person_in_totalDF.iloc[:,1:].astype('int')
person_in_totalDF=person_in_totalDF.drop(columns='연령별')
person_out_totalDF=person_out_totalDF.drop(columns=['연령별','구분'])
person_in_totalDF.replace({'남구':'광주 남구','남구1':'부산 남구','달서구':'대구 달서구','양천구':'서울 양천구','유성구':'대전 유성구'},inplace=True)
person_out_totalDF.replace({'남구':'광주 남구','남구1':'부산 남구','달서구':'대구 달서구','양천구':'서울 양천구','유성구':'대전 유성구'},inplace=True)
# =============================================================================================
# 데이터 전처리끝
person_in_totalDF.to_csv('잠재적 매매인원.csv',encoding='utf-8')
person_out_totalDF.to_csv('순이동인원.csv',encoding='utf-8')