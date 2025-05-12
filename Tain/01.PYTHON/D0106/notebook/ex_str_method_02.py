# str 타입 전용 함수 즉, method
# - 사용법: 변수명.method()
# -------------------------------------------
# [1] 문자열에서 원소의 index 찾아주는 method: index(), find()
# - 결과값: 0이상의 인덱스, 없는 경우 not found ERROR 발생
data='Happy 2025!'
# 'p' index 찾기
print(f'p의 index: {data.index("p")}, {data.find("p")}')
# 두번째 'p' index 찾기
print(f'p의 index: {data.index("p",data.index("p")+1)}, {data.find("p",data.index("p")+1)}')
# 여러개의 동일 문자 index 찾기
data='Good Good Good'
data_index=data.find('G')
print(f'첫번째 "G"의 index: {data_index}')
data_index=data.find("G",data_index+1)
print(f'두번째 "G"의 index: {data_index}')
data_index=data.find("G",data_index+1)
print(f'두번째 "G"의 index: {data_index}')
data='Good Good Good'
data_find=data.find('G')
print(data_find)
for s in range(data.count('G')):
# 첫번째 찾고
    data_find=s
    data_find=data.find('G',int(data_find)+1)
# 두번째째 찾고
    print(data_find)
