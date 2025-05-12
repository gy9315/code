def center_n(a):
    y=[]
    z=[]
    d=[]
    for x in a:
        if x.isspace():
            y.append(x)
        elif x.isascii():
            z.append(x)
        else:
            d.append(x)
    return a.center(242-len(d))

def menu(a):
    print('*'*242)
    msg=[x.strip() for x in a.split(',')]
    # 전체 공백: 56개
    print('\n'*(int((48-len(msg)*2)/2)))
    print('\033[1m\033[33m')
    print(center_n(msg[0]))
    print('\n'*5)
    for y in msg[1:-1]:
        print(center_n(y),end='\n\n')
    print('\033[2m\033[97m]')
    print(center_n(msg[-1]),end='\n\n')
    print('\033[0m')
    print('\n'*(int((48-len(msg)*2)/2))) 
    print('*'*242) 
list=(1,2,3,4,5)
list.count
del list[list.index(1)]
print(list)