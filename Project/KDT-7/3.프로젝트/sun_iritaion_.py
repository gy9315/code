import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv
'''
sum_value: 적외선 합친 값
  * 연도 1850 ~ 2014
'''
f=open('./data/solar_value.txt')
sun_data=list(csv.reader(f,delimiter='\t'))
count=0
final_sun_sun_data={}
sun_data_value=[]
sum_value=[]
for x in sun_data:
    y=x[0].strip().split('  ')
    if len(y)==5:
        sun_data_value.append(y)
    elif len(y)==7:
        # 241번 부터 수행
        DF=pd.DataFrame(sun_data_value)
        count+=1
        # 초기화
        sun_data_value=[]
        DF=DF.astype('float')      
        if count>=242:
            sum_value_row=DF.loc[20:,:].sum().sum()+DF.loc[19,4]
            sum_value.append(sum_value_row)
        else:pass
# ---------------------------------------------------------------
# total_파장 계산하기
total_sum=[]
count=0
for x in sun_data:
    y=x[0].strip().split('  ')
    if len(y)==7:
        if count>=242:
            total_sum.append(y[3])
        else: pass
        count+=1
# ------------------------------------------------------------
# 상대비율 만들기
# sum_value=sum_value-min(sum_value)
# sum_value=sum_value/max(sum_value)
# # ------------------------------------------------------------
# total_sum=pd.Series(total_sum).astype('float')
# # total_sum=total_sum-min(total_sum)
# # total_sum=pd.Series(total_sum)/max(total_sum)
# plt.figure(figsize=(20,5))
# # plt.plot(range(1850,2013),total_sum)
# plt.plot(range(1850,2013),pd.Series(sum_value[:-1])/1000)
# plt.xticks(range(1850,2014,5))
# plt.show()