# set 자료형 살펴보기
# - 특징: 중복 데이터 저장 불가! 순서 없음
# - 형식: {data1, data2, ...}
#         {} <- 빈 dict, set() <- 빈 set
# [1] set 데이터 생성
data1={1,1,2,2,3,4,5,5,8}
data2={'A',100,False,'a',100,100,'a',False}
# data3={'홍길동',[10,20,30],False} -> unhashable type ERROR
data3={'홍길동',(10,20,30),False}
data4={}
data5=set()
print(f'{data1}, type: {type(data1)}')
print(f'{data2}, type: {type(data1)}')
print(f'{data3}, type: {type(data3)}')
print(f'{data4}, type: {type(data4)}')
print(f'{data5}, type: {type(data5)}')


