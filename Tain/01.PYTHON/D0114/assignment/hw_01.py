# [1]
# [1-1]
def class_score():
    a=int(input('점수를 입력하세요:').strip())
    data='A' if a>=90 else 'B' if a>=80 else 'C' if a>=70 else 'D' if a>=60 else 'B'
    print(f'당신은 "{data}"학점입니다.')
class_score()
# [1-2]
def trans():
    data=dict(달러=1167,엔=1.096,유로=1268,위안=171)
    a=input('금액 및 통화명 입력:')
    x,y=a.split()
    print(f'환전금액: {round(int(x)*data[y.strip()],1)}원')
data=dict(달러=1167,엔=1.096,유로=1268,위안=171)
trans()
# [1-3]
def phone_name():
    data=dict(zip(['011','016','019','010'],['SKT','KT','LGU','알수없음']))
    a=input('전화번호:').split('-')
    x,_,_=a
    print(f'통신사: {data[x.strip()]}') 
phone_name()
[2]
# [2-1]
data=dict(강북구=[0,1,2],도봉구=[3,4,5,6],노원구=[6,7,8,9])
a=list(input('우편번호:').strip())
_,_,x,*_=a
data='강북구' if int(x) in list(data.values())[0] else '도붕구' if int(x) in list(data.values())[1] else '노원구'
print(f'지 역: {data}')
# [2-2]
a=input('주민번호:').split('-')
x,y=a
y=y.strip()[0]
x=x[:2]
data1=2026-(1900+int(x)) if y in '1256' else 26-int(x) 
data='남자' if y in '13' else '여자'
print(f'성별: {data}')
print(f'나이: {data1}')
# [2-3]
import random
x=0
while x==0:
    data=['가위','바위','보']
    data1=data[random.randint(0,2)]
    a=input('가위바위보 ~ (종료를 원하면 아무거나 누르삼):').strip()
    if a==data1: print(f'비겼답니다. 컴퓨터: {data1}')
    elif a=='가위':
        if data1=='보': print(f'축하 축하 당신이 이겼어요^^. 컴퓨터: {data1}')
        else: print(f'당신이 졌군요ㅠㅠ. 컴퓨터: {data1}')
    elif a=='바위':
        if data1=='가위': print(f'축하 축하 당신이 이겼어요^^. 컴퓨터: {data1}')
        else: print(f'당신이 졌군요ㅠㅠ. 컴퓨터: {data1}')
    elif  a=='보':
        if data1=='주먹': print(f'축하 축하 당신이 이겼어요^^. 컴퓨터: {data1}')
        else: print(f'당신이 졌군요ㅠㅠ. 컴퓨터: {data1}')
    else: x=1
    if x==1:
        print('게임종료')
        break
# [3]
## [3-1]
fruits = ['사과', '귤', '수박', '딸기', '바나나']
x=len(fruits)
while x>0:
    print(fruits[x-1])
    x=x-1
## [3-2]
num3=list(range(3,10001,3))
num7=list(range(7,10001,7))
num=list(set(num3)|set(num7))
num.sort()
x=0
while x<len(num):
    print(num[x])
    x=x+1
## [3-3]
dataEng=['Happy', 'Good', 'Dog', 'Cat']
data=[]
x=0
while x<len(dataEng):
    data.append(dataEng[x].lower())
    x=x+1
print(data)
## [3-4]
com = ["SK하이닉스", "삼성전자", "LG전자", '카카오']
x=0
data=[]
while x<len(com):
    data.append(len(com[x]))
    x=x+1
print(data)
## [3-5]
numList = [13, 21, 12, 14, 30, 18, 9, 2, 3, 8, 11, 23]
x=0
y=0
while x<len(numList): # 12
    if not x%2:
        y=y+numList[x]
    x=x+1
print(y)
print(sum([numList[x] for x in range(len(numList)) if not x%2]))
## [3-6]
a=0
x=numList = [13, 21, 12, 14, 30, 18, 9, 2, 3, 8, 11, 23]
x=0
y=0
while x<334:
    y=y+1
    x=x+y
print(y)
    
x=0
y=0
while a==0:
    y=y+1
    x=x+y
    if x>=333:
        a=1
        print(y)
        break
## [3-7]
def centern(a,b,c=' '):
    list1=[x for x in list(a) if x.isalpha()]
    print(a.center(b-2*len(list1),c))

a=int(input('좋아하는 단:').strip())
x=9
centern(f'{a}단',12,'=')
while x>0:
    centern(f'{a} X {x} = {a*x}',12)
    x=x-1
# [3-8]
import random
x=random.randint(1,100)

while True:
    num=input('빙고넘버:').strip()
    if int(num)<x: print(f'{num}보다 큰 수')
    else: print((f'{num}보다 작은 수'))
    if int(num)==x:
        print('빙고!')
        break
# [3-9]
num1=range(1,101)
num3=range(3,101,3)
num5=range(5,101,5)
num35=set(num3)|set(num5)
num=list(set(num1)-num35)
num.sort()
x=0
while x<len(num):
    print(num[x])
    x=x+1
## [3-10]

menu=[1,2,3]
print(len(menu) in range(3,100,2))
def calc(num1,num2):
    return num1+num2,num1-num2,num1*num2,num1/num2 if num2!=0 else '잘못된 값 입니다.'
menu=[]
result=[]
x=0
while x==0:
    a=input('숫자입력:').strip()
    menu.append(a)

    result.extend(menu)
    centern(f'{" ".join(menu)}',10)
    if len(menu) in list(range(3,100,2)):
        plus,minu,multi,div=calc(int(result[0]),int(result[-1]))
        if menu[-2]=='+': 
            result.clear()
            result.append(plus)
        elif menu[-2]== '-': 
            result.clear()
            result.append(minu)
        elif menu[-2]== '*':
            result.clear()
            result.append(multi)
        else: 
            if str(round(div)).isnumeric():
                result.clear()
                result.append(div)
            else:
                x=1
                print('바보보')
                break
    centern('1. +',10)
    centern('2. -',10)
    centern('3. *',10)
    centern('4. /',10)
    centern('5. =',10)
    b=int(input('수식 번호입력').strip())
    if b==1:
        c='+'
        menu.append(c)
    if b==2:
        c='-'
        menu.append(c)
    if b==3:
        c='*'
        menu.append(c)
    if b==4:
        c='/'
        menu.append(c)
    if b==5:
        c='='
        print(result[0])
        result.clear()
        menu.clear()
        x=1
    centern(f'{" ".join(menu)}',10)
[3-11]
# join함수 이용시 숫자는 str처럼 합치지 못함함
a=input('단어입력:').strip()
list1=[(ord(x)) for x in a]
list1_=[str(ord(x)) for x in a]
list3=list(map(hex,list1))
print(f'10진수 코드값: {" ".join(list1_)}')
print(f'16진수 코드값: {" ".join(list3)}')
# [3-12]
a=int(input('단:').strip())
list1=[f'{a} X {x} = {a*x}' for x in range(1,10)]
print(list1)
