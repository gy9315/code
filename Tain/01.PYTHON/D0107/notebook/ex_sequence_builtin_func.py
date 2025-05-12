# list 자료형과 내장함수
# - 원소/요소를 인덱스로 식별 => 순서있는 자료형(sequence type)
# [1] 원소/요소 갯수: len()
nums=[55,22,11,34,0,66]
names=['홍','박','이']
print(f'nums의 원소 개수: {len(nums)}')
print(f'names의 원소 개수: {len(names)}')
# [2] 원소/요소 최대/최소 원소: max()/min()
print(f'nums의 최대/최소 원소: {max(nums)}/{min(nums)}')
print(f'nams\es의 최대/최소 원소: {max(names)}/{min(names)}')
# [3] 원소/요소 총 합계: sum() * 수치타입만 가능
print(f'nums의 총 합계: {sum(nums)}')
## 평균
print(f'nums의 평균: {sum(nums)/len(nums)}')
# [4] 원소/요소 정렬하는 내장 함수: sorted()
print(f'nums를 오름차순으로 정렬: {sorted(nums)}')
print(f'nums를 내림차순으로 정렬: {sorted(nums,reverse=1)}')
# str 타입데이터의 정렬
msg="Happy"
print(f'{msg}의 오름차순: {sorted(msg)}')
nums=[55,22,11,34,0,66]
# 원소/요소 삭제: del
del nums[0]
print(nums)