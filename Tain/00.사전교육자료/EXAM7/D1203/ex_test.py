# 복습 문제
# ------------------------------------------------------
# [1] 2개의 숫자를 입력 받아서 비교연산 6가지 수행 결과 출력
num=int(input('숫자를 입력하세요:'))
num1=int(input('숫자를 입력하세요:'))
print(f'{num}>{num1}={num>num1}')
print(f'{num}<{num1}={num<num1}')
print(f'{num}>={num1}={num>=num1}')
print(f'{num}<={num1}={num<=num1}')
print(f'{num}=={num1}={num==num1}')
print(f'{num}!={num1}={num!=num1}')
# [2] 생일을 아래와 같은 형식으로 출력하세요.
# - 출력형태: 12월 24일 2010년 생일축하!
# 3가지 방시을 모두 사용
# [1] 기존
mon=12
day=24
year=2010
print(mon,'월',' ',day,"일",' ',year,'년',' ','생일축하!',sep='')
# [2] 서식지정자(%)사용
print('%d월 %d일 %d년 생일축하!' %(mon, day, year))
# [3] F-string 사용
print(f'{mon}월 {day}일 {year}년 생일축하!')