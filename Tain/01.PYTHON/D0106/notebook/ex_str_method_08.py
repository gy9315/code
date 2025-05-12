# str 타입 전용 함수 즉, method
# - 사용법: 변수명.method()
# -------------------------------------------
# [8] str을 특정 조건에 변경해주는 method:
# - 문법: 대문자(upper), 소문자(lower), 첫 글자 대문자(capitalize)
data='Good luck'
print(f'{data}를 대문자로 변경: {data.upper()}')
print(f'{data}를 소문자로 변경: {data.lower()}')
print(f'{data}에 첫 글자를 대문자로 변경: {data.capitalize()}')