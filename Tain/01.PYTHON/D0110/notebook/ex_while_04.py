# 제어문 while 반복문
# - 반복횟수가 미정인 경우에도 사용 가능
# - 반복횟수가 정해진 경우에도 사용 가능함
# ----------------------------------------------------
# 반복 횟수가 정해지지 않은 경우
# 로또 프로그램
# - 기능: 1 ~ 45까지 숫자 중 6개
import random
# 랜덤 객체 생성 -> 힙영역 저장
r=random.Random()
# 랜덤 개체가 가진 기능 즉, method 사용
# random(): 0.0 ~ 1.0 범위에서 숫자 1개 추출
for idx in range(10):
    print(int(r.random()*10))   
# randint(x,y): x <= num <= y 정수 1개 추출출
for idx in range(6):
    value=r.randint(1,45)
    print(value,end=' ')   
set1=set()
# 중복되지 않는 숫자 6개
while len(set1)==6:
    value=r.randint(1,45)
    set1.add(value)
    print(set1)  