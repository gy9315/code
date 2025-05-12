import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv
from sun_iritaion_ import *
from global_temp import *
from atmospher_density import *
from atmospher_emmistion import *
'''
global_temp: 온도 편차 데이터
dangerous_plus_time: 전년도와 편차가 + 0.2 이상
dangerous_minus_time: 전년도와 편차가 - 0.2 이상

sum_value: 적외선 합친 값
  * 연도 1850 ~ 2014
  
kr_mergeDF: 한국 온실가스 배출량 데이터
  * columns 'Year','Co2','CH4','No2'
gb_mergeDF: 세계 온실가스 배출량 데이터

co2_ylabel: co2 농도 데이터
    - fil_y1_co2
    - fill_y2_c02
no2_ylabel: no2 농도 데이터
    - fil_y1_no2
    - fill_y2_n02
ch4_ylabel: ch4 농도 데이터
    - fil_y1_ch4
    - fill_y2_ch4
'''
# [temp]
# 그래프 그리기
plt.figure(figsize=(20,7))
plt.plot(global_temp["Time"],global_temp['Anomaly (deg C)'], label="Temperature Anomaly", color="k",linewidth=2)
# ---------------------------------------------------------
# 이동평균 추세선 그리기
mean_ylabel=global_temp['Anomaly (deg C)'].rolling(window=10,min_periods=1).mean()
plt.plot(global_temp["Time"],mean_ylabel,color='r')
# ---------------------------------------------------------
plt.fill_between(global_temp["Time"], global_temp["Lower confidence limit (2.5%)"], global_temp["Upper confidence limit (97.5%)"], color='gray', alpha=0.3, label="Confidence Interval")
# 변수 설정
danger_plus_time=[]
danger_plus_vline_value=[]
danger_minus_time=[]
danger_minus_vline_value=[]
# 변수 값 입력
for x in range(global_temp.shape[0]-1):
    danger=global_temp['Anomaly (deg C)'][x]-global_temp['Anomaly (deg C)'][x+1]
    if abs(global_temp['Anomaly (deg C)'][x]-global_temp['Anomaly (deg C)'][x+1])>=0.01:
        if danger<0: 
            danger_plus_time.append(global_temp['Time'][x+1])
            # 튜플 형태로 입력
            danger_plus_vline_value.append((global_temp['Anomaly (deg C)'][x+1],global_temp['Anomaly (deg C)'][x]))
        else: 
            danger_minus_time.append(global_temp['Time'][x+1])
            danger_minus_vline_value.append((global_temp['Anomaly (deg C)'][x],global_temp['Anomaly (deg C)'][x+1]))
# 추가 vline그리기 
# if danger>0: ymin(*x+1), ymax(*x)
# else: ymin(x), ymax(x+1) 
# ------------------------------------------------------------------------------------
# 위험구간 표시
plt.xticks(global_temp["Time"][::5],global_temp["Time"][::5])
# ------------------------------------------------------------------------------------
for xvp,vlines in zip(danger_plus_time,danger_plus_vline_value):
    if xvp==danger_plus_time[-1]:
        plt.vlines(x=xvp, ymin=vlines[0], ymax=vlines[1],color='b', linestyle='-',linewidth=1)
        # plt.text(x=xvp,y=vlines[0]+0.05,s=xvp,ha='center',va='center',color='b',fontweight='bold')
        plt.plot(xvp,vlines[0],'^',ms=5,color='b')
    else:
        plt.vlines(x=xvp, ymin=vlines[1], ymax=vlines[0],color='b', linestyle='-',linewidth=1)
        # plt.text(x=xvp,y=vlines[0]+0.05,s=xvp,ha='center',va='center',color='b',fontweight='bold')
        plt.plot(xvp,vlines[0],'^',ms=5,color='b')
for xvp,vlines in zip(danger_minus_time,danger_minus_vline_value):
        if xvp==danger_minus_time[-1]:
            plt.vlines(x=xvp, ymin=vlines[0], ymax=vlines[1],color='tomato', linestyle='-',linewidth=1)
            # plt.text(x=xvp,y=vlines[1]-0.05,s=xvp,ha='center',va='center',color='tomato',fontweight='bold')
            plt.plot(xvp,vlines[1],'v',ms=5,color='tomato')
        else:
            plt.vlines(x=xvp, ymin=vlines[1], ymax=vlines[0],color='tomato', linestyle='-',linewidth=1)
            # plt.text(x=xvp,y=vlines[1]-0.05,s=xvp,ha='center',va='center',color='tomato',fontweight='bold')
            plt.plot(xvp,vlines[1],'v',ms=5,color='tomato')
# [greenhous gas]
# -------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
plt.xlabel("Year",fontsize=13)
plt.ylabel("Temperature Anomaly (°C)")
plt.title("Changes in the Global Temp by Year",pad=15,fontweight='bold')
plt.grid()
plt.legend()
plt.show()