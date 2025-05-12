## [1-1] 모듈 로딩 
import pandas as pd      # 데이터 분석 및 전처리 관련 모듈 
import numpy as np       # NaN/NAN/nan 즉, 빈칸 표시 관련 모듈
traffic_satDF=pd.read_csv(r'C:\Users\gy931\OneDrive\Desktop\KDP-7\1.프로젝트\PROJECT_DATA\교통만족도.csv',encoding='EUC-KR')
traffic_satDF
traffic_satDF.drop(traffic_satDF.columns[0],inplace=True,axis=1)
traffic_satDF=traffic_satDF.T
traffic_satDF.reset_index(names='시도',inplace=True)
traffic_satDF.rename(columns={0:'교통만족도'},inplace=True)
traffic_satDF
