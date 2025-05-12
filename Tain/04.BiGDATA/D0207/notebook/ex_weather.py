import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
weatherDF=pd.read_excel('../data/weather.xlsx')
dustDF=pd.read_excel('../data/dust_hour.xlsx')
dustDF['date']=pd.to_datetime(dustDF['date'],format='%Y-%m-%d %H')
# print(weatherDF.info())
weatherDF.drop(columns=['지점','지점명'],inplace=True)
# print(weatherDF.columns)
weatherDF.columns=['date', 'temp', 'wind', 'rain', 'humidity']
weatherDF['date']=pd.to_datetime(weatherDF['date'],format='%Y-%m-%d %H')
# print(tabulate(weatherDF.head(),headers='keys',tablefmt='pretty'))
# print(weatherDF.isna().sum())
weatherDF['rain']=weatherDF['rain'].replace(0,0.01)
# data 특정 조건으로 병합하기
# method=merge()
# parameter
## how: 어떤 방식으로 병합 outer or inner(교집합)
## on: 조건(어떤 컬럼을 기준으로 병합)
merge_DF=pd.merge(dustDF,weatherDF,how='inner',on='date')
print(tabulate(merge_DF.head(),headers='keys',tablefmt='pretty'))
