# 데이터의 종류 즉, 타입 변환하기
# -> 형 변환 / 타입 캐스팅
# -> 내장함수
#    int(데이터), int(변수명) / 정수변환
#    float(데이터), ...       / 실수변환
# -> 현재 데이터의 타입을 알려주는 함수: type(데이터)
# ----------------------------------------------------
# 데이터의 타입 확인하기
# --------------------------------------------------
print(type(3.4), type('a'),type('apple'),type(-1))
print(type(1), type('1'))
print(type(True))
age=100
name='홍길동'
print(type('age'), type('name'))
# ----------------------------------------------------
# 데이터의 종류/타입 변경하기
# ----------------------------------------------------
# [1] 정수의 타입 변경
num=100
print(type(num))
print(float(num)) # 원래 데이터의 영구적 변경이 아님
print(num)
num=float(num) # 형 변환된 데이터의 주소가 저장됨
print(type(num))
name=10
print(type(name))
name=print(float(name))
print(type(name))
# ----------------------------------------------------
# 함수의 결과값
value=sum([10,20])
print(value)
value2=print('A')
print(value2)
