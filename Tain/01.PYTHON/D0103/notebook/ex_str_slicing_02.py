# 문자열 str 타입 - 슬라이싱(slicing)
# - 전체 문자열에서 일정한 간격으로 연속된 문자열을 일부 추출하는 방버
# - 문법
#   * 변수명[:끝인덱스+1] * 처음부터 끝인덱스
#   * 변수명[시작인덱스:] * 시작인덱스부터 끝까지
#   * 변수명[:] * 처음부터 끝까지지
# - 특징
#   문자 한 개 원소는 2개의 인덱스를 가짐!
# - 원소 개수 파악 내장함수 -> len(데이터)
msg='Life is too short, You need Python'
# 'Life'만 출력
print(msg[:5])
# 'Python'
print(msg[-6:])
# 전체 출력
print(msg)
print(msg[:])