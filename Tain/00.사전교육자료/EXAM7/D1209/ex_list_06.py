# list 자료형과 method
# - list data type 전용의 함수
# - list 변수명.method()
# [1] 빈 리스트(empty list) 생성
nums=[]
# nums[0]=2025 * 오류
# [2] list 원소 추가하기: append() method 사용
nums.append(10)
print(f'nums 원소개수: {len(nums)}개, {nums}')
nums.append(10)
nums.append('Good')
nums.append(10)
print(f'nums 원소개수: {len(nums)}개, {nums}')
nums.append(['ABC','DEF'])
print(f'nums 원소개수: {len(nums)}개, {nums}')
# [3] list의 지정하는 위치에 원소 추가하기(삽입): insert() method 사용
nums.insert(0,'first')
print(f'nums 원소개수: {len(nums)}개, {nums}')
nums.insert(-1,'first') # -1자리에 삽입, 전에 있던 -1 index는 뒤로 밀림
print(f'nums 원소개수: {len(nums)}개, {nums}')
# [4] list의 원소 인덱스 찾기: index() method 사용
print(f'first의 index의 위치: {nums.index("first",1)}') # 첫번째 순서 이후 first 찾아줘
print(f'first의 index의 위치: {nums.index(10)}')
# print(f'ㅋ의 index 위치:{nums.index("ㅋ")} ') * 오류발생
nums_index=nums.index(10)+1
print(f'10의 첫번째 index의 위치: {nums.index(10)}')
nums_index=nums.index(10)+1
print(f'10의 두번째 index의 위치: {nums.index(10,nums_index)}')