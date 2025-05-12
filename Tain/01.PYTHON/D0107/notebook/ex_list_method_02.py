# list 자료형 전용 함수 즉, method
# - 사용: 변수명.method()
# -----------------------------------------------
# - 원소/요소 순서를 뒤집기: reverse()
data=[9,5,-2,0,11]
data.reverse()
print(data)
# - 원소/요소 정렬해주는 method: sort()
data.sort()
print(data)
data.sort(reverse=1)
print(data)
# ----------------------------------------------
# key활용
data=['999','9959','99999','3333']
data.sort(key=len)
print(data)
# -----------------------------------------------
# 원소/요소의 인덱스를 찾아주는 method: index()
# - 존재하지 않으면 ERROR 발생
data=[9,5,-2,0,11,'바보']
print(f'11의 index: {data.index(11)}')
# print(f'7의 index: {data.index(7)}') * not found ERROR

# 원소/요소를 제거해주는 method: remove()
data.remove('바보')
print(data)