# 행&열 삭제
# - method: drop()
#   * (행,열) 구조임 / axis=0 행, axis=1 열
#   * inplace=0 새로운 DF return, inplace=1은 원본 수정
import pandas as pd
# 데이터 준비
data=[[15,'여','대구중'],[19,'여','대구고'],[13,'남','남주'],[19,'여','경신고']]
# 데이터 프레임 생성
dataDF=pd.DataFrame(data)
print(dataDF.index)
print(dataDF.columns)

# 행 삭제
# 0번행 삭제, 원본변경 X
dataDF1=dataDF.drop(0)
print(f'0번행 삭제\n {dataDF1}')
# 0번행,3번행 삭제, 원본변경 X
dataDF2=dataDF.drop([0,3])
print(f'0,3번번행 삭제\n {dataDF2}')
# 열 삭제 
# - 0열삭제, 단 원본 변경X
dataDF1=dataDF.drop(0,axis=1)
print(f'0번열열 삭제\n {dataDF1}')
# - 0,2열열 삭제
dataDF.drop([0,2],axis=1,inplace=True)
print(f'0,2번열 삭제\n {dataDF}')
# 연령, 학교 컬럼 삭제 => [컬럼1, 컬럼2,...]
