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
global_temp.loc[:,'Anomaly (deg C)':]=global_temp.loc[:,'Anomaly (deg C)':]+0.72495615
global_temp.loc[:,'Anomaly (deg C)':]=global_temp.loc[:,'Anomaly (deg C)':]/1.9026497500000001
plt.figure(figsize=(20,7))
# ---------------------------------------------------------
# 이동평균 추세선 그리기
mean_ylabel=global_temp['Anomaly (deg C)'].rolling(window=10,min_periods=1).mean()
plt.plot(global_temp["Time"],mean_ylabel,color='r',label='Global Temp MAL')
# [sun_ifrared rays]
# --------------------------------------------------------------------------------------
sum_value=pd.Series(sum_value)/1000
sum_value=sum_value-min(sum_value)
sum_value=sum_value/max(sum_value)
# 이동평균 추세선 그리기
sum_value=pd.Series(sum_value).rolling(window=15,min_periods=1).mean()
plt.plot(global_temp['Time'][:-11],sum_value,color='y',label='Sun Infrared Radiation MAL')
# --------------------------------------------------------------------------------------
# 유심히 봐야 하는 지점 그리기
plt.fill([1945,2000,2015,1950],[0.45,0.78,0.48,0.21],color='royalblue',alpha=0.3,label='Ideal Section')
# 시작, 끝지점 그리기
plt.vlines(x=1947, ymin=0.21, ymax=0.45,color='blue', linestyle='--',linewidth=2)
plt.vlines(x=2007, ymin=0.48, ymax=0.78,color='blue', linestyle='--',linewidth=2)
plt.xlabel("Year",fontsize=13)
plt.xticks(global_temp["Time"][::5],global_temp["Time"][::5])
plt.ylabel("Relatibe Ratio")
plt.title("'Global Temp' compare to 'Ifrared Radiaton'", fontweight='bold',pad=15)
plt.grid()
plt.legend()
plt.show()