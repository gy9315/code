# [데이터생성] 1 ~ 50000까지 숫자를 저장하는 list 생성
# 숫자 범위 생성해주는 내장함수: range(variation)
#  ex) range(시작번호, 끝번호+1): 1부터 50000까지의 함수
#         * 시작번호 <= X < 끝번호
# range 원소/요소 data 읽기: range 변수명[index]
# 1 ~ 50까지 홀수
num1=range(1,51,2)
print(f'num1의 개수: {len(num1)}')
print(f'1번 원소까지 빼기: {num1[1]}')
print(f'마지막 원소까지 빼기: {num1[-1]}')
print(f'0부터 5번 원소까지 빼기: {num1[0:5]}') # 출력방식: range