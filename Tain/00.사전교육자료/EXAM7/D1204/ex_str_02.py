# 문자열 str type 다루기
# - 문자열에서 일부 문자 또는 문자열 추출
# - 방법: indexing 방법
#         문자(원소) 1개에 번호를 붙임(단, 0부터 시작: zero counting)
# - 원소일기: 변수명[번호]
# [예시] merry christmas! happy new year 2025!
msg="Merry Christmas! Happy New Year 2025!"
#    0          1         2         3     (양수 index)
#    0123456789012345678901234567890123456(양수 index)
#    -                                  -- (음수 index)
#    37                                 21 (음수 index)
print(msg)
# [일부문자열을 추출하기-원소 추출]
# (1) c문자만 추출
print(f'msg의 6번째 원소: {msg[6]}')
# (2) 앞부분의 !문자만 추출
print(f'msg의 15번째 원소: {msg[15]}')
# (3) 마지막 부분의 !문자만 추출
print(f'msg의 36번째 원소: {msg[36]}')
print(f'msg의 36번째 원소: {msg[-1]}')
# (4) 첫번째 부분의 M문자만 추출
print(f'msg의 0번째 원소: {msg[0]}')
print(f'msg의 -37번째 원소: {msg[-37]}')
num=input('숫자를 입력하세요:')
# [퀴즈] ''사이에 공간이 없지만 str로 보고 원소에 번호 부여 불가에 따른 indexing 불가
msg=''
print(type(msg))
