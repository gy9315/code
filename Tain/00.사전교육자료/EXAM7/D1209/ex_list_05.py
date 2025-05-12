# # list 데이터 type 특징-연산자
# - 덧셈: list+list: 두개 리스트 원소 합쳐진 새로운 리스트
# - 곱셈: list*list: 정수만큼 원소 반복
# - 멤버 연산: in list, not in list: list 원소 존재 여부(T/F)
# [1] 덧셈연산자
nums=[1,3,5,7,9]
datas=['a','b','c']
print(f'nums+datas: {nums+datas}')
# [2] 곱셈연산자
print(f'nums*3: {nums*3}')
# [3] 곱셈연산자
print(f'A in nums: {"A" in datas}')
print(f'a in nums: {"a" in datas}')