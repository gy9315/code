# 가운데 정렬 함수만들기
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

def calc(a,b):
    if not b==0:
        return a+b,a-b,a*b,round(a/b,1)
    else: return a+b,a-b,a*b,'계산할 수 없습니다.'
    
def check_calc(a):
    return len(a)>=3 and ''.join([x for x in a.split(',')]).isnumeric and ',' in a
def menu():
    print('*'*242)
    print('\n'*5)
    print(center_n('[MENU]'))
    print('\n'*5)
    print(center_n('1. 숫자입력'))
    print('\n'*3)
    print(center_n('2. 종료'))
    print('\n'*5)
    print('*'*242)
    
def menu2(a,b):
    print('*'*242)
    print('\n'*5)
    print(center_n(f'[숫자1: {a},  숫자2: {b}]'))
    print('\n'*5)
    print(center_n('1. 덧셈'))
    print('\n'*5)
    print(center_n('2. 뺼셈'))
    print('\n'*5)
    print(center_n('3. 곱셈'))
    print('\n'*5)
    print(center_n('4. 나눗셈'))
    print('\n'*5)
    print('*'*242)
    print('\n')
    
# ---------------------------------------------------------------
a=0
while a==0:
    b=0
    menu()
    choice=input(center_n('메뉴 입력:')).strip()
    if choice=='1':
        num=input(center_n('숫자 2개 입력(예:1,2):')).strip()
        check=''
        if check_calc(num):
            while b==0:
                num1=int(num.split(',')[0].strip());num2=int(num.split(',')[1].strip())
                x,y,z,m=calc(num1,num2)
                menu2(num1,num2)
                choice=input(center_n('메뉴 입력:')).strip()
                if choice=='1':
                    print('\n'*20)
                    print(center_n(f'{num1} + {num2} = {x}'))
                    print('\n'*20)
                    b=1                          
                elif choice=='2':
                    print(center_n(f'{num1} - {num2} = {y}'))
                    b=1
                elif choice=='3':
                    print('\n'*20)
                    print(center_n(f'{num1} X {num2} = {z}'))
                    print('\n'*20)
                    b=1
                elif choice=='4':
                    b=1
                    print('\n'*20)
                    print(center_n(f'{num1} ÷ {num2} = {m}'))
                    print('\n'*20)
                elif choice=='5':
                    a=1;b=1
                else: 
                    print(center_n('정확한 메뉴번호를 입력해주세요!!!'))
                    continue
                if b==1:
                    break
    elif choice=='2': 
        a=1
    else:
        print(center_n('정확한 메뉴번호를 입력해주세요!!!'))
        continue
    if a==1:
        print(center_n('프로그램 종료'))
        break

    
