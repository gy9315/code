# 제어문 while 반복문
# - 반복횟수가 미정인 경우에도 사용 가능
# - 반복횟수가 정해진 경우에도 사용 가능함
# 리스트 데이터에 원소를 출력하기
data_list=['하늘','가을','고양이','책']
for data in data_list:
    print(data)
# [while] -> 원소 인덱스 지정
print()
num=len(data_list)
idx=0
while idx<num:
    print(data_list[idx])
    idx=idx+1
    
# 2단부터 9단까지 사용
num=2
while num<10:
    print()
    print(f'{num}단'.center(20))
    num1=1
    while num1<10:
        print(f'{num} X {num1} = {num*num1}'.center(20))
        num1=num1+1
    num=num+1