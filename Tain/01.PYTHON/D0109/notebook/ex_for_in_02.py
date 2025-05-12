# 제어문 for ~ in 반복문
# [실습] Good Luck이라는 문자열에서 대문자는 소문자로 
#        소문자는 대문자로 변경 후 출력
msg='Good Luck'
msg=list(msg)
for idx in range(len(msg)):
    if msg[idx].isupper():
        msg[idx]=msg[idx].lower()
    else: msg[idx]=msg[idx].upper() 
print(''.join(msg))

msg='Good Luck'
for idx in range(len(msg)):
    if msg[idx].isupper():
        msg.replace(msg[idx],msg[idx].lower())
    else: msg.replace(msg[idx],msg[idx].upper())
print(msg)

msg='1234'
msg.replace('1','5')
print(msg)

msg='Good Luck'
print(msg, end=' =>')
for idx in msg:
    if idx.isupper():
        print(idx.lower(),end='')
    if idx.islower():
        print(idx.upper(),end='')
    if idx==' ':print(' ',end='')
print()
msg='ab cd'
msg.upper()
print(msg)