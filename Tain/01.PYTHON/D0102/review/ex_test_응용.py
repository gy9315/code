# [문제1]
# 정수 2개를 입력 받은 후 7가지 산술연산 결과 출력
# - 출력형태: 9 + 3 = 12, 0b1100, 0o14,0xC
for data in range(3):
    num=input('숫자2개를 입력하시오(예시: 1,2):')
    num=num.strip()
    if len(num)>=3 and ',' in num:
        # num='   6' whitespace str 포함 str(숫자)는 isnumeric 안됨
        if num.split(',')[0].strip().isnumeric() and num.split(',')[1].strip().isnumeric():
            num=num.split(',')            
            num1=int(num[0].strip())
            num2=int(num[1].strip())
            num=num1+num2
            print(f'{num1}+{num2}={num}', bin(num),oct(num),hex(num))
            num=num1-num2
            print(f'{num1}-{num2}={num}', bin(num),oct(num),hex(num))
            num=num1*num2
            print(f'{num1}*{num2}={num}', bin(num),oct(num),hex(num))
            num=num1/num2
            print(f'{num1}/{num2}={num}', bin(int(num)),oct(int(num)),hex(int(num)))
            num=num1//num2
            print(f'{num1}//{num2}={num}', bin(num),oct(num),hex(num))
            num=num1%num2
            print(f'{num1}%{num2}={num}', bin(num),oct(num),hex(num))
            num=num1**num2
            print(f'{num1}**{num2}={num}', bin(num),oct(num),hex(num))
            break
        else: print('숫자를 다시 입력해주세요')
    else: print('양식에 맞게 정확하게 다시 입력해주세요')
# [문제2]
# 3개 단어 입력 받은 후 큰 단어, 작은 단어 출력
# - 출력형태: 'ab', 'abc', 'aba' => 큰 문자열 'abc'
for data in range(3):
    num=input('단어 3개를 입력해주세요(예시: abc,ad,apple):')
    num=num.strip()
    numb=num.find(',')
    numb1=num.find(',',numb+1)
    numb2=num.find(',',numb1+1)
    if len(num)>=5 and str(numb1).isdecimal and numb2==-1 and num.split(',')[0].strip().isalpha() and num.split(',')[1].strip().isalpha() and num.split(',')[2].strip().isalpha():
       num1=num.split(',')[0].strip()
       num2=num.split(',')[1].strip()
       num3=num.split(',')[2].strip()
       print(f'{num1},{num2},{num3} => 큰 문자열 {max(num1, num2, num3)}')
       print(f'{num1},{num2},{num3} => 작은 문자열 {min(num1, num2, num3)}')
       break
    else: print('양식에 맞게 다시 작성해주세요!')