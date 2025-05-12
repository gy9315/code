# 중간고사 5과목 입력받아서 저장하기
score=input('3과목 점수 입력(국어, 영어, 수학):')
scorelist=[['국어,'],['영어,'],['수학,']]
for data in  score.split(','):
    scorelist[score.split(',').index(data)].append(int(data))
print(scorelist)
