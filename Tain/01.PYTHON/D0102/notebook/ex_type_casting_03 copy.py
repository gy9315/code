# 데이터 타입을 변경해주는 내장함수
# - 타입 캐스팅(casting) / 형변환
#   * 데이터 타입을 변경하는 것
#   * 종류
#     - 암묵적 형번환: 시스템에서 진행
#     - 명시적 형변환: 개발자가 진행
# - 함수: 자료형명()
#         int(), float(), str(), bool()
# -------------------------------------------------
# [3] bool 타입으으로 형변환하기
# int->bool
print(f'-8을 bool로 형변환: {bool(-8)}')
print(f'7을 bool로 형변환: {bool(7)}')
print(f'1을 bool로 형변환: {bool(1)}')
print(f'0을 bool로 형변환: {bool(0)}')
# float->bool
print(f'-8.1을 bool로 형변환: {bool(-8.1)}')
print(f'0.0000을 bool로 형변환: {bool(0.0000)}')
# str->bool: "데이터" 데이터가 아무것도 없으면 False, 데이터가 있으면 True
# - "",'': empty string 
# - " ",' ': whitespace string 
print(f'"ABC"을 bool로 형변환: {bool("ABC")}')
print(f'""을 bool로 형변환: {bool("")}')
print(f'" "을 bool로 형변환: {bool(" ")}')

