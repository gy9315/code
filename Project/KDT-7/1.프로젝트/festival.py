import pandas as pd
import numpy as np
import openpyxl as xl
# [데이터 읽기]
festDF=pd.read_excel('./PROJECT_DATA/지역축제.xlsx')
# [데이터 전처리]
# 인덱스 통일
festDF.rename(columns={'광역단체명':'시도','구':'군구'},inplace=True)
festDF
# [시도 별 총 지역축제수]
sr1=pd.DataFrame([['대구광역시',0,0,0,0],['인천광역시',0,0,0,0]])
sr1.columns=['시도','1분기','2분기','3분기','4분기']
sr2=pd.DataFrame([['세종특별자치시',0,0,0,0]])
sr2.columns=['시도','1분기','2분기','3분기','4분기']
festDF[(festDF.iloc[:,0]=='부산광역시')]
festDF=pd.concat([festDF.iloc[:13],sr1,festDF[(festDF.iloc[:,0]=='대전광역시') |
           (festDF.iloc[:,0]=='광주광역시')|(festDF.iloc[:,0]=='울산광역시')],sr2,
           festDF.iloc[festDF[(festDF.iloc[:,0]=='경기도')].index[0]:]])

festDF
festDF.iloc[:2]
list1=[]
for x in festDF.iloc[:,0].drop_duplicates():
    list1.append(festDF[festDF.iloc[:,0]==x].iloc[:,2:].sum().sum())
len(list1)
fest_unique_DF=festDF.iloc[:,0].drop_duplicates()
fest_unique_DF.reset_index(drop=True,inplace=True)
fest_unique_DF=pd.concat([fest_unique_DF,pd.Series(list1)],axis=1)
fest_unique_DF.rename(columns={0:'지역축제 수'},inplace=True)
fest_unique_DF