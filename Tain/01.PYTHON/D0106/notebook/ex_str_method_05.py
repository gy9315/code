# str 타입 전용 함수 즉, method
# - 사용법: 변수명.method()
# -------------------------------------------
# [5] str -> 여러개의 str 분리해주는 method: split()
# - 문법: split('구분자') /split() [기본값: '공백']
# - 표현방식: 문자열을 분리하여 list에 담아서 줌 [str1, str2,...]
data="Happy New Year 2025"
data1='010-1111-2222'
print(f'{data}의 기본값 기준으로 분리: {data.split()}')
print(f'{data1}의 "-"기준으로 분리: {data.split("-")}')
data3='HappyHappyHappy'
print(f'{data1}의 "H"기준으로 분리: {data.split("H")}')
# [실습] 2개의 정수를 입력받아서 덧셈 결과를 출력하세요
data=input('정수 2개를 입력:')
data1='0'
print(str(data))
for data2 in data.split(','):
    data1=int(data1)+int(data2)
print(data1)
data_list=[]
for data3 in (data.split(',')):
    data_list.append(int(data3))
print(sum(data_list))