# DF 분기별 관광객수(2023)
## - 구/군단위 관광객수
import pandas as pd
import numpy as np
from openpyxl import *

FILENAME =r'C:\Users\gy931\OneDrive\Desktop\KDP-7\1.프로젝트\PROJECT_DATA\입장객통계.xlsx'

tourist_statics= pd.read_excel(FILENAME, sheet_name=None)
tourist_statics1 = pd.concat(tourist_statics.values(), ignore_index=True)
tourist_statics1.fillna(method='ffill', inplace=True)
tourist_statics1
tourist_statics1 = tourist_statics1[tourist_statics1['2023년 01월'] == '1분기']
DF = tourist_statics1.iloc[:, [0, 1, 3, 6, 9, 12]]
DF.reset_index(drop=True,inplace=True)
DF.columns=['시도','군구','1분기','2분기','3분기','4분기']
DF
DF[DF['시도']=='광주광역시']
DF.drop_duplicates(inplace=True)
DF.reset_index(drop=True)

region_sum_DF=pd.DataFrame()
for x in ['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원특별자치도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도']:
    y=pd.DataFrame({x:[ DF[DF.iloc[:,0]==x]['1분기'].sum(), DF[DF.iloc[:,0]==x]['2분기'].sum(), DF[DF.iloc[:,0]==x]['3분기'].sum(), DF[DF.iloc[:,0]==x]['4분기'].sum()]})
    region_sum_DF=pd.concat([region_sum_DF,y],axis=1)
region_sum_DF.index=['1분기','2분기','3분기','4분기']
region_sum_DF=region_sum_DF.T
region_sum_DF.reset_index(inplace=True,names='시도')
region_sum_DF
region_all_sum_DF=region_sum_DF.iloc[:,0]
region_all_sum_DF=pd.concat([region_all_sum_DF,region_sum_DF.iloc[:,1:].sum(axis=1)],axis=1)
region_all_sum_DF.rename(columns={0:'총 인원수'},inplace=True)
region_all_sum_DF

# 각 시별 분기별 가장 높은 지역
season_region_DF=pd.DataFrame()
for z in ['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원특별자치도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도']:
    a=pd.concat([DF[DF['1분기']==DF[DF.iloc[:,0]==z].iloc[:,2].max()].iloc[:,[0,1,2]], DF[DF['2분기']==DF[DF.iloc[:,0]==z].iloc[:,3].max()].iloc[:,[0,1,3]],DF[DF['3분기']==DF[DF.iloc[:,0]==z].iloc[:,4].max()].iloc[:,[0,1,4]],DF[DF['4분기']==DF[DF.iloc[:,0]==z].iloc[:,5].max()].iloc[:,[0,1,5]]])
    season_region_DF=pd.concat([season_region_DF,a])
season_region_DF.reset_index(drop=True)
season_region_DF




# 각 시별 구군별 가장 인원밀집이 높은 지역
# 2 ~ 5까지 전부 더 한값에 시도 군구 표현
# DF.iloc[0:2].drop(['1분기','2분기','3분기','4분기'],axis=1).iloc[2]=DF.iloc[u,2:6].sum()

#     DF.iloc[0:2].drop(['2분기','3분기','4분기'])

DF1=DF.iloc[:].drop(['1분기','2분기','3분기','4분기'],axis=1)
list1=[]
for u in range(len(DF.index)):
    list1.append(DF.iloc[u,2:6].sum())
DF1['총 인원수']=list1
DF1
print(DF1)


total_region_DF=pd.DataFrame()
for u in ['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원특별자치도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도']:
    y=pd.concat([DF1[DF1['총 인원수']==DF1[DF1.iloc[:,0]==u].iloc[:,2].max()]])
    total_region_DF=pd.concat([total_region_DF,y])
# season_region_DF.reset_index(drop=True)
total_region_DF.reset_index(inplace=True,drop=True)
total_region_DF
