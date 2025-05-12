# [1]
## 1-1
# num=input('점수를 입력해주세요:')
num=90
if num>=90: data='A'
elif num>=80: data='B'
elif num>=70: data='C'
elif num>=60: data='D'
else: data='F'
print(f'당신의 학점은: {data}입니다.')
## 1-2
s={'국어':98,'영어':45,'수학':72,'미술':99}
x=input('과목을 입력해주세요:')
print(s.get(x.strip(),'존재하는 과목이 아닙니다.'))
## 1-3
for y in range(3):
    num=input('데이터 입력:')
    if len(num.strip())!=0:
        for x in range(5): 
            print(num)
        break
    else: print('데이터를 추가 해주세요')
## 1-4
num=input('무게를 입력해주세요:')
print(num)
if int(num.strip())>=10: data='1등급'
elif int(num.strip())>=7: data='2등급'
elif int(num.strip())>=4: data='3등급'
else: data='4등급'
x=[]
y=[]
x.append(int(num))
y.append(data)
z=dict(zip(x,y))
print(z)
## 1-5
num=input('나이 입력:')
if num>=65: data='노년'
elif num>=50: data='장년'
elif num>=30: data='중년'
elif num>=19: data='청년'
elif num>=13: data='청소년'
elif num>=6: data='아동'
else: data='영·유아'
print(f'당신의 연령은: {data}입니다.')
## 1-6
x=input('입력:')
for z in x:
    if z.isupper():
        print(z.lower(),end='')
    else: print(z.upper(),end='')
print()
## 1-7
num=input('숫자 입력:')
if num.strip().isnumeric() and len(num.strip())!=0:
    print('입력 OK')
else: print('숫자 데이터가 아닙니다.')
## 1-8
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
    else:print('정확한 연산자자를 입력해주세요!!')
## 1-9
msg=input('알파벳 또는 한글 1개 입력:')
data=ord(msg.strip()) if msg.strip().isalpha() else '정확한 데이터가 아닙니다.'
print(data)
## 1-10
num=input('숫자입력:')
data='양수' if int(num)>0 else '0' if int(num)==0 else '음수'
print(f'{num}은 {data}입니다.')