import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
'''
global_temp: 온도 편차 데이터
dangerous_plus_time: 전년도와 편차가 + 0.2 이상
dangerous_minus_time: 전년도와 편차가 - 0.2 이상
'''
global_temp=pd.read_csv("./data/HadCRUT_STD.csv")  

# 데이터 확인
# print(global_temp.head())
# 그래프 그리기
# -------------------------------------------------------------------------------
# 상대비율 표현하기: 최소값: -0.72495615 최대값: 1.9026497500000001
# --------------------------------------------------------------------------------
# y축 수정 필요
# global_temp.loc[:,'Anomaly (deg C)':]=global_temp.loc[:,'Anomaly (deg C)':]+0.72495615
# global_temp.loc[:,'Anomaly (deg C)':]=global_temp.loc[:,'Anomaly (deg C)':]/1.9026497500000001
# plt.figure(figsize=(20,5))
# plt.plot(global_temp["Time"],global_temp['Anomaly (deg C)'], label="Temperature Anomaly", color="red")
# plt.fill_between(global_temp["Time"], global_temp["Lower confidence limit (2.5%)"], global_temp["Upper confidence limit (97.5%)"], color='gray', alpha=0.3, label="Confidence Interval")
# ------------------------------------------------------------------------------
# vline 그리기 준비하기
danger_plus_time=[]
danger_minus_time=[]
for x in range(global_temp.shape[0]-1):
    danger=global_temp['Anomaly (deg C)'][x]-global_temp['Anomaly (deg C)'][x+1]
    if abs(global_temp['Anomaly (deg C)'][x]-global_temp['Anomaly (deg C)'][x+1])>=0.1:
        if danger<0: danger_plus_time.append(global_temp['Time'][x+1])
        else: danger_minus_time.append(global_temp['Time'][x+1])
# print(danger_plus_time)
# print(danger_minus_time)
# plt.xticks(global_temp["Time"][::5],global_temp["Time"][::5])
# --------------------------------------------------------------------------------
# text 및 vline 그리기
# for xvp in danger_plus_time:
#     plt.axvline(x=xvp, color='b', linestyle='--')
#     plt.text(x=xvp,y=0.5,s=xvp,ha='center',va='center',color='b')
#     if xvp==danger_plus_time[-1]:
#         plt.axvline(x=xvp, color='b', linestyle='--',label='급격히 증가 지점')
#         plt.text(x=xvp,y=0.5,s=xvp,ha='center',va='center',color='b')
# for xvm in danger_minus_time:
#     plt.axvline(x=xvm, color='tomato', linestyle='--')  
#     plt.text(x=xvm,y=0.25,s=xvm,ha='center',va='center',color='r')
#     if xvm==danger_minus_time[-1]:
#         a=plt.axvline(x=xvm, color='tomato', linestyle='--',label='급격히 감소 지점')
#         plt.text(x=xvm,y=0.25,s=xvm,ha='center',va='center',color='r')
# # -------------------------------------------------------------------------------
# plt.xlabel("Time")
# plt.ylabel("Temperature Anomaly (°C)")
# plt.legend()
# plt.show()
