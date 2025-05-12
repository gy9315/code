# dict 자료형 전용 함수 즉, method
data={'name':'홍길동','age':20,'gender':'남','job':'의적'}
# [1] dict에서 키만 추출 해주는 method: values()
## memory절약을 위해서 단순 바로가기용으로 생성
print(data.keys(), type(data.keys()))
data_keys=data.keys()
## dict_keys 타입을 list 타입으로 형 변환
print(list(data_keys), type(list(data_keys)),list(data_keys)[0])
# -------------------------------------------------------------------
# [2] dict에서 값만 추출 해주는 method: values()
print(data.values(), type(data.values()))
data_values=data.values()
# dict_values 타입을 list 타입으로 형 변환
print(list(data_values), type(list(data_values)),list(data_values)[0])

# [3] dict에서 키와 값을 tuple로 추루 해주는 method: items()
items=data.items()
print(items, type(items))

# [4] dict에서 키로 값 추출해주는 method: get(key)
# 존재하는 Key는 value추출
print(data['name'],data.get('name'))
# 존재하지 않는 key는 :key ERROR
# print(data.get('phone'))
# ---------------------------------------------------- 
## 검색에서 사용
print(data.get('phone', '존재하지 않습니다.'))
print(data.get('phone',0))
print(data.get('phone',-1))

# [5] 멤버연산자 in/not in: 모든 기준=key
# Key
print(f'name in data: {"name" in data}')
print(f'job in data: {"job" in data}')
# value
print(f'남 in data: {"남" in data}')