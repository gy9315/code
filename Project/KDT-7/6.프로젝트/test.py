import numpy as np
from scipy import stats 
import matplotlib.pyplot as plt
import pandas as pd
# np.random.seed(0)

example=pd.read_csv('./DATA/lastweek.csv',encoding='euc-kr')
example=example.drop(columns=['지점','지점명'])
example['일시']=pd.to_datetime(example['일시'],format=('%Y-%m-%d'))
print(example.columns)
example.columns=['일시', '평균기온', '일강수량', '평균풍속', '평균기압','평균전운량']
example['일강수량']=example['일강수량'].fillna(0)
example1=example['일시'].dt.quarter
example=pd.concat([example,example1],axis=1)
example.columns=['일시', '평균기온', '일강수량', '평균풍속', '평균기압', '평균전운량','분기']
example=example.sort_values(by='일시',axis=0)
year_list=example['일시'].dt.year.unique()
quater_list=range(1,5)
total=[]
for x in year_list:
    year_example=example[example['일시'].dt.year==x]
    for y in quater_list:
        quater_example=year_example[year_example['분기']==y]
        week_quaterexample=quater_example.groupby(quater_example['일시'].dt.isocalendar()['week'])
        for a in week_quaterexample:
            total.append(a[1].mean().values)
example=pd.DataFrame(total)
example.columns=['일시', '평균기온', '일강수량', '평균풍속', '평균기압', '평균전운량','분기']
example.loc[:,'평균기온':]=example.loc[:,'평균기온':].apply(lambda x:round(x,2))
print(example)