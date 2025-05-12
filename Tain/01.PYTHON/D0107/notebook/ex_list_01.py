# List 자료형
# - 다양한 종류의 여러 개의 데이터를 저장하는 타입
# - 형식: [data1,data2,...]
# - 원소/요소 식별을 위해서 index와 slicing을 사용함
# ------------------------------------------------
# list 데이터 생성
# - 빈 리스트 생성
data=[]
data1=[1,2,3]
# - 변수를 원소로 저장하는 리스트
data2='2025'
data3='100'
data4='하늘'
datas=[data2,data3,data4] # ['2025'주소, 100의 주소, '하늘'주소]
print(f'data: {type(data)}, 원소개수: {len(data)}')
print(f'data1: {type(data1)}, 원소개수: {len(data1)}')
print(f'data2: {type(data2)}, 원소개수: {len(data2)}')
print(f'data3: {type(data3)}, 원소개수: {len(data3)}')
print(f'data4: {type(data4)}, 원소개수: {len(data4)}')
print(f'datas: {type(datas)}, 원소개수: {len(datas)}')
# - 리스트르 원소로 저장하는 리스트
names=['홍길동','마징가','베트맨']
jobs=['의적','로봇','박쥐']
datas=[names,jobs,100,200,False]
print(f'datas: {type(datas)}, 원소개수: {len(datas)}')