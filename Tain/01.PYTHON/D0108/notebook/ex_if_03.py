# 제어문 - 조건문
# - 특정 조건에 맞을 시 실행되는 경우와 실행되지 않는 코드 구분 실행
# [문] 숫자가 양수, 0, 음수 여부를 판단해서 출력하세요
num=-4
if str(abs(num)).isnumeric and str(num)!=0:
    if num>0: data='양수'
    elif num<0: data='음수'
    else: data='0'
else: data='잘못된 숫자가 입력되어있습니다.'
print(f'{num}은(는) {data}')
# [문] 점수에 대한 학점을 출력하세요
# - A: 90점 이상
# - B: 80점 이상 90점 미만
# - C: 70점 이상 80점 미만
# - D: 60점 이상 70점 미만
# - F: 60점 미만
num=78
if num>=90: data='A'
if 80<=num<90: data='B'
if 70<=num<80: data='C'
if 60<=num<70: data='D'
if num<60: data='F'
print(f'당신의 학점은 {data}입니다.')
# ------------------------------------------
num=61
if num>=90: data='A'
elif num>=80: data='B'
elif num>=70: data='C'
elif num>=60:data='D'
else: data='F'
print(f'당신의 학점은 {data}입니다.')