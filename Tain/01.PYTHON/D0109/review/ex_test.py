# 숫자 2개와 4칙 연산자 1개를 입력
# 입력 9 8 + 단, 0으로는 나눌수 없음
print(bool(set()))
num=input('숫자2개와 4칙연산(+,-*,/)입력해주세요:')
num1=int(num.split()[0].strip())
num2=int(num.split()[1].strip())
num3=num.split()[2].strip()
if num3=='+':
    print(f'{num1} + {num2} = {num1+num2}')
elif num3=='-':
    print(f'{num1} - {num2} = {num1-num2}')
elif num3=='*':
    print(f'{num1} * {num2} = {num1*num2}')
elif num3=='/':
    if num1==0 or num2==0:
        print('계산할 수 없습니다.')
    else: print(f'{num1} / {num2} = {num1/num2}')
else: print('지원하지 않습니다.')

