# dict 자료형 실습
# [데이터] 아이스크림 가격을 저장합니다.
icedict={'메로나':1500,'월드콘':1200,'국화빵':2500}
# 내가 찾는 아이스크림 존재 여부 확인
print(f'내가찾는 아이스크림 존재여부:{"내가찾는 아이스크림"in icedict}')
# 내가 찾는 가격 존재 여부 확인
print(f'내가찾는 가격 존재여부:{2000 in icedict.values()}')
# 좋아하는 아이스크림 이름과 구매 수량 입력 받가
# 총 구매금액 출력하기
ice_dict=input('예시) 아이스크림과 수량:')
ice_dict=ice_dict.split(' ')
print(f'총 금액: {icedict.get(ice_dict[0])*int(ice_dict[1])}')


