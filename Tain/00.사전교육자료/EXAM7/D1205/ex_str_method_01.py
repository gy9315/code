# 문자열 str type 전용 함수 즐, method
# - 사용법: str type의 변수명.method()
# --------------------------------------------
data='1'
print(data.isdigit())
print(len(data))
msg='Merry Christmas! Happy New Year 2025'
# [1] 특정 문자 1개/문자 여러개의 index의 method
# - 변수명.index('문자'): 문자의 index을 알려줌
# - 없는 문자가 있는 경우 ERROR 발생
print(f"M의 index: {msg.index('M')}")
print(f"mas의 index: {msg.index('mas')}")# 첫시작의 index을 알려줌
print(f"M의 index: {msg.index('M')}")
# 똑같은 문자열이 여러개 있는 경우: 제일 먼저 발견된 문자의 index을 알려줌
print(f'r의 인덱스:{msg.index("r")}')
print(f'r의 인덱스:{msg.index("r",4,17)}')
r_index=msg.index("r")
print(f'r의 첫번째 index: {r_index}')
r_index=msg.index("r",r_index+1)
print(f'r의 두번째 index: {r_index}')
r_index=msg.index("r",r_index+1)
print(f'r의 세번째 index: {r_index}')
# [2] 특정 문자 1개/문자 여러개의 index의 method
# - 변수명.find('str') * 없는문자: -1
msg='Merry Christmas! Happy New Year 2025'
print(f'y의 인덱스:{msg.find("y")}')
# [3] 특정 문자 1개/문자 여러개가 문자열 안에 몇개 존재하는지 개수를 알려주는 method
# - 변수명.count(): 개수
print(f'y의 첫번째 index: {msg.count("y")}')
# [4] 문자열의 왼쪽 오른쪽의 공백 제어 method
# - 변수명.lstrip(): 문자열 앞부분 공백제거
# - 변수명.rstrip(): 문자열 뒷부분 공백제거
# - 변수명.strip(): 문자열 앞부분 and 뒷부분 공백제거
msg='   Good luck     '
print(f'msg의 길이/원소개수: {len(msg)}{msg}')
msg2=msg.lstrip()
print(f'msg의 길이/원소개수: {len(msg)}{msg.lstrip()}')
print(f'msg의 길이/원소개수: {len(msg)}{msg2}{len(msg2)}')
# --------------------------------------------------------------
msg2=msg.rstrip()
print(f'msg의 길이/원소개수: {len(msg)}{msg.rstrip()}{len(msg2)}')
# --------------------------------------------------------------
msg2=msg.strip()
print(f'msg의 길이/원소개수: {len(msg)}{msg.strip()}{len(msg2)}')