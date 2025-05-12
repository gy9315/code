import pandas as pd
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
# 입력 연도에 6월부터 9월까지 열대야 일자와 전체 횟수를 출력
# 열대야 최저온도: 25도 이상
# pandas활용하여 표현
# {'날짜':0,'지점':1,'평균기온':2,'최저기온':3,'최고기온’:4}
# 열대야 수 와 열대야 날짜
# ----------------------
# 열대야 연도 입력
# ---------------------
def main(year):
    # 파일을 오픈
    DF=pd.read_csv('../data/daegu1.csv',encoding='utf-8')
    # print(DF)
    DF.columns=['날짜','지점','평균기온','최저기온','최고기온']
    # 설계
    # 1. 열대야 날짜 출력
    # 2. 열대야 총 횟수 출력 
    # 날짜 타입 변경
    DF['날짜']=pd.to_datetime(DF['날짜'],format='%Y-%m-%d')
    # 본격 작업
    # --------------------------------------------------------------------------------------------------------
    # 연도=year, 월 in [6,7,8,9], '최저온도' >=25
    DF1=DF[(DF['날짜'].dt.year==year) & (DF['날짜'].dt.month.isin([6,7,8,9])) & (DF['최저기온'].astype('float')>=25)]
    for x in range(DF1.shape[0]):
        print(f'{DF1['날짜'].dt.month.values[x]}-{DF1['날짜'].dt.day.values[x]}: {DF1['최저기온'].values[x]}')
    print(f'{year}년 총 열대야 수는 {DF1.shape[0]}')


def input_main():
    x=input('열대야를 계산할 연도를 입력력하세요')
    main(int(x))
    
input_main()
