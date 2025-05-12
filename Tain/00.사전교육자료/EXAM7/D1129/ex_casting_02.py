# 데이터 형 변환 즉, 타입 캐스팅
# ---------------------------------------
# [1] 정수를 다른 데이터 타입으로 변환하기
num=0

print('int -> float', float(num))
print('int -> str', str(num))
print('int -> bool', bool(num))
# [2] 실수를 다른 데이터 타입으로 변환하기
num=-0.8

print('float -> int', int(num))
print('float -> str', str(num))
print('float -> bool', bool(num))
# [3] 문자를 다른 데이터 타입으로 변환하기
msg='4'

print('str -> int', int(msg))
print('str -> float', float(msg))
print('str -> bool', bool(msg))

msg='0'

print('str -> int', int(msg))
print('str -> float', float(msg))
print('str -> bool', bool(msg))

# str -> bool 변환시 '' 아무것도 없으면 False
#                    '' 있다면 True
msg=''   # 빈문자, empty string
msg2=' ' # 공백문자, whitespace
print('str -> bool', bool(msg))
print('str -> bool', bool(msg2))

msg='0'
msg2='00' # str, 소주점 아래는 정수 변환 불가
print('str -> int', int(msg))
print('str -> int', int(msg2))

# [4] bool/논리 문자를 다른 데이터 타입으로 변환하기
isOk=False

print('bool -> int', int(isOk))
print('bool -> float', float(isOk))
print('bool -> str', str(isOk))