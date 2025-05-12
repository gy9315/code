# str 타입 전용 함수 즉, method
# - 사용법: 변수명.method()
# -------------------------------------------
# [7] str을 구성하는 알파벳관련 검사: 대문자, 소문자, 첫글자 대문자.....
# - 결과: True/False
data='Happy New Year'
data1=' '
# 모든 문자가 대문자인지여부 method: isupper()
print(f'{data}의 모든 문자가 대문자인가? {data.isupper()}')
print(f'{data}의 모든 문자가 소문자인가? {data.islower()}')
print(f'{data}의 첫 글자가 대문자인가? {data.istitle()}')
print(f'"{data1}"의 공백이 있는가? {data1.isspace()}')

# [실습] 정수를 입력하세요. 나이를 입력하세요
num=input('정수를 입력하세요:')
print('숫자와 알파벳으로 구성?',num.isalnum())
print('공백이 아닙니까?',not num.isspace())