# 지역(local)변수와 전역(Global)변수
# - 지역(local) 변수: 함수에서 사용되는 변수들
# - 전역(Global) 변수: 파일(py)에서 사용되는 변수들
# -------------------------------------------------
# 전역변수, 해당파일 모든 곳에서 사용 가능한 변수
name='홍'

def printData():
    name='마징가'
    year=2025 # 지역변수로 함수 안에서만 사용가능
    print(name,year)
def changeData():
    global name # 전역변수 name을 사용 선언 = 전역변수 변경이 가능
    name='이순신'
    year=2025 # 지역변수로 함수 안에서만 사용가능
    print(name,year)
print(f'나의 이름은 {name}!!!')
# print(f'올해는 {year}!!!')

printData()
changeData()
print(name)