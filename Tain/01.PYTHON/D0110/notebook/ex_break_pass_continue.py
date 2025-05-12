# 제어문 제어용 키워드
# - break: 반복문 즉시 중단시킴, 단 가장 가까이 있는
#          반복문만 해제 시킴
# - pass: 아무일도 없음(python문법적으로 들여쓰기가 필요한)
#         문법의 경우 실행 코드 미작성 시 사용됨
# - continue: 반복문에서 아래의 코드는 실행하지 않고 다음
#             다음 요소로 이동할 수 있도록 함
# [기본]
for num in range(1,51):
    if num%3:
        print(num,end=' ')
print()
# [for continue]        
for num in range(1,51):
    if num%3==0: continue
    print(num, end=' ')
print()   
# [while continue] 변수 업데이트가 continue전에 진행
#                  * 안그러면 무한반복진행
num=0
while num<50:
    num=num+1
    if num%3==0: continue
    print(num, end=' ')

