# 연산자(Operator) - 논리연산자
# - 왼쪽 and 오른쪽 : 그리고
#                    True and True: True
# - 왼쪽 or 오른쪽 : 또는
#                    True or False: True
#                    False or False: False
# - not 오른쪽 : 오른쪽 반대로(toggle)
#                    not True: False
#                    not and False: True
# -----------------------------------------------------------
# [문제] 입력받은 데이터가 5 또는 10인 경우 체크
for data in range(4):
    num=input(f'숫자 한개만 입력해주세요({4-data}):').strip()
    if num.isdecimal() and len(num)==1:
        num=int(num)
        if num==5 or num==10:
            print(f'5 또는 10이 맞습니다.')
            break
        else:
            print(f'5 또는 10이 아닙니다.')
    elif num.isnumeric() and (len(num)>1 or len(num)==0):
         print('숫자 1개를 다시 입력해주시길 바랍니다.')
    else : print('숫자가 아닙니다. 다시 입력해 주시길 바랍니다.')
        
# [문제] 임의의 숫자가 3의 배수 또는 5의 배수 여부 체크
# 나머지가 3 또는 5가 아니면 된다
num=33
# 0은 False
print(not num%3 or not num%5) 
# [문제] 30대 여성 여부 체크
gender='여'
age=25
print(f'30대 여성 여부: {gender=="여"and 30<=age<40}')