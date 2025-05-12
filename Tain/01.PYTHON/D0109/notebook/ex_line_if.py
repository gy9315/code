# 조건부 표현식
# - if ~ else 문법을 1줄로 표현하는 문법
# - 문법: (참일 때 실행 코드) if 조건문 else (거짓일 때 실행 코드) 
# [문제] 양수, 음수 구별해서 출력하기
num=0
print('양수입니다.') if num>=0 else print('음수입니다.')
data='양수' if num>=0 else '음수'
print(f'{num}은 {data}입니다.')
# [문] 양수, 음수, 0 구별해서 출력하기
data='양수' if num>0 else '음수' if num<0 else '0'
print(f'{num}은 {data}입니다.')
# [문] 월에 따른 계절을 알려주세요
# - 봄: 3 ~ 5
# - 여름: 6 ~ 8
# - 가을: 9 ~ 11
# - 겨울: 12 ~ 2
## 다중 조건문
num=13
if num<=2 or num==12:
    data='겨울'
elif num<=5:  
    data='봄'
elif num<=8:
    data='여름'
else:
     if num>=12: data='잘못된 "월" 입력 데이터'
     else: data='가을'
print(f'{num}월은 {data}입니다.')

## 조건부 표현식
num=3
data='겨울' if num<=2 or num==12 else '봄' if num<=5 else '여름' if num<=8 else '가을'
print(data)
