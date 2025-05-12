# - 문자열에서 일부 문자 또는 문자열 추출
# [1] 여러개의 원소 읽기
# - 방법: indexing 방법
msg="Happy New Year!"
# - New만 출력하기
print(msg[6], msg[7], msg[8], sep='')
# - New year!만 출력하기
print(msg[6], msg[7], msg[8],msg[9], msg[10], msg[11], msg[12], msg[13],msg[14],sep='')
# - 방법: slicing: 변수명[indexing 시작번호:끝번호+1] ★ 단, 시작번호 이상 끝번호 미만
print(msg[6:15])
# [2] 문자의 부분만 읽기 즉, slicing
msg="Merry Christmas^^ Happy 2025!!"
# happy만 출력하기
print(msg[-12:-7])
# christms^^ 출력하기
print(msg[6:17])
# 특별하면서 간편한 슬라이싱
msg='Good luck~♥'
#    012345678901234567890123456789012345
# Good부분만 출력하기
# 변수명[emptyspace:#] 0부터 #+1까지의 원소 추출
print(msg[0:4], msg[:4])
# 변수명[#:emptyspace] #부터 끝까지의 원소 추출
print(msg[5:11],msg[5:])
# slicing활용 전부 출력
print(msg[:])