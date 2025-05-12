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