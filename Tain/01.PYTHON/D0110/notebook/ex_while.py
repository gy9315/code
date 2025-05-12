# 제어문 while 반복문
# - 반복횟수가 미정인 경우에도 사용 가능
# - 반복횟수가 정해진 경우에도 사용 가능함
# [1. 반복횟수가 정해진 경우]
for x in range(10,0,-1):
    print(x,end=' ')
print()
# [while 사용]
count=10
while count>0:
    print(count,end=' ')
    count=count-1
print('\n')
# [구구단]
num1=9
num=9
print(f'{num1}단'.center(20))
print()
while num>0:
    print(f'{num1} X {num} = {num1*num}'.center(20))
    num=num-1