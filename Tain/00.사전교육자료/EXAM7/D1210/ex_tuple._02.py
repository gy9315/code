# tuple type의 수정/삭제/변경 그리고 method
# - read only type: 수정/삭제/변경, 불가
# - method: 읽기관련 method만 존재
# [1] 수정/삭제/변경
number=('053','054','02','032')
# ★★★★★★★★★★
# 053을 53으로 변경
# number[0]=53 * 오류: 지원하지 않음(변경)
# 053을 삭제
# del number[0] * 오류: 지원하지 않음(삭제)
# 추가 관련 method 없음
# [2] method
# - 데이터 갯수 파악: count()
print(number.count('053'))
print(int(number[0])+int(number[1]))
# [3] 형변환
number=list(number)
print(number)
number.insert(2,"031")
print(number)
number=('053','054','02','032')
# 054: 제거, 057변경
number=list(number)
number[0]='057'
del number[1]
number=tuple(number)
print(number)