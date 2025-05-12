# List 자료형
# - 다양한 종류의 여러 개의 데이터를 저장하는 타입
# - 형식: [data1,data2,...]
# - 연산
#   * 덧셈: list+list: 2개 list 원소 합쳐서 새로운 list
#   * 곱셈: list*int: 숫자만큼 list 원소 합쳐서 새로운 list
#   * 멤버연산자: in, not in
data=[1,3,5,7]
data1=['a','b','c','d']
# 덧셈 연산: list 확장
print(f'data + data1 = {data+data1}')
print(f'data1 + data1 = {data1+data1}')
# 곱셉 연산: list 확장
print(f'data * 2 = {data*2}')
# 데이터 in list: 데이터가 list에 존재여부
print(f'1 in data: {1 in data}')
