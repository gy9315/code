# 연산자(Operator) - 논리연산자
# - 왼쪽 and 오른쪽 : 그리고
#                    True and True: True
# - 왼쪽 or 오른쪽 : 또는
#                    True or False: True
#                    False or False: False
# - not 오른쪽 : 오른쪽 반대로(toggle)
#                    not True: False
#                    not and False: True


# 20대 남자인 경우
gender='남자'
age=30
# - 20대 나이 체크
print(f'{age}는 20대 맞는가?:{20<=age<30}')
# - 남자 성별 체크
print(f'{gender}는 남자가 맞는가?: {gender=="남자"}')
print(f'20대 남자가 맞는가?: {gender=="남자" and age>=20 and age<30}')
# 30대 이상 또는 여자
print(f'30대 이상 또는 여자가 맞는가?: {gender=="여자" or age>=30}')
# -------------------------------------------------------------------------
# not 연산자: 현재 결과 반대
print(f'{age}가 20대 이상이 아닌가?: {not age>=20}')

# ----------------------------------------------------
print(f'not 1: {not 1}')
print(f'not 0: {not 0}')
# 0 또는 0.0이 아닌 숫자는 전부 True
print(f'not -1: {not -1}')
print(f'not 2: {not 2}')
print(f'not -1: {not -1.1}')