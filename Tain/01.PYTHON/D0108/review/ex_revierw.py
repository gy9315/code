# [1] dict
msg=dict(a='b',c='d',e='f')
print(msg)
msg.update(abc=123)
print(msg)
msg.update(zip([1,2,3],['a','b','c']))
print(msg)
list_=[]
list_.extend(zip([1,2,3],['a','b','c']))
print(list_)
print(list(zip([1,2,3],['a','b','c'])))
# 12-5
msg='health mana melee attack_speed magic_resistance'
num='537.6 308.8 600.0 0.625 35.7'
msg_list=[]
num_list=[]
for data in msg.split():
    msg_list.append(data)
for data in num.split():
    num_list.append(float(data))
data=dict(zip(msg_list,num_list))
print(data)
# [2] if 가정문
x=10
if x==10:
    pass
x=20
if x>=10:
    print('10 이상입니다.')
    if x==15:
        print('15입니다.')
    if x==20:
        print('20입니다.')
# 13-6
x=5
if x!=10:   
    print('OK')
# 13-7
price=input('가격을 입력해주세요:')
insale=input('쿠폰코드를 입력해주세요:')
if insale=='Cash3000':
    data=3000
elif insale=='Cash5000':
    data=5000
print(int(price)-data)