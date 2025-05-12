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
# --------------------------------------------------------------------------------------
# [atmosphere_emmision]
# --------------------------------------------------------------------------------------
colors=['#003049','#d62828','#f77f00']
for x,y in zip(gb_mergeDF.columns[1:],range(3)):
    plt.plot(gb_mergeDF['Year'],gb_mergeDF[x],label=x,color=colors[y])
# --------------------------------------------------------------------------------------
plt.xlabel("Year",fontsize=13)
plt.ylabel("Relatibe Ratio")
plt.xticks(global_temp["Time"][::5],global_temp["Time"][::5])
plt.title("Emmision of GreenHouse Air by Year",pad=15,fontweight='bold')
plt.grid()
plt.legend()
plt.show()