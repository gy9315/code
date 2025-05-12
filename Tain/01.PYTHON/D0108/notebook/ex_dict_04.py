# dict 자료형 전용 함수 즉, method
data={'name':'홍길동','age':20,'gender':'남','job':'의적'}
# [6] dict에서 여러개 추가해주는 method: update()
data['name']='Hong' # 값 변경
data['phone']='010-2222-1111' # 값 추가
# str타입 key에는 '' or " "붙이지 않음
# update()는 str타입만 key만 입력 받음
data.update(name='마징가',phone='010-1111-2222')
print(data)
# 내장함수 zip([],[],[],...): index끼리 묶음
result=zip([1,2,3],['a','b','c'],[100,200,300])
print(list(result))
# update() 사용 시 zip()활용도 높음
data.update(zip(['A','B','C'],[100,200,300]))
print(data)
# [7] dict에서 원소/요소 꺼내기 method: pop(키), popitem()
print(data.pop('name'))
print(data)

print(data.popitem())
print(data)
# [8] dict에서 모든 원소/요소 삭제
data.clear()
print(data)
