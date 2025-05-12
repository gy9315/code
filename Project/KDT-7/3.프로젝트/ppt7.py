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
fig,axes=plt.subplots(1,3,figsize=(15,5))
plt.suptitle('Concentration of GreenHouse Gas  in the Atmosphere',fontweight='bold')
# ---------------------------------------------------------
ch4DF=pd.DataFrame({'mean(ch4)':ch4_ylabel.values,'-unc(ch4)':fil_y1_ch4.values,'+unc(ch4)':fill_y2_ch4.values},index=ch4_xlabel)
# --------------------------------------------------------------------------------------
# 병합하기
densityDF=pd.concat([co2DF,n2oDF,ch4DF],axis=1,ignore_index=True)
# densityDF.fillna(0.,inplace=True)

for x,y,z,a in zip(range(3),[range(3),range(3,6),range(6,9)],['Co2/ppm','N2O/ppb','CH4/ppb'],['#003049','#d62828','#f77f00']):    
    axes[x].plot(densityDF.index,densityDF.iloc[:,y[0]],label=z,color=a)
    axes[x].fill_between(densityDF.index,densityDF.iloc[:,y[1]],densityDF.iloc[:,y[2]],color='lightgray', alpha=0.3, label="Confidence Interval")
    axes[x].set_xticks(densityDF.index[::5])
    axes[x].set_xlabel("Year")
    axes[x].set_ylabel(z)
    axes[x].legend()
    axes[x].grid()
    axes[x].set_title(f"{z[:3]}")
    if z=='Co2/ppm':
        axes[x].plot(densityDF.index,[350]*len(densityDF.index),'--',c='r',label='Ideal concentration')
        axes[x].legend()
    if z=='N2o/ppb':
        axes[x].plot(densityDF.index,[300]*len(densityDF.index),'--',c='r',label='Ideal concentration')
        axes[x].legend()
    if z=='CH4/ppb':
        axes[x].plot(densityDF.index,[1800]*len(densityDF.index),'--',c='r',label='Ideal concentration')
        axes[x].legend()
# # --------------------------------------------------------------------------------------
plt.tight_layout()
plt.show()
