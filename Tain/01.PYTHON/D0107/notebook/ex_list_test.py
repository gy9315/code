# List 자료형 살펴보기
# [실습] 중간고사 점수를 입력 받아서 저장하기
# - 5과목: 1개 변수로 저장하기
score_list=[]
score=input('5과목 점수 입력:')
for x in score.split(','):
    score_list.append(int(x.strip()))
print(f'list: {x}, 합계: {sum(score_list)} 평균: {sum(score_list)/len(score_list)}')                              