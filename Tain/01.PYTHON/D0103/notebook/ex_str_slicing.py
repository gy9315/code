# 문자열 str 타입 - 슬라이싱(slicing)
# - 전체 문자열에서 일정한 간격으로 연속된 문자열을 일부 추출하는 방버
# - 문법: 변수명[시작인덱스:끝인덱스+1]
# - 특징
#   문자 한 개 원소는 2개의 인덱스를 가짐!
# - 원소 개수 파악 내장함수 -> len(데이터)
msg='Happy New Year 2025! Merry Christmas♥'
# 전체 출력
print(msg)
# 'Happy'만 출력
print(msg[0],msg[1],msg[2],msg[3],msg[4],sep='')
# 0이상 5미만(0<='Happy'<5)
print(msg[:5],msg[:4])
# 2025!만 출력
print(msg.find('2'))
print(msg[15:20])
print(msg[msg.find('2'):msg.find('2')+5])
# 'Christmas'만 출력
print(msg[-10:-1])
