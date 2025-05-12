# 데이터 타입을 변경해주는 내장함수
# - 타입 캐스팅(casting) / 형변환
#   * 데이터 타입을 변경하는 것
#   * 종류
#     - 암묵적 형번환: 시스템에서 진행
#     - 명시적 형변환: 개발자가 진행
# - 함수: 자료형명()
#         int(), float(), str(), bool()
# -------------------------------------------------
# [3] str 타입으로 형변환하기
# int->str
print(f'-8을 str로 형변환: {str(-8)}')
print(f'7을 str로 형변환: {str(7)}')
print(f'1을 str로 형변환: {str(1)}')
print(f'0을 str로 형변환: {str(0)}')
# float->str
print(f'-8.을 str로 형변환: {str(-8.)}')
print(f'0.0000을 str로 형변환: {str(0.0000)}')
print(f'1.2345을 str로 형변환: {str(1.2345)}')
# bool->str
print(f'True을 str로 형변환: {str(True)}')