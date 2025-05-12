# 논리 연산자
# - 여러개의 조건들을 비교 평가하는 연산자
# - 결과 => T or F
# - 형식
# -- 모든 조건이 T여야만 하는 경우 ex) * and * and * and ...
# -- 일부조건/1개 이상의 조건이 T여야만 하는 경우 ex) * or * or * ...
# -- 현재 결과의 반대 ex) not a(T)=F, not a(F)=T
# [1] 청소년 9세 이상 24세 미만
age=int(input('나이 입력:'))
print(age>=9 and age<24)

# [2] 미취학 아동 8세 미만
age=int(input('나이 입력:'))
print(age<8)
# [3] 나이와 성별 입력 받아서 검사
age=int(input('나이 입력:'))
sex=input('성별 입력\n[남/여]:')
# - 20세 이상이고 여성인 경우
print(age>=20 and sex=='여')
# - 20세 이상이거나 여자인 경우
print(age>=20 or sex=='여')
# [4] 입력받은 데이터가 알파벳인지 판별
# a,b,c,d,... / A,B,C, ....
print(f'a > b 비교: {"a">"b"}') 
print(f'a > A 비교: {"a">"A"}') 
data=input('알파벳을 입력하세요:')
# 소문자 검사
print(f'data 소문자 여부: {data >="a" and data <="z"}')
# 대문자 검사
print(f'data 소문자 여부: {data >="A" and data <="Z"}')
# 알파벳 검사
print(f'data 소문자 여부: {data >="a" and data <="z"}' or '{data >="A" and data <="Z"}')
# [5] 결과를 반대로 만들어주는 논리연산쟈
# - 숫자(0~9)만 입력하기
num=input('숫자만 입력:')
# - 비교연산자 활용 변수 정하기
is_num=(num>='0' and num<='9')
print(f'{is_num}')
print(f"숫자입력 여부 체크: {num} {num>='0' and num<='9'}")
# - 숫자를 제외한 문자 입력
num=input('숫자를 제외한 문자입력 여부:')
is_num1=(num>='0' and num<='9')
print(f"숫자를 제외 입력 여부 체크: {num} {num<'0' or num>'9'}")
print(f"숫자를 제외 입력 여부 체크: {num} {not is_num1}")