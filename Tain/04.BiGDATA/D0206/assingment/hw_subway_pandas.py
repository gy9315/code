import csv
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
# 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시, 하차인원 출력
# 1호선 ~ 7호선까지 분석
# 인원수에 ','찍을 것!
# Bar x축: 노선+지하철 역이름, y축: 인원수 표시
# pandas 표현
DF=pd.read_csv('../data/subwaytime.csv',encoding='utf-8',header=[0,1])
DF1=pd.concat([DF.iloc[:,:4],DF.iloc[:,11:14:2].sum(axis=1)],axis=1)
# 저장변수 설정
line_num=[]
station_list=[]
for x in range(1,8):
    a=DF1[DF1[('호선명', 'Unnamed: 1_level_1')].str[0]==str(x)]
    # 값 뽑기
    max_value=a.iloc[:,4].max()
    line_num.append(max_value)
    max_index=a.iloc[:,4].idxmax()
    station_list.append(a.iloc[:,3][max_index])
# -------------------------------------------------------------------
for x,y,z in zip(line_num,station_list,range(1,8)):
    print(f'출근 시간 대 {z}호선 최대 하차역: {y}, 하차인원: {x:,}')
line_info=pd.Series(range(1,8)).apply(str)+'호선'
line_info=line_info+' '+pd.Series(station_list)
plt.figure(figsize=(10,5))
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역',size=15,pad=15)
plt.bar(line_info,line_num)
plt.xticks(range(0,7),line_info,rotation=85)
plt.show()