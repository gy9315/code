# DataFrame 생성하기: 표만들기
# DataFrame 생성하기: 표만들기
import pandas as pd
# 전역변수 
data=[[17,'남','덕영고'],[15,'여','대구중']]
# DataFrame 만들기
dataDF=pd.DataFrame(data)
print(dataDF)

dataDF=pd.DataFrame(data,index=['마징가','원더우먼'],
                    columns=['나이','성별','학교'])
print(dataDF)