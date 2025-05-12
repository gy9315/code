# comprehension
# - for ~ in + if + list/set/dict 결합한 문법
# - 시간과 메모리 상의 이득으로 아주 많이 사용됨

# str타입 숫자를 여러개 저장한 list
# int타입 숫자로 변환한 새로운 list생성
msg=['1','2','3','4','5','6']
for x in msg:
    msg[msg.index(x)]=int(x)
print(msg)

msg=['1','2','3','4','5','6']
msg1=[]
for x in msg:
    msg1.append(int(x))
print(msg1)
# []와 for 결합
msg=['1','2','3','4','5','6']
msg1=[int(x) for x in msg]
print(msg1)
# -------------------------------------------------
# 숫자 데이터를 저장하고 있는 list에서 2의 배수인 숫자만
# 새로운 list에 원소로 넣기기
msg=list(range(1,20))
msg1=[]
for x in msg:
    if not x%2: msg1.append(x)
print(msg1)

msg=list(range(1,20))
msg1=[x for x in msg if not x%2]
print(msg1)

# 숫자 데이터를 저장하고 있는 list에서 2의 배수인 숫자는 제곱
# 2의 배수가 아닌 숫자는 그대로 전달
msg=list(range(1,11))
msg1=[]
for x in msg:
    if not x%2: msg1.append(x**2)
    else: msg1.append(x)
print(msg1)

msg=list(range(1,11))
msg1=[x**2 if not x%2 else x for x in msg]
print(msg1)