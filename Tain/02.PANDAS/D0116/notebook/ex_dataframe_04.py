# 행 인덱스&열 이름 일부 변경하기
# - method: rename()
import pandas as pd
# 데이터 준비
data=[[15,'여','대구중'],[19,'여','대구고']]
# 데이터 프레임 생성
dataDF=pd.DataFrame(data)
print(dataDF.index)
print(dataDF.columns)
# 인덱스,컬럼즈 설정
dataDF.index=['학생1','학생2']
dataDF.columns=['연령','성별','학교']
print(dataDF)
# dataDF.values[0,0]=20
# print(dataDF)

# # 변경
# dataDF2=dataDF.rename(index={'학생1':'학생01'})
# print(dataDF2)
# dataDF3=dataDF.rename(columns={'연령':'나이'},inplace=1)
# print(dataDF)
print(dataDF.rename({'연령':'나이'},axis=1))
print(dataDF.index[0])