# Set 자료형 전용함수 즉, method
# - 형식: {d1,d2,...,dn}
# - 중복data 불허, 순서 없음
# [데이터 저장]
nums={1,3,5,7,9,1,2,3,4,5}
print(f'nums의 개수: {len(nums)}개,{nums}')
# [1] 원소/요소 추가: add()
# - 이미 존재하는 데이터 중복 저장 안함
nums.add(1)
nums.add('Good')
nums.add(9)
print(f'nums의 개수: {len(nums)}개,{nums}')
# [2] 원소/요소 제거: remove()
nums.remove(9)
nums.remove('Good')
print(f'nums의 개수: {len(nums)}개,{nums}')
# [3] 원소/요소 여러개 추가: update()
# nums.update(1,11,2,22) * 숫자는 순서를 읽을수 없기에 단독으로는 업데이트 불가
nums.update((1,11,2,22))
print(f'nums의 개수: {len(nums)}개,{nums}')
nums.update([44,55,66,4,5,6])
print(f'nums의 개수: {len(nums)}개,{nums}')
nums.update('happy') # h,a,p,y를 각각 원소로 봄
print(f'nums의 개수: {len(nums)}개,{nums}')
# ------------------------------------------------------------------------
# 집합관련 method
n2=set(range(2,51,2))
n3=set(range(3,51,3))
print(f'n2의 개수: {len(n2)}')
print(f'n2의 개수: {len(n3)}')
# [1] 합집합: or 연산자 |, union()
result=n2|n3
result1=n2.union(n3)
print(f'합집합1의 개수: {len(result)}')
print(f'합집합2의 개수: {len(result1)}')
# [2] 교집합: and 연산자 %, intersection()
result=n2&n3
result1=n2.intersection(n3)
print(f'교집합1의 개수: {len(result)}')
print(f'교집합2의 개수: {len(result1)}')
# [3] 차집합: 연산자 -, difference()
result=n2-n3
result1=n2.difference(n3)
print(f'차집합1(n2-n3)의 개수: {len(result)}')
print(f'차집합2(n2-n3)의 개수: {len(result1)}')
result=n3-n2
result1=n3.difference(n2)
print(f'차집합1(n3-n2)의 개수: {len(result)}')
print(f'차집합2(n3-n2)의 개수: {len(result1)}')
