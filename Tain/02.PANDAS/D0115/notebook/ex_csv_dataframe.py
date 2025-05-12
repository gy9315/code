# csv 데이터 파일을 => pandas의 DataFrame으로 읽기
# 모듈 로딩
import pandas as pd
# 전역변수: 파일 전체에서 사용
DATA_PATH=r'C:\Users\gy931\OneDrive\Desktop\KDP-7\02.PANDAS\DATA\iris.csv'
# 데이터 읽기- 방법 (1) 일반 파일 읽기 방식
# - 파이썬 내장함수: open(파일경로+이름, 열기모드,인코딩방식)
#                   read(), write()
#                   close()
dataF=open(DATA_PATH,mode='r',encoding='utf-8')
# 파일에서 읽기

all_lines=dataF.readlines()
# print(f'[모든 라인데이터]: {all_lines}')
# for line in all_lines:
    # print(line.split(','))
# 파일닫기
# dataF.close()
# 데이터 읽어들이기 - 방법 (2) Pandas 파일 읽기 방식
# - Pandas 내장함수: read_csv(파일경로+파일명)
#                   => DataFrame으로 읽어 들익

# CSV 파일 => DataFrame 읽기
dataDF=pd.read_csv(DATA_PATH)
print(dataDF)