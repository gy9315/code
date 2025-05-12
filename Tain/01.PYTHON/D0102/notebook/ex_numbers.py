# 숫자의 다양한 표현법
# - 2진수: 0b1
# - 8진수: 0o1
# - 10진수: 1
# - 16진수: 0x1

# 정수 -> 2진수로 변환해주는 내장함수 bin()
num=100
print(bin(num))
bin_num=bin(num)
print(f'{num}의 2진수 표현: {bin_num}')
# 정수 -> 8진수로 변환해주는 내장함수 oct()
oct_num=oct(num)
print(f'{num}의 8진수 표현: {oct_num}')
# 정수 -> 16진수로 변환해주는 내장함수 oct()
hex_num=hex(num)
print(f'{num}의 16진수 표현: {hex_num}')

# 사람문자 <-> 컴퓨터/기계 문자
# 사람 -> 기계어: 인코딩(encoding)
# 기계 -> 사람: 디코딩(decoding)
data='?'
# 사람문자 -> 기계어 변환 내장함수: ord()
# ord= ordinary position
ord_data=ord(data)
print(f'{data}의 코드값: {ord_data}, {bin(ord_data)}')
# 'hello' -> 기계어로 변환
# print(ord(hello)) -> 오류(문자 한개만 가능)
print('hello 코드값:',end=' ')
print(bin(ord('h')),bin(ord('e')),bin(ord('l')),bin(ord('l')),bin(ord('o')))
# 사람문자 -> 기계어 변환 내장함수: chr()
# chr=charater
print(chr(63))