# lst 데이터 type
# - 여러개의 다양한 type 데이터를 저장하는 자료형input() -> 키보드로 입력받기
# - 형식: [데이터, 데이터1,...]
# - 특징: [] 안에 있는 데이터를 원소(요소)라고 함
#         원소/요소를 식별하기 위해서 indexing 사용
# [1] 3개 과목 점수를 저장하기
score=[90,80,60] 
print(f'score type:{type(score)}')
print(f'score 원소 개수:{len(score)}개')
print(f'score data:{score}')
# list에서 특정 원소 데이터만 가져오기
score1=score[0]
print(score1)
# list에서 일부 원소 데이터만 가져오기: slicing
print(score[:2])