# list 데이터 타입 method
# - 리스트에 원소/요소 추가
# - 문법: list.append('data')
# 빈 리스트 생성 및 원소 추가하기
list=[]
list.append(100)
print(list)
# 원하는 위치에 원소/요소 추가: insert(index,data1)
list.insert(0,[1,2,3])
print(list)
list.insert(1,[4,5,6])
print(list)
list[1].insert(1, 2)
print(list)
# 끝자리에 넣는 방법: append(data1), insert(len(data),data1)
list.insert(len(list),[3,4])
print(list)