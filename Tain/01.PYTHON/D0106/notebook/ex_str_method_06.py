# str 타입 전용 함수 즉, method
# - 사용법: 변수명.method()
# -------------------------------------------
# [6] str을 구성하는 문자의 종류 즉, 숫자/알파벳/기호문자/... 검사
# - method: isaplha(), isdigit()
# - 결과: True/False
data1='0123456789'
data2='010-1111-2222'
data3='0.0001'
data4='½'
data5='3²'
data6='-4'
data7='1.4'
# isdigit(): 오직 0 ~ 9 숫자 체크
## isdecimal < isdigit:제곱근 < isnumeric: 제곱급, 분수수
print(f'{data1}은 is digit?:{data1.isdigit()} ')
print(f'{data2}은 is digit?:{data2.isdigit()} ')
print(f'{data3}은 is digit?:{data3.isdigit()} ')
# -------------------------------------------------
print(f'{data1}은 is digit?:{data3.isnumeric()} ')
print(f'{data1}은 is digit?:{data3.isdecimal()} ')
# -------------------------------------------------
print(f'{data4}은 is digit?:{data4.isdigit()} ')
print(f'{data4}은 is numeric?:{data4.isnumeric()} ')
print(f'{data4}은 is decimal?:{data4.isdecimal()} \n')
# ------------------------------------------------
print(f'{data5}은 is digit?:{data5.isdigit()} ')
print(f'{data5}은 is numeric?:{data5.isnumeric()} ')
print(f'{data5}은 is decimal?:{data5.isdecimal()} \n')
# ------------------------------------------------
print(f'{data6}은 is digit?:{data6.isdigit()} ')
print(f'{data6}은 is numeric?:{data6.isnumeric()} ')
print(f'{data6}은 is decimal?:{data6.isdecimal()} \n')
# ------------------------------------------------
print(f'{data7}은 is digit?:{data7.isdigit()} ')
print(f'{data7}은 is numeric?:{data7.isnumeric()} ')
print(f'{data7}은 is decimal?:{data7.isdecimal()} \n')
# ------------------------------------------------
# isalpha(): 알파벳, 자음 모음으로 만 이루어진 str체크
## 기호(?,!,..) whitespace string X
data1='Happy'
data2='월요일'
data3='0106오늘늘'
print(f'{data1}은 is alpha?:{data1.isalpha()} ')
print(f'{data2}은 is alpha?:{data2.isalpha()} ')
print(f'{data3}은 is alpha?:{data3.isalpha()} ')

# isalnum(): 글자와 숫자만으로 구성되어있는지 체크
data1='Happy 2025'
data2='Happy2025'
data3='0106오늘'
print(f'{data1}은 is alnum?:{data1.isalnum()} ')
print(f'{data2}은 is alnum?:{data2.isalnum()} ')
