## [1-1] 모듈 로딩 
import pandas as pd      # 데이터 분석 및 전처리 관련 모듈 
import numpy as np       # NaN/NAN/nan 즉, 빈칸 표시 관련 모듈
FILE_EXCEL='./PROJECT_DATA/관광지수1.xlsx'
## [1-3] 엑셀 파일의 모든 시트를 딕셔너리로 불러오기 
## - sheet_name=None을 이용하여 모든 시트를 한번에 불러옴
all_sheets=pd.read_excel(FILE_EXCEL, sheet_name=None)
all_sheets=pd.concat(all_sheets.values(), ignore_index=True)
all_sheets.iloc[:,2].unique()
all_sheets.iloc[:,:3].isna().sum()
landmarkDF=all_sheets.iloc[:,:3]
landmarkDF.dropna(inplace=True)
list2=[]
# landmarkDF[['시도','군구']].drop_duplicates(inplace=True)
y = landmarkDF.iloc[:,:2].drop_duplicates().values
list2 = []
# 1.대단위 내 소단위 관광지 숫자 합하기 방법
# for x in y:
#     # x[0]: '시도', x[1]: '군구' 값
#     z=len(landmarkDF[(landmarkDF['시도'] == x[0])&(landmarkDF['군구'] == x[1])].index)
#     list2.append(z)
# --------------------------------------------------------------------------------
# 2.대단위 내 소단위 관광지 숫자 합하기 방법
for x in y:
    list2.append(len(landmarkDF[(landmarkDF.iloc[:,:2]==x).all(axis=1)].index))
list2
landmark_smallDF=landmarkDF.iloc[:,:2].drop_duplicates()
landmark_smallDF['관광지 수']=list2
landmark_smallDF.reset_index(drop=True, inplace=True)
landmark_smallDF

# 대단위 내 가장 가장많은 관광지를 보유하고 있는 구/군 데이터
landmark_best_smallDF=pd.DataFrame()
for x in landmark_smallDF['시도'].unique():    
    count=landmark_smallDF[(landmark_smallDF['시도']==x)]['관광지 수'].max()
    landmark_best_smallDF=pd.concat([landmark_best_smallDF,landmark_smallDF[(landmark_smallDF['관광지 수']==count) & (landmark_smallDF['시도']==x)]])
landmark_best_smallDF.reset_index(drop=True,inplace=True)
landmark_best_smallDF

list2=[]
for x in landmarkDF.iloc[:,0].drop_duplicates().values:
    list2.append(len(landmarkDF[landmarkDF.iloc[:,0]==x].index))
len(list2)
landmark_bigDF=landmarkDF.iloc[:,:1].drop_duplicates()
landmarkDF['시도'].unique()
landmark_bigDF['관광지 수']=list2
landmark_bigDF.reset_index(drop=True,inplace=True)
landmark_bigDF