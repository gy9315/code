# [문제1]
# 정수 2개를 입력 받은 후 7가지 산술연산 결과 출력
# - 출력형태: 9 + 3 = 12, 0b1100, 0o14,0xC
num1=int(input('숫자를 입력하시오:'))
num2=int(input('숫자를 입력하시오:'))
num=num1+num2
print(f'{num1}+{num2}={num1+num2}, {bin(num1+num2)},{oct(num1+num2)},{hex(num1+num2)}')
print(f'{num1}-{num2}={num1-num2}, {bin(num1-num2)},{oct(num1-num2)},{hex(num1-num2)}')
print(f'{num1}*{num2}={num1*num2}, {bin(num1*num2)},{oct(num1*num2)},{hex(num1*num2)}')
num=num1/num2
print(f'{num1}/{num2}={num}, {bin(int(num))},{oct(int((num)))},{hex(int(num))}')
num=num1//num2
print(f'{num1}//{num2}={num}, {bin(num)},{oct(num)},{hex(num)}')
num=num1%num2
print(f'{num1}%{num2}={num}, {bin(num)},{oct(num)},{hex(num)}')
num=num1**num2
print(f'{num1}**{num2}={num}, {bin(num)},{oct(num)},{hex(num)}')
# [문제2]
# 3개 단어 입력 받은 후 큰 단어, 작은 단어 출력
# - 출력형태: 'ab', 'abc', 'aba' => 큰 문자열 'abc'
num=input('단어1를 입력해주세요:')
num1=input('단어2를 입력해주세요:')
num2=input('단어3를 입력해주세요:')
print(f'{num},{num1},{num2} => 큰 문자열 {max(num, num1, num2)}')
print(f'{num},{num1},{num2} => 작은 문자열 {min(num, num1, num2)}')