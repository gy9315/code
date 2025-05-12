import csv
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
# 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시, 하차인원 출력
# 1호선 ~ 7호선까지 분석
# 인원수에 ','찍을 것!
# Bar x축: 노선+지하철 역이름, y축: 인원수 표시
# python 표현
# ------------------------------------------------------------------
# 자료확인
f=open('../data/subwaytime.csv',encoding='utf-8')
data=csv.reader(f,delimiter=',')
header=next(data)
# print(header)
# print(len(header))
header1=next(data)
# 읽어드리는 오류 삭제를 위해 list화 함
data=list(data)
# print(header1)
# 출근시간대 col 인덱스 11 ~ 14
# 하차 시간대 12,14
# type 확인
# count=0
# for x in data:
#     print(type(x[11]),type(x[14]))
#     count+=1 
# type은 'str' 형 변환 필요
# -------------------------------------------------------------------
# 전체 11인덱스와 14인덱스 합치기 필요
# 변수 설정
# 호선 인덱스 [1], station info [3]
sum_list=[]
station_list=[]
for x in data:
    sum_data=sum([int(x[11]),int(x[13])])
    station_list.append((x[1],x[3],sum_data))
line_best_station_list=[]
for x in range(1,8):
    a=[y for y in station_list if y[0].replace('호선','')==str(x)]
    a=sorted(a,key=lambda x:x[2],reverse=True)
    line_best_station_list.append(a[0])
# print(line_best_station_list)
x,y,z=zip(*line_best_station_list)
f.close()
# ------------------------------------------------------------------------
for a,b,c in zip(z,y,x):
    print(f'출근 시간 대 {c} 최대 하차역: {b}, 하차인원: {a:,}')
line_info=[]
for a,b in zip(x,y):
    line_info.append(a+b)
plt.figure(figsize=(10,5))
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역',size=15,pad=15)
plt.bar(line_info,z)
plt.xticks(range(0,7),line_info,rotation=85)
plt.show()