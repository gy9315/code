import pandas as pd
# DataFrame에서 행 선택/추출 -> 가로 한줄 선택
## -------------------------------------
# [1] 모듈 로딩
# [2] 데이터 준비
a=r'C:\Users\gy931\OneDrive\Desktop\KDP-7\02.PANDAS\DATA\iris.csv'
irisDF=pd.read_csv(a)
# print(irisDF)
# [3] 데이터 확인, 속성: col,ind,val, dtypes, shape,ndimension
# - 속성읽기: 변수명.속성명
# print(f'risDF.index: {irisDF.index}')
# print(f'irisDF.column: {irisDF.columns}')
# print(f'irisDF.values: {irisDF.values}')
# print(f'irisDF.dtypes: {irisDF.dtypes}')
# print(f'irisDF.shape: {irisDF.shape}')
# print(f'irisDF.ndim: {irisDF.ndim}')
# DataFrame 기본 정보 출력 method: info()
# irisDF.info()
# DataFrame col별 수치형에 대한 통계치 계산 method: desc()
# print(irisDF.describe())
# print(irisDF.describe(include='all'))

# [4] 행 선택/추출 method: loc(), iloc()
# [4-1] 한개의 행 선택
# - 문법: 변수명.loc(행 인덱스명)
#         변수명.iloc(행 인덱스 번호)
print(f'[0번행]\n {irisDF.iloc[0]}\n{type(irisDF.iloc[0])}')
# [4-2] 여러개 행 선택(0,2)
print(f'[0,2번행]\n {irisDF.iloc[[0,2]]}\n{type(irisDF.iloc[[0,2]])}')
# [4-2] 여러개 행 선택(0 ~ 5)
print(f'[0~5번행]\n {irisDF.iloc[:6]}\n{type(irisDF.iloc[:6])}')
# [4-2] 여러개 행 선택(0,2,4)
print(f'[0,2,4번행]\n {irisDF.iloc[:6:2]}\n{type(irisDF.iloc[:6:2])}')
# 행 인덱스 5개 변경
# 0부터 4번행까지 변경
print(f"[0번 ~4번행 변경]\n {irisDF.rename(index={0:'zero',1:'one',3:'three',4:'four',5:'five'})}")
irisDF1=irisDF.rename(index={0:'zero',1:'one',3:'three',4:'four',5:'five'})
print(f'[0번행]\n {irisDF1.iloc[0]}\n{type(irisDF1.iloc[0])}')
print(f"[0번행]\n {irisDF1.loc['zero']}\n{type(irisDF1.loc['zero'])}")