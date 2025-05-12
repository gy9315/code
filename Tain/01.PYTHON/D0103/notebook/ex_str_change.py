# 문자열 str 데이터 타입
# - 인덱스와 슬라이싱 활용
# [인덱스] 원소/요소 읽기/추출
msg='pithon'
print('msg', msg,id(msg))
print('msg[0]', msg[0],id(msg[0]))
print('msg[1]', msg[1],id(msg[1]))
# 1번 원소 'i'를 'y'로 변경
# ----------------------------
# msg[1]='y' * 미지원 기능
# ----------------------------
print(msg[0]+'y'+msg[2:]) # str+str+str
msg=msg.replace('i','y')
print(msg, id(msg))
# 크리스마스 트리 만들기
for data in range(24):
    print(' '*(24-data),'*'*(2*data+1),' '*(24-data),sep='')
