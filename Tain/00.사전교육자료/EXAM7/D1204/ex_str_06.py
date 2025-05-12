# 문자열 str type 연산 -> 산술연산가
# - 덧셈, 곱셈(뺄셈, 나눗셈 지원불가)
# --------------------------
m1='happy'
m2='2025'
# 산술연산
print(f'{m1}+{m2}={m1+m2} ')
print(f'{m1}+{str(5)}={"5"+m1}') # str+int X, str+str or int+int만 가능
# print(f'{m1}-{m2}={m1-m2} ')  # (-) str type에서 지원하지 않는 연산
print(f'{m1}*5, happy happy happy happy happy={m1*5} ')
print(f'1*5={1*5} ')
# print(f'{m1}*{m2}={m1*m2} ')  # str * str은 오류/str*int or int*int만 가능 
# --------------------------
# str type 산술연산 활용
data='pithon'
data=data[0]+'y'+data[2:]
print(data)
