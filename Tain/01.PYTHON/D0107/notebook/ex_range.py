# range 객체
# - 기능: 숫자의 범위 생성
# - 형식: range(숫자): 0 <= X < 숫자
#         range(숫자1, 숫자2, (1)): 숫자1 <= X < 숫자2
# - 원소/요소: indexing, slicing 가능
# 1 ~ 100까지 List 생성
nums=range(1,11)
print(nums, type(nums))
print(nums[:9])
print(f'{nums}을 list로 형 변환: {list(nums)}')
# 0 ~ 100까지 List 생성
nums=range(101)
# 순서있는 데이터 타입 즉, sequence 타입의 특징
# min(),max(),sum() 가능
print(f'{nums}의 최대값: {max(nums)}')
print(f'{nums}의 최소값: {min(nums)}')
print(f'{nums}의 합계: {sum(nums)}')

# 연산: 덧셈, 곱셈, 멤버연산자
r1=range(1,6)
r2=range(10,16)
# 덧셈 및 곱셈활용, range type을 list롤 형 변환하여 연산 진행
print(f'{r1} + {r2} = {list(r1)+list(r2)}')
print(f'{r1}*6 = {list(r1)*6}')
print(f'17 in {r2} = {17 in r2}')
print(f'17 not in {r2} = {17 not in r2}')

# 1 ~ 100범위에서 3의 배수로만 구성된 데이터
nums=range(3,100,3)
print(list(nums))