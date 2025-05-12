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
    f=open('../data/daegu1.csv',encoding='utf-8')
    data=csv.reader(f)
    # 설계
    # 1. 열대야 날짜 출력
    # 2. 열대야 총 횟수 출력 
    # 변수를 설정
    mon_list=[]
    temp_list=[]
    # 본격 작업
    next(data)  
    for x in data:      
        if x[1].isnumeric():
            date_string=x[0].split('-')
            # 조건 설정
            if int(date_string[0])==year and float(x[3])>=25 and int(date_string[1]) in [6,7,8,9]:
                # 월/일 집어넣기
                mon_list.append('-'.join([date_string[1],date_string[2]]))
                # 값 집어넣기
                temp_list.append(x[3])
        else:pass
    for x,y in zip(mon_list,temp_list):
        print(f'{x}: {y}')
    print(f'{year}년의 총 열대야 수는 {len(mon_list)}')
    f.close()

def input_main():
    x=input('열대야를 계산할 연도를 입력력하세요')
    main(int(x))
    
input_main()
