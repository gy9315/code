# 문자열 str type 전용 함수 즉, method
# - input() -> 키보드로 입력받기
# - str.split() method: 1개 str -> n개 str
# [예시] 2개의 정수를 입력받아 주세요.
nums=input('숫자 2개 입력: 예) 10, 20')
num=nums.split(',')
print(num)
print(int(num[0])+int(num[1]))
