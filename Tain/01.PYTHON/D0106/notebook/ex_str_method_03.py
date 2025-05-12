# str 타입 전용 함수 즉, method
# - 사용법: 변수명.method()
# -------------------------------------------
# [2] 문자열에서 뒷 원소의 index 찾아주는 method: rindex(), rfind()
# - 결과값: 0이상의 인덱스, 없는 경우 not found ERROR 발생/-1
data='Happy 2025!'
# 제일 뒤에서 부터'p' index 찾기
print(f'p의 index: {data.index("p")}, {data.find("p")}')
print(f'p의 index: {data.rindex("p")}, {data.rfind("p")}')