# tuple 자료형
# - 특징: 여러 종류의 여러 개의 데이터 저장 가능
#         단, 저장 후 수정/변경/삭제/추가 불가!
# - 활용: 변경이 되지말아야할 데이터를 저장 시 사용
# tuple 생성
data=()
data1=('f')
data2=(10,'GOOD')
data3=[15,5,7,412,'DOG']
# 타입, 원소 갯수 출력
print(f'{data}의 type: {type(data)}');print(f'{data1}의 type: {type(data1)}')
print(f'{data2}의 type: {type(data2)}')
# 원소/요소 읽기: 변수명[인덱스] 
print(data2[0])
# ---------------------------------------------------
# 원소/요소 값 변경: 변수명[인덱스]=새로운 값
# - list인 경우
data3[0]='백'
print(f'list, {data3}')

# ---------------------------------------------------
# - tuple인 경우
#   data2[0]='백'-------------------> 변경 불가
#   print(f'tuple, {data2}')
# ---------------------------------------------------

# 원소/요소 삭제: del 요소
# - tuple인 경우
#   del data2[0] -------------------> 변경 불가
#   print(data2)

# 반드시 변경이 필요한 경우: list 형 변화 후 -> 다시 tuple 형 변환 시행
data=('F','Park')
# 성별을 F에서 M으로 변환 필요
data=list(data)
data[0]="M"
data=tuple(data)
print(data)