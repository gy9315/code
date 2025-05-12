# [데이터생성] 1 ~ 50000까지 숫자를 저장하는 list 생성
# 숫자 범위 생성해주는 내장함수: range(variation)
#  ex) range(시작번호, 끝번호+1): 1부터 50000까지의 함수
#         * 시작번호 <= X < 끝번호
num=range(1, 501)
print(len(num))
print(f'num의 type: {type(num)}')
print(list(num))
num_list=list(num)
print(f'num의 type: {type(num_list)}')