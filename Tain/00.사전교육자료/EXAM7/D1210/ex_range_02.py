# [데이터생성] 1 ~ 50000까지 숫자를 저장하는 list 생성
# 숫자 범위 생성해주는 내장함수: range(variation)
#  ex) range(시작번호, 끝번호+1): 1부터 50000까지의 함수
#         * 시작번호 <= X < 끝번호
# [1] 값이 0부터 시작하는 경우의 range(,끝번호+1)
nums=range(11)
print(nums)
# [2] 값이 1 ~ 10에서 짝수만 범위를 나타내는 경우
nums=range(2,11,2)
print(list(nums))
