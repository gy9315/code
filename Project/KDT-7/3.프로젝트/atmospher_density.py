import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv
'''
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
# [atmophere density]
co2_density_data=pd.read_csv('./data/co2_annmean_gl_ppm.csv')
n2o_density_data=pd.read_csv('./data/n2o_annmean_gl_ppm.csv')
ch4_density_data=pd.read_csv('./data/ch4_annmean_gl_ppb.csv')
# -------------------------------------------
# co2 대기 중 농도에 대한 그래프
# 단위: ppm
co2_ylabel=co2_density_data['mean']
co2_xlabel=co2_density_data['year']
fil_y1_co2=co2_ylabel+co2_density_data['unc']
fill_y2_co2=co2_ylabel-co2_density_data['unc']
co2DF=pd.DataFrame({'mean(co2)':co2_ylabel.values,'-unc(co2)':fil_y1_co2.values,'+unc(c02)':fill_y2_co2.values},index=co2_xlabel)
# -------------------------------------------
# no2 대기 중 농도에 대한 그래프
# 단위: ppb
n2o_ylabel=n2o_density_data['mean']
n2o_xlabel=n2o_density_data['year']
fil_y1_n2o=n2o_ylabel+n2o_density_data['unc']
fill_y2_n2o=n2o_ylabel-n2o_density_data['unc']
n2oDF=pd.DataFrame({'mean(n2o)':n2o_ylabel.values,'-unc(n2o)':fil_y1_n2o.values,'+unc(n20)':fill_y2_n2o.values},index=n2o_xlabel)
# -------------------------------------------
# ch4 대기 중 농도에 대한 그래프
# 단위: ppb
ch4_ylabel=ch4_density_data['mean']
ch4_xlabel=ch4_density_data['year']
fil_y1_ch4=ch4_ylabel+ch4_density_data['unc']
fill_y2_ch4=ch4_ylabel-ch4_density_data['unc']
ch4DF=pd.DataFrame({'mean(ch4)':ch4_ylabel.values,'-unc(ch4)':fil_y1_ch4.values,'+unc(ch4)':fill_y2_ch4.values},index=ch4_xlabel)
# -------------------------------------------
