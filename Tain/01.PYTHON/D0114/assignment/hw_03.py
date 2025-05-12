# [1]
def calc(*a,b:str):
    list1=[z for z in a]
    if b=='+':
        x=0
        for y in list1:
            x+=y
        return x
    if b=='*':
        x=1
        for y in list1:
            x*=y
        return x
    if b=='!':
        x=1
        for y in range(1,list1[0]+1):
            x*=y
        return x            
print(calc(5,b='!'))
# [2]
num='2000.07.01'
def calc_age(a):
    a=a.split('.')
    return 2024-int(a[0].strip())
age=calc_age(num)

print(f'당신의 한국 나이는 {age}세입니다. ')
# [3]
def calc_dan(a):
    for x in range(10):
        if x<=3:
            print(f'{a} X {x} = {a*x}'.center(10),end='     ')
        elif x==4:
            print(f'{a} X {x} = {a*x}'.center(10))
        elif x<=8:
            print(f'{a} X {x} = {a*x}'.center(10),end='     ')
        else:
            print(f'{a} X {x} = {a*x}'.center(10))
num=5
calc_dan(num)
# [4]
def score_grade(a):
    return 'A' if int(a)>=90 else 'B' if int(a)>=80 else 'C' if int(a)>=70 else 'D' if int(a)>=60 else 'F'
num=81
a=score_grade(num)
print(f'당신의 학점은: {a}학점')
# [5]
def divi_zero(a):
    data=[]
    for x in range(1,int(a)+1):
        if not a%x:
            data.append(x)
    return data
num=28
a=divi_zero(num)
print(f'{num}의 약수: {a}')

# [6]
def only_numeric(a):
    data=[x.strip() for x in a if x.isnumeric()]
    return ' '.join(data)
msg='Phone 010-2121-9876'
a=only_numeric(msg)
print(f'문자열 내의 숫자: {a}')  

# [7]
def ord_hex(a):
    data=[ord(x) for x in a]
    data1=list(map(hex,data))
    return ''.join(data1)
msg='Hello'
a=ord_hex(msg)
print(f'{msg}의 코드값: {a}')
# [8]
data2=[('홍길동','N20123'),('이철수','N20124'),
       ('이나영','N20125'),('김민우','N20126'),('박보민','N20127'),('이나영','N20128'),('김지은','N20129')]
data1=['합격','합격','불합격','대기','불합격','합격','대기']
data=dict(zip(data2,data1))
print(data)
## [8-1]
def search_value(a):
    b=tuple(a.split())
    return data.get(b)
msg='김민우 N20126'
x=search_value(msg)
print(f'검색결과: {x}')
## [8-2]
def search_key(a):
    data_value=list(data.values())
    data_key=list(data.keys())
    a=[data_value.index(x) for x in data_value if a==x]
    b=[data_key[x] for x in a]
    c=''
    for x in range(len(b)):        
        for y in range(len(data_key[x])):
            if not y%2:
                c+=data_key[x][y]   
            else:
                c+='('+data_key[x][y]+').'         
    return ' '.join(c.split('.'))
print(search_key('합격'))
# [9]
def upper_lower(a):
    str1=''
    for x in a:
        if x.islower():
            str1+=x.upper()
        else: str1+=x.lower()
    return str1
msg='Apple'
print(upper_lower(msg))
# [10]
def max_min_user(a,b=1):
    m=a.replace(',','')
    m=m.replace(' ','')
    data=[x.strip() for x in a.split(',')]
    if m.isalpha():
        x=[data[0]]
        if b==1:
            for y in data[1:]:
                if x[0]<y:
                    x.clear()
                    x.append(y) 
        if b==0:
            for y in data[1:]:
                if x[0]>y:
                    x.clear()
                    x.append(y)
        return x[0]
    else:
        data=list(map(int,data))
        x=[data[0]]
        if b==1:
            for y in data[1:]:
                if x[0]<y:
                    x.clear()
                    x.append(y) 
        if b==0:
            for y in data[1:]:
                if x[0]>y:
                    x.clear()
                    x.append(y)
        return x[0]
        
msg='10, 9, 8, -3, 7, 5, -1, 0'
msg1='A, z, q, H, Z, y'

print(max_min_user(msg,0))
print(max_min_user(msg1,1))



