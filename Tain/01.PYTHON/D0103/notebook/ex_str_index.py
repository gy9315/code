# 문자열 str 타입 - 인덱스
# - 인덱스
#   문자열을 구성하는 문자 한 개 한개를 식별을 하기 위한 번호
#   파이썬에서 자동으로 부여함 -> 인덱상
# - 종류
#   * 왼쪽: 0,1,...
#   * 오른쪽: -1, -2, ....
# - 특징
#   문자 한 개 원소는 2개의 인덱스를 가짐!
# - 원소 개수 파악 내장함수 -> len(데이터)
msg='오늘은 좋은 날!!'
#     012 3 45 6 7 89
#     10987 65 4 3 2 1
# 전체 메시지 출력
print(msg, len(msg))
# '날'만 출력 => 변수명[인덱스]
print(msg[-3],msg[7])
# '은'만 출력
print(msg[2], msg[-8])
# '좋'과 '!'출력
print(msg[4], msg[msg.find('!')], msg[msg.find('!')+1])

msg='Happy New Yer 2025! Merry Christmas♥'
# msg
print(msg[msg.find('5')])
print(msg.count('a'))