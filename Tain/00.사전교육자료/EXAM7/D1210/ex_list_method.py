# # list 자료형 전용 함수 즉, method
# [8] 원소를 꺼내주는 기능 method: pop()
# - 기본: 가장 마지막에 입력된 원소를 꺼내기(기존 list에는 꺼낸 원소 나머지 원소 존재)
# - 선택: 원하는 index 번호 지정해서 꺼내기
datas=['해바라기','겨울','스위스','사과']
print(datas.pop())
print(f'1번 요소 꺼내기: {datas.pop(1)}')
datas=[1,2,3,4]
print(datas.pop())
# [9] list 안에 데이터가 몇개 존재하는지 카운팅: count(##)
num=[1,3,8,2,3,5,1,3]
print(f'데이터 3이 몇개 존재하는지: {datas.count(3)}')
print(f'데이터 a이 몇개 존재하는지: {datas.count("a")}')
# [10] list를 확장 즉, 여러개 원소 추가: extend(list)
num=[1,3,8,2,3,5,1,3]
num.extend([11,22,33])
print(f'num의 개수: {len(num)}')
# [11] list에 모든 원소 삭제: clear()
num.clear()
print(f'num의 개수: {len(num)}')
# del함수 활용 가능: del num[:]