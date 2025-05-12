import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
DF=pd.read_csv('./DATA/(월) 매입자연령대별 아파트매매거래현황 (1).csv',encoding='euc-kr',header=None)
a=DF.iloc[1][DF.iloc[1]=='면적'].index
DF=DF.drop(columns=a)
DF=DF.drop(index=[1,2])
DF=DF.drop(columns=[0,1])
DF.reset_index(drop=True,inplace=True)
DF.columns=DF.iloc[0].values
DF.drop(index=0,inplace=True)
DF.reset_index(drop=True,inplace=True)
#======================================
region=DF['지역'].unique()
gen=DF['매입자연령대'].unique()
for x in range(2,DF.shape[1]):
    DF.iloc[:,x]=DF.iloc[:,x].str.strip('"')
    DF.iloc[:,x]=DF.iloc[:,x].str.replace(',','')
inform=DF.iloc[:,:2]
DF=DF.iloc[:,2:].astype('int')
DF=pd.concat([inform,DF],axis=1)
# print(DF)
# ====================================
newDF=pd.DataFrame()
for x in region:
    sum_value=DF[(DF['지역']==x) & (DF['매입자연령대']=='합계')].iloc[:,2:]
    # sum_value=np.array(sum_value.values.reshape(-1))
    sum_value=sum_value.values.reshape(-1)
    # print(sum_value)
    # print(sum_value.shape)
    a=DF[(DF['지역']==x) & (DF['매입자연령대']!='합계')].iloc[:,2:]/sum_value
    newDF=pd.concat([newDF,a])
newDF=newDF.apply(lambda x:round(x,2)*100)
DF=pd.concat([inform[inform['매입자연령대']!='합계'],newDF],axis=1)
# print(DF.iloc[:5,:])
# values=DF[DF['지역']=='양천구'].iloc[:,2:]
# print(values)
# # for x in values.index:
# #     ys=values.loc[x]
# #     for x in range(2,ys.shape[0]):
# #         ys1=ys[x::12]
# #         print(len(ys1))
# #         plt.plot(ys)
    
# # plt.show()
# print(DF)
value_mean=DF.iloc[:,2:].sum(axis=1)/((DF.shape[1])-2)
# region.loc['mean']=value_mean
ratio_DF=pd.concat([inform[inform['매입자연령대']!='합계'],value_mean],axis=1)
ratio_DF.replace({'20대이하':'20대','기타':'10대','70대이상':'70대'},inplace=True)

ratio_DF=ratio_DF.sort_values(by=['지역','매입자연령대'])
ratio_DF.reset_index(drop=True,inplace=True)
ratio_DF=pd.DataFrame([ratio_DF[0]]*288).T
a1=ratio_DF.iloc[:,:2]
ratio_DF=pd.concat([a1,ratio_DF],axis=1)
# print(ratio_DF)

# for x in range(291):
#     ratio_DF=pd.concat([ratio_DF,ratio_DF[[0]]],axis=1)
# print(ratio_DF)