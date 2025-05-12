def centern(a,b,c=' '):
    list1=[x for x in list(a) if x.isalpha()]
    print(a.center(b-2*len(list1),c))
# [1]
## [1-1]
nums=[13,21,12,14,30,18]
for x  in nums:
    print(x)
## [1-2]
for x in nums:
    if not x%2:
        print(x)
## [1-3]
list1=[x for x in nums]
print(f'합계: {sum(list1)} 평균: {sum(list1)/len(list1)}')
## [1-4]
list1.sort(reverse=1)
print(list1)
# [2]
# [2-1]
words = ["I", "study", "python", "language", "!"]
for x in words:
    print(x)
# [2-2]
for x in range(len(words)):
    if x%2:
        print(x)
## [2-3]
for x in words:
    if len(x)>=3:
        print(x)
## [2-4]
list1.sort()
print(list1)
# [3]
files = ['intra.h', 'intra.c', 'define.h', 'run.py', 'ex01.py', 'intro.hwp']
## [3-1]
for x in files:
    print(x.split('.')[0])
## [3-2]
for x in files:
    if x.endswith('.h') or x.endswith('.c'):
        print(x)
## [3-3]
for x in files:
    if x.count('e')>=2 and 'f' in x:
        print(x)
# [4]
num=6
x=1
for y in range(1,num):
    x*=y
print(x)
# [5]
for x in range(2,10):
    print(f'{x}단')
    for y in range(1,10):
        print(f'{x} X {y} = {x*y}')
# [5]
for x in range(2,10):
    print(f'{x}단')
    for y in range(1,10):
        print(f'{x} X {y} = {x*y}')
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