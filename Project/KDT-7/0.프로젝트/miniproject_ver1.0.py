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
    
# 메뉴창 만들기
## 전체 세로: 56개
print('*'*242)
# 첫 화면 창 생성
## 상식게임에 오신 것을 환영합니다.
print('\n'*24)
print('\033[1m\033[33m')
print(center_n('상식게임에 오신것을 환영합니다'))
print('\n'*4)
print()
print(center_n('게임을 진행하기 위해서 ENTER버튼을 눌러주시기 바랍니다.'))
print('\033[1m\033[33m\033[0m')
print('\n'*23)
print('*'*242)
input()
# 메뉴 창 생성
# 메뉴
# 1. 게임설명
# 2. 게임시작
# 3. 종료
# 게임시작 메뉴창
a=0
b=0
while a==0:
    print('\n'*22)
    print('\033[1m\033[97m')
    print(center_n('1. 게임설명'))
    print('\n'*4)
    print(center_n('2. 게임시작'))
    print('\n'*4)
    print(center_n('3. 게임종료'))
    print('\n'*21)
    print('*'*242)
    choice=input('메뉴번호를 입력해주세요')
# 메뉴선택
    while b==0:
        # 게임설명 나오기
        if choice==1:
            print('\n'*20)
            print(center_n('게임진행 설명'))
            print('\n'*5)
            print(center_n('1.문제 출제자 선정\n\n'))
            print(center_n('2. 문제 입력\n\n'))
            print(center_n('3. 제한시간 선정\n\n'))
            print(center_n('4. 문제 맞추기\n\n'))
            print('\n'*4)
            print('\033[2m\033[97m')
            print(center_n('다음으로 넘어가기 위해서 ENTER버튼을 눌러주시기 바랍니다.'))
            print('\n'*12)
            input()
            print('\n'*10)
            print('\033[0m')
            print(center_n('게임규칙 설명'))
            print('\n'*5)
            print(center_n('1. 출제자 제외 전부 정답 또는 오답 시\n'))
            print(center_n('   출제자 벌칙 수행\n\n'))
            print(center_n('2. 문제풀이자 중 최소 1명이상 정답 시\n'))
            print(center_n('   문제풀이자 중 정답자 및 출제자 제외 벌칙 수행\n\n'))
            print(center_n('3. 문제풀이자, 제한시간 초과 입력 시\n'))
            print(center_n('   벌칙 수행\n\n'))            
            print('\n'*4)
            print('\033[2m\033[97m')
            print(center_n('다음으로 넘어가기 위해서 ENTER버튼을 눌러주시기 바랍니다.'))    
            print('\n'*13)
            
            
            pass
        elif choice==1:
            pass
        elif choice==1:
            pass
        elif choice==1:
            a=1
            b=1
            pass
        else:
            print(center_n('잘못된 입력입니다.'))
            continue
        if b==1:break
    if a==1:
        print(center_n('프로그램을 종료합니다.'))
        break
# 1. 참가인원 선택
# 2. 이름설정
# 3. 종료