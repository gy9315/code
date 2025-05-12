# 연산자(Operator) - 산술연산자
# - 뎃셈(+), 뺄셈(-), 나눗셈(/), 곱셈(*), 몫(//), 나머지(%), 제곱근(**)
# int 타입 산술연산자
num1=7
num2=5
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2}')
print(f'몫: {num1}//{num2}={num1//num2}')
print(f'나머지: {num1}%{num2}={num1%num2}')
print(f'제곱근: {num1}**{num2}={num1**num2}')
# -------------------------------------------------------------------
# str 타입 산술연산자
num1='a'
num2='b'
print(f'덧셈: 문자열 연결 {num1}+{num2}={num1+num2}')
# 미지원: print(f'{num1}-{num2}={num1-num2}')
# 미지원: print(f'{num1}*{num2}={num1*num2}')
print(f'곱셈: 문자열 정수만큼 반복 {num1}*{3}={num1*3}')
# 미지원: print(f'{num1}/{num2}={num1/num2}')
# 미지원: print(f'몫: {num1}//{num2}={num1//num2}')
# 미지원: print(f'나머지: {num1}%{num2}={num1%num2}')
# 미지원: print(f'제곱근: {num1}**{num2}={num1**num2}')

# [실습]
print('Happy'+'New'+"Year"+'2025')
print('Happy'*5)

# bool 타입 산술연산자
num1=True
num2=False
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
# 오류: print(f'{num1}/{num2}={num1/num2}')
# 오류: print(f'몫: {num1}//{num2}={num1//num2}')
# 오류: print(f'나머지: {num1}%{num2}={num1%num2}')
print(f'제곱근: {num1}**{num2}={num1**num2}')