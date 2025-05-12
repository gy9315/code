# 제어문 for ~ in 반복문
# - 특징
#   * 반복 횟수가 정해진 경우 거의 사용됨
#   * 여러개의 원소/요소를 가지는 데이터 타입의 경우
#     원소/요소 추출에 사용됨
# - 형태
#   for 변수명 in 데이터: 여러개 데이터 저장
#       반복문
msg='Merry Chrismas~'
# 원소 한개씩 출력
print(f'[0번 원소]{msg[0]}, [1번 원소]{msg[1]}, [2번 원소]{msg[2]}',end=', ')
print(f'[3번 원소]{msg[3]}, [4번 원소]{msg[4]}, [5번 원소]{msg[5]}',end=', ')
print(f'[6번 원소]{msg[6]}, [7번 원소]{msg[7]}, [8번 원소]{msg[8]}',end=', ')
print(f'[9번 원소]{msg[9]}, [10번 원소]{msg[10]}, [11번 원소]{msg[11]}',end=', ')
print(f'[12번 원소]{msg[12]}, [13번 원소]{msg[13]}, [14번 원소]{msg[14]}')
# 반복문 사용
for x in msg:
    print(x,end=',')
# msg 코드값으로 출력
print()
for x in msg:
    print(ord(x),end=', ')
# msg 기계어로 출력
print()
for x in msg:
    print(bin(ord(x))[2:],end=', ')
# 숫자 str데이터로 구성된 msg
print()
msg='1 3 5 7 9 11 22'
msg_list=msg.split()
''.join(msg_list)
print('-'.join(msg_list))
for x in msg_list:
    msg_list[msg_list.index(x)]=int(x)

