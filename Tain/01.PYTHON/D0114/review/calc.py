# 4칙 연산 계산기
# - 기능: 덧셈, 뺄셈, ..., 나눗셈
# - 이름: calc
# - 변수: a,b
# - 출력: 덧셈 ... 나눗셈
def calc(*a):
    x=0
    y=a[0]
    z=1
    m=a[0]
    if len(a)>1 and a[-1]!=0:
        for A in a:  
            x=x+A
        for A in a[1:]:
            y=y-A
        for A in a:
            z=z*A
        for A in a[1:]:
            m=m/A
            return x,y,z,m
    elif len(a)>1 and a[-1]==0:
        for A in a:  
            x=x+A
        for A in a[1:]:
            x=x-A
        for A in a:
            z=z*A   
        return x,y,z,'계산오류'
    elif len(a)==1: return a
print(calc(3,5,8,0))
# 메뉴표시
# - 기능: 가운데 표시
# - 이름: centern
# - 변수: a
# - 출력: 중간값값
def centern(a):
    list1=[x for x in a if x.isalpha()] 
    x=50-len(list1)
    return a.center(x)
    
    
# 메뉴표시
# - 기능: 메뉴표시
# - 이름: menu
# - 변수: a
# - 출력: none(print)
def menu1(a):
    print('='*50)
    print('\n'*2)
    print('\033[1m\033[97m')
    print(centern(a.split(',')[0].strip()))
    print('\033[0m')
    for x in a.split(',')[1:-1]:
        print(centern(x.strip()),'\n')
    print('\033[2m')
    print(centern(a.split(',')[-1].strip()))
    print('\n'*3)
    print('\033[0m')
    print('='*50)

# ------------------------------------------------------------------------
menu1('[계산기],1. 계산, 2. 종료, 메뉴번호를 입력해주세요')
input()

    