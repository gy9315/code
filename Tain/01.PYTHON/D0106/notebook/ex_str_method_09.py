# str 타입 전용 함수 즉, method
# - 사용법: 변수명.method()
# -------------------------------------------
# [9] 문자열 앞부분, 끝부분 공백 제거 method:
# - 문법: 앞부분(lstrip), 뒷부분(rstrip), 앞/뒷부분(strip)
data='  Good luck   '
print(f'{data}의 원소 개수: {len(data)}')
print(f'{data}의 앞부분 공백을 제거한 원소 개수: {len(data.lstrip())}')
print(f'{data}의 뒷부분 공백을 제거한 원소 개수: {len(data.rstrip())}')
print(f'{data}의 앞/뒷분 공백을 제거한 원소 개수: {len(data.strip())}')
# [실습]
data=input('댓글입력:').strip()
print(f'입력 데이터 여부: {len(data)>0}')