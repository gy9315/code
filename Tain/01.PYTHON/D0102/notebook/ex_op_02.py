# 연산자(Operator) - 비교연산자자
# - 왼쪽 > 오른쪽 : 크다
# - 왼쪽 < 오른쪽 : 작다
# - 왼쪽 >= 오른쪽 : 크거나 같다
# - 왼쪽 <= 오른쪽 : 작거나 같다
# - 왼쪽 == 오른쪽 : 같다
# - 왼쪽 != 오른쪽 : 같지않다

# int 타입 비교연산자자
num1=7
num2=5
print(f'{num1}>{num2}={num1>num2}')
print(f'{num1}<{num2}={num1<num2}')
print(f'{num1}>={num2}={num1>=num2}')
print(f'{num1}<={num2}={num1<=num2}')
print(f'{num1}=={num2}={num1==num2}')
print(f'{num1}!={num2}={num1!=num2}')

# str 타입 비교연산자: 문자의 코드값으로 비교함
num1='A'
num2='B'
print(ord(num1))
print(ord(num2))
print(f'{num1}>{num2}={num1>num2}')
print(f'{num1}<{num2}={num1<num2}')
print(f'{num1}>={num2}={num1>=num2}')
print(f'{num1}<={num2}={num1<=num2}')
print(f'{num1}=={num2}={num1==num2}')
print(f'{num1}!={num2}={num1!=num2}')

# bool 타입 비교연산자: 문자의 코드값으로 비교함
num1=True
num2=False
print(f'{num1}>{num2}={num1>num2}')
print(f'{num1}<{num2}={num1<num2}')
print(f'{num1}>={num2}={num1>=num2}')
print(f'{num1}<={num2}={num1<=num2}')
print(f'{num1}=={num2}={num1==num2}')
print(f'{num1}!={num2}={num1!=num2}')