# dict 자료의 전용 함수 즉, method
# [4] 특정 key에 해당하는 value 읽어오는 method: get(key)
# - 형식1: get(key) dict에서 key에 해당하는 value 반환
# - 형식2: get(key,default) dict에서 key가 없은 경우에 돌려줄 결과 설정 
flowerdict={'장미':3000, '백합':4500,'데이지':2900}
# 백합의 가격
print(flowerdict['백합'], flowerdict.get('백합'))
# print(flowerdict['해바라기']) * keyerror
# get(key) method는 dict에 key가 없을 경우 표현방식을 정할 수 있음
print(flowerdict.get('해바라기','없음'))
# -----------------------------------------------------------------
# [5] 모든 원소 삭제 method: clear()
flowerdict.clear()
print(f'flowerdict의 개수: {len(flowerdict)}')
# [6] 여려개의 value를 변경 method: update()
flowerdict['백합']=5500
flowerdict['목련']=6200
flowerdict.update({'목련':6700,'해바라기':5000,'수국':10000})
print(flowerdict)
# update(key=value,...) key는 문자 or 숫자 따음표 X, value는 문자일 경우 따음표 O
flowerdict.update(목련=6400,해바라기=10000,수국=10000)
print(flowerdict)