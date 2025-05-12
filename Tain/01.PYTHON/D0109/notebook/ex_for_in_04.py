# 제어문 for ~ in 반복문
# [문제] 구구단 출력하기
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