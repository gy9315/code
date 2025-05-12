# 가변인자 함수
# # ----------------------------------------------
# 기능: 0개 ~ n개 정수 덧셈 화면 출력
# 함수이름: plus
# 변수: *num
# 결과: 화면 출력으로 반환값

def plus(*nums):
    print(type(nums))

plus(3,4,5)
plus()
plus(100)
# 키워드 파리미터 함수
# 개수: 0개 ~ n개 인자 
# 형태: def 함수명(**매개변수)
# 변수: *num(0개 ~ n개 인자)
# 타입: dict
# ----------------------------------------------------------
# [실습] 중간고사 3과목 점수에 대한 합계와 평균을 출력하는 함수
# 기능: 3과목에 대한 합계/평균 출력 
# 이름: score_sum_avg
# 변수: score1,score2,score3
# 결과: 합계와 평균균

def score_sum_avg(score1,score2,score3):
    sum1=score1+score2+score3
    avg=sum1/3
    return sum,avg
# [실습] 중간고사 n과목 점수에 대한 합계와 평균을 출력하는 함수
# 기능: 3과목에 대한 합계/평균 출력 
# 이름: score_sum_avg2
# 변수: *score1
# 결과: 합계와 평균균

def score_sum_avg2(*score):
    sum1=sum(score)
    avg=sum1/len(score) if len(score) else 0
    return sum1,avg

print(score_sum_avg2(1,2,3))
# [실습] 과목별 점수를 0 ~ n개 합계와 평균을 출력하는 함수
# 기능: 과목별 점수에 대한 합계/평균 출력 
# 이름: score_sum_avg3
# 변수: **score1
# 결과: 합계와 평균
def score_sum_avg3(**jumsu):
    print(type(score_sum_avg3))

score_sum_avg3()
score_sum_avg3(kor=90,math=100)
score_sum_avg3(music=99,art=100,kor=98,eng=99,math=100)
# -------------------------------------------------------
# dict 타입으로 변환환
dict_={}
dict_.update(music=99,art=100,kor=98,eng=99,math=100)
x=dict(music=99,art=100,kor=98,eng=99,math=100)
print(dict_.items())
print(dict_)
print(x)
x1=('강재훈',2),('바보',4),('바보1',6)
print(dict(x1))
x2=()
list3=tuple(['바보=1'])
print(list3)
list1=[1,2]
list2=[12,23]
# --------------------------------------------------
print(dict([tuple(list1),tuple(list2)]))
# --------------------------------------------------
dict_1=dict(zip(list1,list2))
print(dict_1)
print(list(dict_1))