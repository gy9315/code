# [1]
## 1-1
nums=[13,21,12,14,30,18]
for x in nums:
    print(x)
num=[x for x in nums if not x%2]
print(num)
print(f'평균: {sum(nums)}, 평균: {sum(nums)/len(nums)}')
nums.sort(reverse=1)
print(nums)
## 1-2
words=['I','study','python','language','!']
for x in words:
    print(x)
word=[x for x in words if words.index(x)%2]
print(word)
word=[x for x in words if len(x)>=3]
print(word)
words.sort()
print(words)
## 1-3
files=['intra.h', 'intra.c', 'define.h', 'run.py', 'ex01.py', 'intro.hwp']
file=[x.split('.')[0] for x in files]
print(file)
file=[x for x in files if x.split('.')[1] in 'hc' ]
print(file)
file=[x for x in files if x.count('e')>=2 and 'f' in x ]
print(file)
## 1-4
num=input()
num1=int(num)
for x in range(1,int(num)):
    num1=num1*x
print(f'{num}! 결과:{num1}')
## 1-5
for y in range(1,7):
    if y==1:
        
        for x in range(2,6):
            print('{:5}단'.format(x), end='        ')
    if y==2 or y==5:print()
    if y==3 or y==6:
        for x in range(1,10):
            if y==3:
                for z in range(2,6):
                    print(f'{z} X {x} = {z*x}'.center(10), end='      ')
                    if z==5: print()
            if y==6:
                for z in range(2,6):
                    print(f'{z} X {x} = {z*x}'.center(10), end='      ')
                    if z==5: print()
    if y==4:    
        print()
        for x in range(6,10):
            print('{:5}단'.format(x), end='        ')
## 1-6
for x in range(4):
    num=input('숫자 2개를 입력해주세요:')
    if len(num.strip())>=3 and ',' in num and num.split(',')[0].strip().isnumeric() and num.split(',')[0].strip().isnumeric():
        num=[int(x.strip()) for x in num.split(',')]
        break
    else:print('정확한 숫자를 입력해주세요!!')
for x in range(4):
    num1=input('연산자를 입력해주세요(+,-,*,/):').strip()
    if num1 in '+-*/' and len(num1.strip())==1:
        if num1=='+': print(f'{num[0]} + {num[1]} = {num[0]+num[1]}')
        if num1=='-': print(f'{num[0]} - {num[1]} = {num[0]-num[1]}')
        if num1=='*': print(f'{num[0]} * {num[1]} = {num[0]*num[1]}')
        if num1=='/': print(f'{num[0]} / {num[1]} = {num[0]/num[1]}')
    else:print('정확한 연산자를 입력해주세요!!')