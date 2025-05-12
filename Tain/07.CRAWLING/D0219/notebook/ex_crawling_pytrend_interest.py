from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
pytrend=TrendReq(hl='ko',tz=540)
kw_list=['chicken','beef','pork','salmon']
# pytrend.build_payload(kw_list,cat=0,timeframe='2023-10-01 2023-12-01',geo='KR')
# df=pytrend.interest_over_time()
# print(df)
# plt.plot(df.index,df.chicken)
# plt.plot(df.index,df.beef)
# plt.plot(df.index,df.pork)
# plt.plot(df.index,df.salmon)
# plt.legend(['chicken','beef','pork','salmon'])
# plt.show()
# kw_list=['chatGPT','Gemini','Copilot','DeepSeek']
# pytrend.build_payload(kw_list,cat=0,timeframe='2023-10-01 2023-12-01',geo='KR')

DF=pd.DataFrame({1:['2020-01-04','2021-01-05','2024-01-06'],2:[3,4,5]})
print(DF)
DF[1]=pd.to_datetime(DF[1],format=('%Y-%m-%d'))
print(DF[1].dtype)
print(DF[1].dt.strftime('%m-%d').to_list())