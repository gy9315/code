# 제어문-조건문(특별한 조건문: 조건부표현식)
# - 형식: 참일때 실행문 if 조건식 else 거짓을때 실행문문
# - 다른언어: 삼항연산자
# [1] 숫자가 짝수인지 홀수인지 출력하기
num=-1
if num%2:
    print(f'{num}는 홀수')
else:
    print(f'{num}는 짝수')
# 조건부표현식   
print(f'{num}는 홀수')if num%2 else print(f'{num}는 짝수')
result='홀수' if num%2 else '짝수'
print(f'{num}은 {result}')   
# [2] 숫자가 양수, 0, 음수인지 출력하기
if num>0:
    print(f'{num}는 양수')
elif num<0:
    print(f'{num}는 음수')
else:
    print(f'{num}는 0')
result='양수' if num>0 else '음수' if num<0 else 0 
print(f'{num}은 {result}')
num='1'
num2='2'
print(num+num2)