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

def menu(a):
    print('*'*242)
    msg=[x.strip() for x in a.split(',')]
    # 전체 공백: 56개
    print('\n'*(int((48-len(msg)*2)/2)-1))
    print('\033[1m\033[33m')
    print(center_n(msg[0]))
    print('\n'*5)
    for y in msg[1:-1]:
        print('\033[97m')
        print(center_n(y),end='\n\n')
    print('\033[2m\033[97m')
    print(center_n(msg[-1]),end='\n\n')
    print('\033[0m')
    print('\n'*(int((48-len(msg)*2)/2))) 
    print('*'*242) 
    
# 메뉴창 만들기
## 화면 표현 전체 레이아수: 56개
# 첫 화면 창 생성
## 상식게임에 오신 것을 환영합니다.
menu('[상식게임에 오신것을 환영합니다], 게임을 진행하기 위해서 화면을 Click 후 ENTER버튼을 눌러주시기 바랍니다.')
input()
# 메뉴 창 생성
# 메뉴
# 1. 게임설명
# 2. 게임시작
# 3. 종료
# 게임시작 메뉴창
a=0
b=0
c=0
d=0
while a==0: #####
    b=0
    c=0
    d=0
    menu('[메뉴], 1. 게임설명, 2. 게임시작, 3. 게임종료, 메뉴번호를 입력해주세요')
    choice=input()
# 메뉴선택
    while b==0: #####
        # 게임설명 나오기
        c=0
        d=0
        if choice=='1':
            menu('[게임진행 순서], 1.문제 출제자 선정, 2. 문제 입력,3. 제한시간 선정,4. 문제 맞추기, 다음화면: 화면을 Click 후 ENTER')   
            input()
            menu('[게임규칙],1. 출제자 제외 전부 정답 또는 오답 시:,출제자 벌칙 수행,2. 문제풀이자 중 최소 1명이상 정답 시:,문제풀이자 중 정답자 및 출제자 제외 벌칙 수행,3. 문제풀이자 제한시간 초과 입력 시:,벌칙 수행,처음화면 돌아가기: 화면 Click 후 ENTER버튼')
            b=1
            input()
        elif choice=='2':
            while c==0:
                d=0
                menu('[상식게임], 게임 참가인원을 입력해주세요(3명 이상 ~ :')
                num=input() 
                if num.isnumeric() and int(num)>2:             
                    name=[]
                    for x in range(int(num)):
                        menu('[이름 설정하기], 한 명씩 이름을 입력해주세요:')
                        name.append(input('이름:').strip())
                    while d==0:
                        name=set(name)
                            # 무작위 한명 뽑아서 문제 입력란 받기
                        P1=name.pop()
                        menu(P1+'님, 문제를 입력해주세요' )
                        Q=input('문제:').strip()
                        menu(P1+'님, 정답을 입력해주세요' )
                        P_name=[]
                        P_A=[]
                        P_name.append(P1)
                        P_A.append(input('정답:').strip())                    
                        # 나머지 인원에게 질문보여주고 답변받기
                        for x in name:
                            menu('%s님 차례,%s,정답을 입력해주세요:'%(x,Q))
                            P_name.append(x)
                            P_A.append(input('정답:').strip())
                        dict_P_A=dict(zip(P_name,P_A))
                        menu(f'[정답공개], {P_A[0]},화면을 Click 후 Enter')
                        input()
                        if list(dict_P_A.values()).count(P_A[0])==1 or list(dict_P_A.values()).count(P_A[0])==(len(P_name)):
                            penalty=P_name[0]
                            menu(f'[벌칙수행자 공개],{penalty},벌칙을 수행해주세요!!,다음: Click 후 Enter')
                            input()
                        else:
                            penalty_value=list(set(dict_P_A.values()))
                            penalty_value.pop(penalty_value.index(P_A[0]))
                            penalty_value1='-'.join(penalty_value)
                            menu(f'[벌칙수행자  답 공개],{penalty_value1},벌칙을 수행해주세요!!,다음: Click 후 Enter')
                            input()
                        d=1
                        b=1
                        menu('[다음], 종료를 원하시면 1를 입력,새로운 게임을 원하시면 2를 입력,처음화면으로 돌아가기를 원하시면 0을 입력,계속 진행을 원하면 Click 후 Enter 입력')
                        msg=input()
                        if msg=='1':
                            d=1
                            c=1
                            b=1
                            a=1
                        if msg=='2':
                            d=1
                        if msg=='0':
                            d=1
                            c=1
                            b=1
                        if d==1:
                            break
                elif num.isnumeric() and 0<=int(num)<3:
                    print('잘못된 숫자를 입력했습니다.')
                else: print('숫자를 입력해주세요!!!')
                if c==1:
                    break
            if b==1:break
        elif choice=='3':
            a=1
            break
        else:
            print(center_n('잘못된 입력입니다.'))
            b=1
    if a==1:
        print(center_n('프로그램을 종료합니다.'))
        break