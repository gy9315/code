import pandas as pd
import numpy as np
from scipy import stats,integrate
import matplotlib.pyplot as plt
import koreanize_matplotlib
DF=pd.read_csv('./DATA/temperature_total.csv',encoding='utf-8',index_col=0)
# print(DF)
DF=DF.drop(columns=['지점','지점명'])
# print(DF)
# print(DF.dtypes)
DF['일시']=pd.to_datetime(DF['일시'],format=('%Y-%m-%d'))
# print(DF.dtypes)
print(DF.columns)
DF.columns=['일시', '평균기온', '일강수량', '평균풍속', '평균기압','평균전운량']
# # print(DF)
DF['일강수량']=DF['일강수량'].fillna(0)
DF1=DF['일시'].dt.quarter
# # print(DF1.index)
DF=pd.concat([DF,DF1],axis=1)
DF.columns=['일시', '평균기온', '일강수량', '평균풍속', '평균기압', '평균전운량','분기']
# print(DF)
DF=DF.sort_values(by='일시',axis=0)
year_list=DF['일시'].dt.year.unique()
# print(year_list)
quater_list=range(1,5)
# 각 연도에 해당 분기에 주차별로 평균기온: 평균전운량 평균내기
total=[]
for x in year_list:
    year_DF=DF[DF['일시'].dt.year==x]
    for y in quater_list:
        quater_DF=year_DF[year_DF['분기']==y]
        week_quaterDF=quater_DF.groupby(quater_DF['일시'].dt.isocalendar()['week'])
        for a in week_quaterDF:
            total.append(a[1].mean().values)
DF=pd.DataFrame(total)
DF.columns=['일시', '평균기온', '일강수량', '평균풍속', '평균기압', '평균전운량','분기']
# print(DF)
# # 평균기온 밑 2자리, 강수량, 밑 2자리, 평균풍속 밑 2자리, 평균기강, 밑 2자리, 전운량 밑2자리
DF.loc[:,'평균기온':]=DF.loc[:,'평균기온':].apply(lambda x:round(x,2))
# # 2020년 기준 특정 index 값일 일치한다면, 그다음주 가 일치할 확률 구하기

match_list=[]
next_list=[]
# np.random.seed(100)
rand_int=np.random.choice(DF.index,1)[0]
example=DF.loc[rand_int]
example1=DF.loc[rand_int+1]
for x in year_list[1:]:
    year_DF=DF[DF['일시'].dt.year==x]
    # 평균기온 오차 정하기
    if example['평균기온']<0:
        a=year_DF['평균기온'].between(example['평균기온']*1.2,example['평균기온']*0.8)
    else:
        a=year_DF['평균기온'].between(example['평균기온']*0.8,example['평균기온']*1.2)
    # print(example['평균기온']*0.9)
    b=year_DF['평균풍속'].between(example['평균풍속']*0.8,example['평균풍속']*1.2)
    c=year_DF['평균기압'].between(example['평균기압']*0.996,example['평균기압']*1.004)
    d=year_DF['평균전운량'].between(example['평균전운량']*0.9,example['평균전운량']*1.1)
    if example['분기'] in [1,4]:
        valueDF=year_DF[a & b & c & d & ((year_DF['분기']==1) |(year_DF['분기']==4))]
    else: valueDF=year_DF[a & b & c & d & ((year_DF['분기']==2) |(year_DF['분기']==3))]
    value=valueDF.values
    try:
        for y in range(len(value)):
            if len(value)!=0:   
                match_list.append(value[y])     
                # print(value)       
            else: pass
        if len(value)!=0:
            for idx in valueDF.index:
                next_list.append(year_DF.loc[idx+1].values)
        else: pass
    except: pass
    
print(example)
print('='*40)
match_DF=pd.DataFrame(match_list)
try:
    match_DF.columns=['일시', '평균기온', '일강수량', '평균풍속', '평균기압', '평균전운량','분기']
except: pass
print(match_DF['일강수량'].mean())
next_DF=pd.DataFrame(next_list)
try:
    next_DF.columns=['일시', '평균기온', '일강수량', '평균풍속', '평균기압', '평균전운량','분기']
except: pass
# print(match_DF)
print('='*40)
print(f'다음주 날씨')
print(example1)
print('='*40)
print(next_DF['일강수량'].mean())
bin=np.arange(0,next_DF['일강수량'].max()+0.9,0.5)
label=['강수없음']
label.extend(bin[1:])
# print(label)
# print(bin)
print(next_DF)
b=pd.cut(next_DF['일강수량'],bins=bin,labels=bin[:-1],right=False)
# 강수 0 ~ 0.5 0.5 ~ 1.0, 미만 강수가 없음
try:
    kde=stats.gaussian_kde(next_DF['일강수량'])
    print()
    xs=np.linspace(0,next_DF['일강수량'].max(),100)
    ys=kde(xs)/sum(kde(xs))
    inte,_=integrate.quad(kde,-np.inf,0.5)
    inte1,_=integrate.quad(kde,0.5,np.inf)
    # =========================================================
    # 시각화
    plt.suptitle('[다음주 평균 강수량의 확률 그래프]',fontweight='bold',fontsize=20)
    plt.plot(xs,kde(xs))
    plt.axvline(next_DF['일강수량'].mean(),linestyle='--',color='r')
    xs=np.linspace(0,0.5,100)
    plt.fill_between(xs,(kde(xs)),alpha=0.5,color='y')
    xs=np.linspace(0.5,next_DF['일강수량'].max(),100)
    plt.fill_between(xs,(kde(xs)),alpha=0.5,color='royalblue')
    plt.title(f'비가 오지 않을 확률: {inte*100:.1f}%, 비가 올 확률: {inte1*100:.1f}%')
    plt.text(next_DF['일강수량'].mean(),kde(next_DF['일강수량'].mean()),round(next_DF['일강수량'].mean(),1),size=15,fontweight='bold',label='예측 평균 강수량')
    plt.tight_layout()
    plt.legend()
    plt.show()
except: pass
# 연도별 거리별 차별화
# 단계 1970 ~ 1977 
# +1
# 단계 1978 ~ 1995
# +2
# 단계 1996 ~ 2014
# +3
# 단계 2015 ~ 2021
# +4
# 단계 2022 ~ 