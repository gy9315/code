# 행&열 삭제
# - method: drop()
#   * (행,열) 구조임 / axis=0 행, axis=1 열
#   * inplace=0 새로운 DF return, inplace=1은 원본 수정
import pandas as pd
# 데이터 준비
data=[[15,'여','대구중'],[19,'여','대구고'],[13,'남','남주'],[19,'여','경신고']]
# 데이터 프레임 생성
dataDF=pd.DataFrame(data)
# print(dataDF.index)
# print(dataDF.columns)
# 인덱스,컬럼즈 설정
dataDF.index=['학생1','학생2','학생3','학생4']
dataDF.columns=['연령','성별','학교']
# 행 삭제
# - '학생1' 삭제
dataDF1=dataDF.drop('학생1',axis=0)
print(dataDF1)

# 열 삭제 
dataDF1=dataDF.drop('성별',axis=True)
print(dataDF1)
# 연령, 학교 컬럼 삭제 => [컬럼1, 컬럼2,...]
dataDF1=dataDF.drop(['연령','학교'],axis=True)
print(dataDF1)
print(dict(dataDF1))