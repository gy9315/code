
# ---------------------------------------------------------------
# while 종료 변수 만들기
a=0

# 메뉴 보이기
while a==0:
    b=0
    print('*'*30)
    print('\n'*5)
    print(('[MENU]').center(30))
    print('\n'*5)
    print(('1. 숫자입력').center(30))
    print('\n'*3)
    print(('2. 종료').center(30))
    print('\n'*5)
    print('*'*30)
    # ---------------------------------------------------------------
    # 메뉴 선택 입력받기
    choice=input('메뉴 입력:').strip()
    if choice=='1':
    # 숫자 입력받기
        num=input('숫자 2개 입력(예:1,2):').strip()
        check=''
    # 입력값 체크(길이 3이상, 숫자, 쉼표존재)
        if len(num)>=3 and ''.join([x for x in num.split(',')]).isnumeric and ',' in num:
            while b==0:
            # 입력 값이 참일 때 연산자 선택 메뉴 보이기
                print('*'*30)
                print('1. 덧셈'.center(30));print('2. 뺄셈'.center(30));print('3. 곱셈'.center(30));print('4. 나눗셈'.center(30))
                print('*'*30)
                print('\n')
                # 덧셈 후 출력
                choice=input('메뉴 입력:').strip()
                num1=int(num.split(',')[0].strip());num2=int(num.split(',')[1].strip())
                if choice=='1':
                    print(f'{num1} + {num2} = {num1+num2}')
                    b=1                          
                # 뺄셈 후 출력
                elif choice=='2':
                    print(f'{num1} - {num2} = {num1-num2}')
                    b=1
                # 곱셈 후 출력   
                elif choice=='3':
                    print(f'{num1} X {num2} = {num1*num2}')
                    b=1
                # 나눗셈 후 출력
                elif choice=='4':
                    b=1
                    if not num2==0: 
                        print(f'{num1} ÷ {num2} = {round(num1/num2,1)}')
                    else: 
                        print('계산할 수 없습니다!')
                # 종료
                elif choice=='5':
                    a=1;b=1
                else: 
                    print('정확한 메뉴번호를 입력해주세요!!!')
                    continue
                if b==1:
                    break
    # 메뉴 다시보이기
        # else: pass
    elif choice=='2': 
        a=1
    # 메뉴 다시 보이기
    else:
        print('정확한 메뉴번호를 입력해주세요!!!')
        continue
    if a==1:
        print('프로그램 종료')
        break

    
