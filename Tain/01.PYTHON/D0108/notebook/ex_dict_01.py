# dict 자료형 살펴보기
# - 툭징: 데이터를 식별하는 키와 함께 저장
#         키로 데이터를 식별하기 떄문에 인덱스 필요 X
# - 형식: {키1:data, 키2:data, 키3:data}
# [1] dict 생성
data={}
data2={'홍길동':'대구', '마징가':'미국','베트맨':'미국','홍길동':'한양'}
data3={1:'대구', '마징가':2,'지역':'대구'}
# data3={['홍길동','대구']:'대구', ['마징가','서울']:2,'지역':'대구'}: ERROR 키는 변경불가 상태여야 함
data4={('홍길동','대구'):'대구', ('마징가','서울'):2,'지역':[90,10,30,60]}
data5={('홍길동','대구'):{'국어':30,'영어':80}, ('홍길동','서울'):{'체육':90,'미술':80}}

print(f'data {type(data)} {len(data)} {data}')
print(f'data2 {type(data2)} {len(data2)} {data2}')
print(f'data3 {type(data3)} {len(data3)} {data3}')
print(f'data4 {type(data4)} {len(data4)} {data4}')
print(f'data5 {type(data5)} {len(data5)} {data5}')