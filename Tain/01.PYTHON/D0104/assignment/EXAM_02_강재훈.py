# 1
## 자료형: 자료(데이터)를 효과적으로 저장하기 위한 자료를 자료유형별로 구분한 종류
# 2
## 정수(1,2,3)=int()
## 실수(1.1,0.0)=float()
## 문자열('Happy Birthday!')=str()
## 논리형(True,False)=bool()
#
## list([1,2])=list()
## tuple(('',''))=tuple()
# 3 
num=31
print(f'{num}의 2진수는 {bin(num)}')
print(f'{num}의 8진수는 {oct(num)}')
print(f'{num}의 10진수는 {int(num)}')
print(f'{num}의 16진수는 {hex(num)}')
# 4
avg=98.7
avg=int(avg)

year=2022
year=float(year)
greet="Hello~"
greet=bool(greet)
# 5
num=int(input('숫자 1 입력:'))
num1=int(input('숫자 2 입력:'))
print(f'덧셈 {num} + {num1} = {num+num1}')
print(f'뺄셈 {num} - {num1} = {num-num1}')
print(f'곱셈 {num} * {num1} = {num*num1}')
print(f'나눗셈 {num} / {num1} = {num/num1}')
print(f'몫 {num} // {num1} = {num//num1}')
print(f'나머지 {num} % {num1} = {num%num1}')
print(f'제곱근 {num} ** {num1} = {num**num1}')
# 6
num=(input('문자 1개 입력:'))
print(f'{num}코드값: {ord(num)} {num}기계어: {bin(ord(num))}')
num1=(input('문자 1개 입력:'))
print(f'{num1}코드값: {ord(num1)} {num}기계어: {bin(ord(num1))}')