# str 타입 전용 함수 즉, method
# - 사용법: 변수명.method()
# -------------------------------------------
# [10] 여러개 문자열을 특정 문자로 연결해서 1개의 문자열 생성 method:
# - 문법: join()
data='Happy New Year'
data=data.split()
print(data)
# *를 str 사이에 넣어서 연결 후 저장
data=''.join(data)
print(data)
# [실습습]
str_1='a:b:c:d'
print(str_1[::2])
# ------------------------------------
str_2=''
for data in str_1.split(':'):
    str_2=str_2+data
print(str_2)
# ------------------------------------
print(''.join(str_1.split(':')))