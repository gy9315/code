## [1-1] 모듈 로딩 
import pandas as pd      # 데이터 분석 및 전처리 관련 모듈 
import numpy as np       # NaN/NAN/nan 즉, 빈칸 표시 관련 모듈
payDF=pd.read_csv('./PROJECT_DATA/지출액.csv',encoding='EUC-KR')
payDF.drop(payDF.columns[0],inplace=True,axis=1)
payDF=payDF.T
payDF.reset_index(names='시도',inplace=True)
payDF.rename(columns={0:'지출액'},inplace=True)
payDF
