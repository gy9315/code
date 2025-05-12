# list 자료형과 method
# - list data type 전용의 함수
# - list 변수명.method()
# [5] 원소 삭제 method: remove()
nums=[1,2,3,1,4,1,5]
nums.remove(1)
print(f'원소 "1"을 제거: {nums}')
# [6] 원소를 역순으로 변경해주는 method: reverse()
nums=[1,2,3,1,4,1,5]
nums.reverse()
print(f'list의 원소를 역순으로 정리: {nums}')
# [7] 원소를 정렬해주는 method: sort()
nums.sort() # 오름차순, 변경 후 재 저장
print(f'정렬 전 list -> 정렬 후 list: {nums}')
nums.sort(reverse=1) # 내림차순
print(f'정렬 전 list -> 정렬 후 list: {nums}')
nums.pop()
print(nums)