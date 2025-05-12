# set 자료형 전용 함수 즉, method

#  set 데이터 생성
# 1 ~ 100사이 3의 배수로 구성된 data1
# 1 ~ 100사이 5의 배수로 구성된 data2
data1=set(range(3,101,3))
data2=set(range(5,101,5))
print(data1, len(data1))
print(data2, len(data2))

# [1] 2개의 집합에 모든 원소를 합치기: 변수명.union(변수명)
result=list(data1.union(data2))
result.sort()
print(result, len(result))
print(data1|data2)
# [2] 2개의 집합에 공통 원소를 합치기: 변수명.intersection(변수명)
result=list(data1.intersection(data2))
result.sort()
print(result, len(result))
print(data1&data2)
# [3] 1개의 집합에만 있는 원소 추출: 변수명.difference(변수명)
result=list(data1.difference(data2))
result.sort()
print(result, len(result))
print(data1-data2)