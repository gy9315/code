# # [실습] 연산자 & 형 변환 & 내장함수 실습
# # ------------------------------------------------
# # [1] 2개 숫자 데이터 입력 받아서 그 중 큰 숫자를 출력하세요.
# #  - 출력형태: -5와 8중 큰 숫자는 8입니다.
# num=int(input('숫자를 입력하세요:'))
# num1=int(input('숫자를 입력하세요:'))
# print(f'{num}와 {num1} 중 큰 숫자는 {max(num, num1)}')
# # [1] 2개 숫자 데이터 입력 받아서 거듭 제곱값을 출력하세요.
# #  - 출력형태: 8의 3승은 512입니다.
# num=int(input('숫자를 입력하세요:'))
# num1=int(input('숫자를 입력하세요:'))
# print(f'{num}의 {num1}승은 {pow(num, num1)}')
# # [3] 숫자 데이터를 입력 받은 후 숫자 데이터 여부 검사 출력 
# #  - 그 숫자의 2진수, 8진수, 16진수를 출력하세요.
# #  - 출력형태: 3은 숫자 데이터 입니다. 3의 2진수 ob11
num=int(input('숫자를 입력하세요:'))
is_num=num>=0 and num<=9
print(f'{num}은 숫자 데이터입니다.{is_num}')
print(f'{num}의 2진수는 {bin(num)}')
print(f'{num}의 8진수는 {oct(num)}')
print(f'{num}의 16진수는 {hex(num)}')