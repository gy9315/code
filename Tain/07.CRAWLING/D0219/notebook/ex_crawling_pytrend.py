from pytrends.request import TrendReq
pytrend=TrendReq(hl='ko',tz=540)
pytrend.build_payload([''],geo='KR',timeframe='now 1-d', gprop='')
trend_data=pytrend.trending_searches(pn='south_korea')
print(trend_data)