# 문자열 str type 전용 함수 즉, method
# [1] 알파벳 대소문자 변환 관련 method
# - 소문자로 변경하는 method lower()
# - 대문자로 변경하는 method upper()
# - 첫문자만 대문자로 변경 capitalize()
# - 소문자인지 검사하는 method islower()
# - 대문자인지 검사하는 method isupper()
# - 알파벳인지 검사하는 method isalpha()
msg='good'
print(f'{msg}를 대문자로: {msg.upper()}')
print(f'{msg}를 첫문자만 대문자로: {msg.capitalize()}')
print(f'{msg}가 소문자 여부: {msg.islower()}')
print(f'{msg}가 대문자 여부: {msg.isupper()}')
print(f'{msg}가 알파벳 여부: {msg.isalpha()}')
msg='좋은날'
print(f'{msg}를 대문자로: {msg.upper()}')
print(f'{msg}를 첫문자만 대문자로: {msg.capitalize()}')
print(f'{msg}가 소문자 여부: {msg.islower()}')
print(f'{msg}가 대문자 여부: {msg.isupper()}')
print(f'{msg}가 알파벳 여부: {msg.isalpha()}')
msg='좋은날1'
print(f'{msg}를 대문자로: {msg.upper()}')
print(f'{msg}를 첫문자만 대문자로: {msg.capitalize()}')
print(f'{msg}가 소문자 여부: {msg.islower()}')
print(f'{msg}가 대문자 여부: {msg.isupper()}')
print(f'{msg}가 알파벳 여부: {msg.isalpha()}')
# 문자열 str type 전용 함수 즉, method
# [2] 특정 문자열로 시작 또는 끝나는 문자열 검사 관련 method
# - 특정 문자열로 시작하는 체크: startswith()
# - 특정 문자열로 끝나는 체크: endswith()
file1='flower.jpg'
file2='flower.png'
# jpg로 끝나는지 검사
print(f'{file1}: {file1.endswith(".jpg")}')
print(f'{file2}: {file2.endswith(".jpg")}')