# DataFrame 생성하기: 표만들기
# DataFrame 생성하기: 표만들기
import pandas as pd
# 전역변수 
data=[[17,'남','덕영고'],[15,'여','대구중'],[19,'여','대구고']]
# DataFrame에서 속성 읽기&변경하기

dataDF=pd.DataFrame(data)
print(dataDF)
# DataFrame의 속성읽기
print(f'index: {dataDF.index}')
print(f'column: {dataDF.columns}')
dataDF=pd.DataFrame(data,index=['마징가','원더우먼','홍길동'],
                    columns=['나이','성별','학교'])
print(dataDF)
print(f'index: {dataDF.index}')
print(f'column: {dataDF.columns}')
print(f'values: {dataDF.values}')
print(f'type: {type(dataDF.values)}')
# 속성변경
# - 컬럼명 속성을 영어로 변경
dataDF.columns=['age','gender','school']
print(dataDF)
dataDF.index=['ma','won','hong']
print(dataDF)
# 값 속성 변경이 불가
import numpy as np
print(dataDF)