# 연산자(Operator) - 객체비교연산자
# - 객체: 메모리 힙 영역에 존재하는 데이터
# - is 연산자: A is B, A와 B와 같은 객체면 True
# - is not 연산자: A is not B, A와 B가 같은 객체가 아니면 True
a=10
b=10.
c=a
print(f'{a}의 type은: {type(a)}')
print(f'{b}의 type은: {type(b)}')
print(f'{c}의 type은: {type(c)}')
print(f'{a}의 저장주소는: {id(a)}')
print(f'{b}의 저장주소는: {id(b)}')
print(f'{c}의 저장주소는: {id(c)}')
# ----------------------------------------------------------
# 비교하기: ==연산자는 값 비교
print(f'{a}와 {b} 같은가?: {a == b}')
print(f'{a}와 {c} 같은가?: {a == c}')
# 비교하기: is 연산자는 메모리 상의 객체체 비교
print(f'{a}와 {b} 동일 객체인가?: {a is b}')
print(f'{a}와 {c} 동일 객체인가?: {a is c}')