# tuple type
# - 변경되면 안되는 데이터 저장용 type
# - [다른언어] 변경 불가 데이터 저장 문법 있음: 상수
# - 형태: (데이터, 데이터, ..) 또는 데이터, 데이터, 데이터  또는 (데이터,) 또는 데이터,
# [1] tuple instance 생성
# 3사람의 혈액형 저장
blood=('a','o','ab')
blood2='a','o','ab'
blood_1='a',
blood_2='a'
blood_3=('a')
print(f'blood type: {type(blood)}')
print(f'blood 개수: {len(blood)}')
print(f'blood2 type: {type(blood2)}')
print(f'blood2 개수: {len(blood2)}')
print(f'blood_1 type: {type(blood_1)}')
print(f'blood_2 type: {type(blood_2)}')
print(f'blood_3 type: {type(blood_3)}')
# [2] tuple 원소/요소 읽기
print(f'첫번째 원소 읽기: {blood[0]}')
print(f'0 ~ 1번 원소 읽기: {blood[0:2]}')