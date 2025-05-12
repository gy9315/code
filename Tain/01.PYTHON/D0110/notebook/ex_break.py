# # 제어문 제어용 키워드
# # - break: 반복문 즉시 중단시킴, 단 가장 가까이 있는
# #          반복문만 해제 시킴
# # -------------------------------------------------
# # [중첨 반복문 중단시키기] 중단여부를 확인하는 변수명 반복문당 n-1개 필요요
# is_stop=False # 내부 반복문 중단 여부 저장장
# for x in range(10):
#     print(f'{x} 문자: {chr(x)}')
#     for y in range(10):
#         print('*'*y)
#         if x==3:
#             is_stop=True
#             break
#     # 내부에 반복문이 중단되어있다면 멈춰라
#     if is_stop==True:
#         break
# # [중첨 반복문 중단시키기] 중단여부를 확인하는 변수명 반복문당 n-1개 필요요
is_stop=False # 내부 반복문 중단 여부 저장
num=0
while num<4:
    num=1+num
    print(f'{num} 문자: {chr(num)}')
    for y in range(4):
        print('*'*y)
        if num==2:
            is_stop=True
            break
    if is_stop==True:
        break
    # 내부에 반복문이 중단되어있다면 멈춰라

2