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
# print(DF.columns)
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

# print(DF['일시'])
DF['일시']=DF['일시'].dt.strftime('%Y-%m(%U)')
DFT=DF.T.copy()
DFT.columns=DFT.loc['일시'].values
DFT.drop(index='일시',inplace=True)
DFT.columns=pd.MultiIndex.from_tuples([x.split('-') for x in DFT.columns])
print(DFT)   # 평균기온에 대한 상관계수
# print(DFT.loc[['평균기온']])
compare_list=['평균기온','평균풍속', '평균기압', '평균전운량']
fig,axes=plt.subplots(2,2)
plt.suptitle('1970 ~ 2025년 월(주) 별 기후 변화 추이',fontsize=15,fontweight='bold',color='green')
count=1
count1=1
for ax,com in zip(axes.flatten(),compare_list):
    a=DFT.loc[[com]].unstack(level=1).groupby(level=1,axis=0)
    count=1
    count1=1
    for x in a:
        value=x[1].values
        xs=np.arange(0,len(value))
        xs=xs.astype(float)
        value=value.astype(float)
        a=np.polyfit(xs,value,3)
        poly_ld=np.poly1d(a)
        ys=poly_ld(xs)
        if abs(a[0])<=3e-4:
            ax.plot(xs,ys,color='lightgrey')
        else:
            ax.plot(xs,ys,color='tomato')
            print(x[1].index[0])
            count1+=1
        count+=1
        ax.set_xlim(0,55)
        ax.set_xticks(range(0,56,5),range(1970,2026,5))
        ax.set_title(f'{com}(Ideal ratio: {(count1/count)*100:.2f})')
    ax.plot([0],[value.max()],color='lightgrey',label='Normal Value')
    ax.plot([0],[value.max()],color='tomato',label='Ideal Value')
    ax.legend(loc=1)
plt.tight_layout()
plt.show()
