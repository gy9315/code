# 내장함수 len()
# - 데이터를 구성하는 원소 갯수를 알려주는 함수
# - int, float, bool 사용불가
# - 여러개의 데이터로 구성된 데이터집합
#   예) str1, str2, str3
# - 특징: 요소 갯수를 알면 인덱스 범위를 알 수 있음
#       * 2개-> 0,1
#       * n개-> 0,1,...,n-1
data1=2025 # int
data2=9.998 # float
data3=True # bool
data4='' # empty string
# 기본데이터 타입인 int, float, bool은 1개의 데이터를 저장
# 원소/요소가 없음 -> len() 사용 불가
print(f'{data4}의 원소 개수: {len(data4)}')
# 기본 데이터 타입 중 str에서 사용
data4='ab'
print(f'{data4}의 원소 개수: {len(data4)}')
print(data4[0], data4[1])
