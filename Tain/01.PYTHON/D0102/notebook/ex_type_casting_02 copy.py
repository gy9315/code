# 데이터 타입을 변경해주는 내장함수
# - 타입 캐스팅(casting) / 형변환
#   * 데이터 타입을 변경하는 것
#   * 종류
#     - 암묵적 형번환: 시스템에서 진행
#     - 명시적 형변환: 개발자가 진행
# - 함수: 자료형명()
#         int(), float(), str(), bool()
# -------------------------------------------------
# [2] 실수 float 타이브로 형변환하기
# int->float
print(f'-8을 float으로 형변환: {float(-8)}')
print(f'7을 float으로 형변환: {float(7)}')
# str->float
print(f'"-8"을 float으로 형변환: {float("-8")}')
print(f'"7"을 float으로 형변환: {float("7")}')
print(f'"7.1"을 float으로 형변환: {float("7.1")}')
print(f'"0b11100"을 float으로 형변환: {float(int("0b11100",base=2))}')
# bool->float
print(f'False를 float으로 형변환: {float(False)}')
