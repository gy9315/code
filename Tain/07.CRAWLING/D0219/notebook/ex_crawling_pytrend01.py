from pytrends.request import TrendReq
import pandas as pd
pytrend=TrendReq(hl='ko',tz=540)
result=pytrend.suggestions(keyword='치킨')
print(type(result))
df=pd.DataFrame(result)

df.drop(columns='mid',inplace=True)
print(df)