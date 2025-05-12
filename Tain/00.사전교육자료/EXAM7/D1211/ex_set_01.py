# Set 자료형
# - 형식: {d1,d2,...,dn}
# - 중복data 불허, 순서 없음
# [1] 생성
flowername={'해바리기', '백함','장미', '안개꽃','장미','백합','장미'}
names=['해바리기', '백함','장미', '안개꽃','장미','백합','장미']
print(f'names-> {len(names)}개, {names}')
print(f'flowername-> {len(flowername)}개, {flowername}')
print(f'flowername-> {type(flowername)}')
# [2] 생성
data=[]
data1=()
data2={}
data3=set()
print(f'data의 type: {type(data)}')
print(f'data1의 type: {type(data1)}')
print(f'data2의 type: {type(data2)}')
print(f'data3의 type: {type(data3)}')
print(f'data의 개수: {len(data)}개')
print(f'data1의 개수: {len(data1)}개')
print(f'data2의 개수: {len(data2)}개')
print(f'data3의 개수: {len(data3)}개')
# [3] 생성
# datas={'Good',1234,False,{'name':'hong','age':10}} * 수정 type은 불가
# datas={'Good',1234,False,['hong','age']} * 수정 type은 불가
datas={'Good',1234,False,range(1,51)}
print(range(1,51))
print(datas)
datas={'Good',1234,False,('hong','age')}
print(datas)