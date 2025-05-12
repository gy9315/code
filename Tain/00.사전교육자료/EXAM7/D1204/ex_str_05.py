# 문자열 str type과 원소(문자) 변경 -> 바꾸기 불가
# - 변수명[]: 특정 인덱스 원소 일기, 가져오기
# - 변수명[] = '새로운 값' X
# --------------------------------------------------
msg='pithon'
# 오타 수정-> [1] index 'i'를 y로 변경
# msg[1]='y'
print(f'id(msg) -> {id(msg)}')
print(f'id("pithon") -> {id("pithon")}')
msg=msg[0]+"y"+msg[2:]
print(msg)