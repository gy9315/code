# input() 함수와 casting 함수를 이용한 계산 구현
#-----------------------------------------------
# [1] 2개의 정수를 입력 받기 -> input() 
num1=input('정수 입력:')
num2=input('정수 입력:')

# [2] 입력받은 데이터 확인
print('num1 타입', type(num1))
print('num2 타입', type(num2))

# [3] str-> int cast
num1=int(num1)
num2=int(num2)

print('num1 타입', type(num1))
print('num2 타입', type(num2))

# [4] 계산하기
print('덧셈', num1+ num2)
print('뺄셈', num1+ num2)
print('곱셈', num1*num2)
print('나눗셈', num1/ num2)
