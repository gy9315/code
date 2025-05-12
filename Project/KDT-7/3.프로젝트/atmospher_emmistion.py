import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv
'''
kr_mergeDF: 한국 온실가스 배출량 데이터
  * columns 'Year','Co2','CH4','No2'
gb_mergeDF: 세계 온실가스 배출량 데이터
'''

co2_emmision_data=pd.read_csv('./data/annual-co-emissions.csv')
no2_emmision_data=pd.read_csv('./data/nitrous-oxide-emissions.csv')
ch4_emmision_data=pd.read_csv('./data/methane-emissions.csv')
# -------------------------------------------
# [co2 배출량에 대한 그래프}
# global
gb_co2_emmision_data=co2_emmision_data[co2_emmision_data['Entity']=='World']
gb_co2_emmision_data=gb_co2_emmision_data.drop(columns='Entity')
gb_co2_emmision_data.reset_index(drop=True,inplace=True)
gb_co2_emmision_data=gb_co2_emmision_data[gb_co2_emmision_data['Year']>=1850]
# south Korea
# 1905년 부터 2023년까지지
kr_co2_emmision_data=co2_emmision_data[co2_emmision_data['Entity']=='South Korea']
kr_co2_emmision_data=kr_co2_emmision_data.drop(columns='Entity')
kr_co2_emmision_data.reset_index(drop=True,inplace=True)
# print(kr_co2_emmision_data)
# --------------------------------------------
# {no2 배출량에 대한 그래프}
gb_no2_emmision_data=no2_emmision_data[no2_emmision_data['Entity']=='World']
gb_no2_emmision_data=gb_no2_emmision_data.drop(columns='Entity')
gb_no2_emmision_data.reset_index(drop=True,inplace=True)
gb_no2_emmision_data=gb_no2_emmision_data[gb_no2_emmision_data['Year']>=1850]
# south Korea
# 1850년 부터 2023년까지지
kr_no2_emmision_data=no2_emmision_data[no2_emmision_data['Entity']=='South Korea']
kr_no2_emmision_data=kr_no2_emmision_data.drop(columns='Entity')
kr_no2_emmision_data.reset_index(drop=True,inplace=True)
# print(kr_no2_emmision_data)
# ------------------------------------------------
# {ch4 배출량에 대한 그래프}
gb_ch4_emmision_data=ch4_emmision_data[ch4_emmision_data['Entity']=='World']
gb_ch4_emmision_data=gb_ch4_emmision_data.drop(columns='Entity')
gb_ch4_emmision_data.reset_index(drop=True,inplace=True)
gb_ch4_emmision_data=gb_ch4_emmision_data[gb_ch4_emmision_data['Year']>=1850]
# south Korea
# 1850년 부터 2023년까지지
kr_ch4_emmision_data=ch4_emmision_data[ch4_emmision_data['Entity']=='South Korea']
kr_ch4_emmision_data=kr_ch4_emmision_data.drop(columns='Entity')
kr_ch4_emmision_data.reset_index(drop=True,inplace=True)
# print(kr_ch4_emmision_data)
# --------------------------------------------------



# 하나의 DF로 합치기
# korea
mergeDF=pd.merge(kr_ch4_emmision_data,kr_no2_emmision_data,on='Year')
kr_mergeDF=pd.merge(kr_co2_emmision_data,mergeDF,on='Year')
kr_mergeDF.columns=['Year','Co2','CH4','N2O']
# print(kr_mergeDF)
# global
mergeDF=pd.merge(gb_ch4_emmision_data,gb_no2_emmision_data,on='Year')
gb_mergeDF=pd.merge(gb_co2_emmision_data,mergeDF,on='Year')
gb_mergeDF.columns=['Year','Co2','CH4','N2O']
# print(gb_mergeDF)
# ---------------------------------------------------------
# 상대 비율 만들기
kr_mergeDF
for x in kr_mergeDF.columns[1:]:
    min_value=kr_mergeDF[x].min()
    kr_mergeDF[x]=kr_mergeDF[x]-min_value
    max_value=kr_mergeDF[x].max()
    # min 값 전체 빼고 max값으로 나누기
    kr_mergeDF[x]=kr_mergeDF[x]/max_value
gb_mergeDF
for x in gb_mergeDF.columns[1:]:
    min_value=gb_mergeDF[x].min()
    gb_mergeDF[x]=gb_mergeDF[x]-min_value
    max_value=gb_mergeDF[x].max()
    # min 값 전체 빼고 max값으로 나누기
    gb_mergeDF[x]=gb_mergeDF[x]/max_value
# --------------------------------------------------------
# colors=['royalblue','tomato','green']
# for x,y in zip(gb_mergeDF.columns[1:],range(3)):
#     plt.plot(gb_mergeDF['Year'],gb_mergeDF[x],label=x)
# plt.legend()
# plt.show()