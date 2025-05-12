# 객체(object)
# -  힙 메모리 영역에 저장된 데이터들을 통칭하는 용어
# - int, float, str, bool, ... type
# ------------------------------------------------
# 비교연산자: 데이터의 타입 비교 X, 순수 값만을 비교
num=10 # int type 인스턴스
num1=10.0 # float type 인스턴스
print(f'{num}=={num1}: {num==num1}')
print(f'{num}>{num1}: {num>num1}')
# 객체 비교연산자: 데이터의 타입 비교
# - A is B: A와 B가 같다
# - A is B: A와 B가 다르다
num=10
num1=10.0
num2=11
num3=10
print(f'{num} is {num1}: {num is num1}')
print(f'{num} is {num2}: {num is num2}')
print(f'{num} is {num3}: {num is num3}')
print(id(num))
print(id(num3))