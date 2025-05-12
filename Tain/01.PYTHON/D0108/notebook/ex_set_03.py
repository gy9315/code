# set 자료형 전용 함수 즉, method

#  set 데이터 생성
# 1 ~ 100사이 3의 배수로 구성된 data1
# 1 ~ 100사이 5의 배수로 구성된 data2
data=set(range(5,31,5))
print(data,len(data))
# [4] 원소/요소 1개 추가 mothod: add()
data.add('1000')
print(data,len(data))
data.add('AB')
print(data,len(data))
data.add('Fasle')
data.add(1)
print(data,len(data))
# [5] 원소/요소 여러개 추가 mothod: update(), 변경가능한 list & dict
data.update(['a','b','b','c'])
print(data,len(data))
data.update(['a','b','b',(111,222)])
print(data,len(data))
# [6] 원소/요소 여러개 추가 mothod: update(), 변경가능한 list & dict
data.update(['a','b','b','c'])
# [7] 원소/요소 꺼내기 즉, 삭제 method: pop()
print(data.pop())
print(data,len(data))
print(data.pop())
print(data,len(data))
print(data.pop())
print(data,len(data))
# [8] 원소/요소 삭제하기 method: remove()
data.remove(30)
print(data,len(data))
## - 모든 원소 삭제
data.clear()
print(data, len(data))