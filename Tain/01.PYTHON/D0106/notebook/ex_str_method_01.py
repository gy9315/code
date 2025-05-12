# str 타입 전용 함수 즉, method
# - 사용법: 변수명.method()
# -------------------------------------------
# [1] 문자열에서 원소의 index 찾아주는 method: index()
# - 결과값: 0이상의 인덱스, 없는 경우 not found ERROR 발생
data='Happy 2025!'
# 'y' 원소의 index 찾기
print(f'Y의 index: {data.index("y")}')
# '5' 원소의 index 찾기
print(f'Y의 index: {data.index("5")}')
# 'y' 원소의 index 찾기
print(f'Y의 index: {data.index("25")}')
# '  ' 원소의 index 찾기 -> 없는 경우 ERROR 발생
# print(f'  의 index: {data.index("  ")}')
# --------------------------------------------
# [2] 문자열에서 원소의 index 찾아주는 method: find()
# - 결과값: 0이상의 인덱스, 없는 경우: -1
print(f'Y의 index: {data.find("y")}')
# '5' 원소의 index 찾기
print(f'Y의 index: {data.find("5")}')
# 'y' 원소의 index 찾기
print(f'Y의 index: {data.find("25")}')
# '  ' 원소의 index 찾기, 없는 경우 -1 반환
print(f'  의 index: {data.find("  ")}')