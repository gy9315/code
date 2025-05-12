# # list 데이터 type 특징
# - 다양한 데이터를 여러개 저장하는 타입
# [1] 원소/요소의 값 변경
data=['2024-12-09',2025,True,'Happy']
# 2025를 1000으로 변경 *replace를 쓰는게 아닌 그냥 값변경으로 변경가능
data[1]=1000
print(f'data 요소 2025를 1000으로 변경:{data}')
# [2] 원소/요소의 값 삭제
# 명령어: del * 함수 X, method X
# 형식: del 삭제데이터, del(삭제데이터)
# 2024-12-09삭제
del data[0]
del(data[0])
print(data)
