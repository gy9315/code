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
# [temp]|
# 그래프 그리기
sum_value=pd.Series(sum_value)/1000
plt.figure(figsize=(20,7))
plt.plot(global_temp["Time"][:-11],sum_value,'go--',ms=2,linewidth=1,c='goldenrod',label='Sun Ifrared Radiation')
plt.fill_between(global_temp["Time"][:-11],(sum_value-0.0005),(sum_value+0.0005),color='r',alpha=0.2)
# 이동평균 추세선 그리기
sum_value=sum_value.rolling(window=20,min_periods=1).mean()
plt.plot(global_temp['Time'][:-11],sum_value,color='y',label='Moving Average Line')
# --------------------------------------------------------------------------------------
plt.xlabel("Year",fontsize=13)
plt.ylabel("Infrared Radiation(W/m2)")
plt.title("Changes in the Total Amount of Infrared Radiation by Year",pad=15,fontweight='bold')
plt.xticks(global_temp["Time"][::5],global_temp["Time"][::5])
plt.grid()
plt.legend(loc=2)
plt.show()