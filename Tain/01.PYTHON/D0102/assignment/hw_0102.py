# 값을 정수로 만들기
print(int(3.3))
print(int(5/2))
print(int('10'))
# 값을 실수로 만들기
print(float(5))
print(float(1+2))
print(float('5.3'))
# --------------------------------------------
# 비교 연산자의 판단 결과
print(3>1)
# 숫자가 같은지 다른지 비교하기
print(10==10)
print(10!=5)
# 문자열이 같은지 다른지 비교하기
print('Python'=='Python')
print('Python'=='python')
print('Python'!='Python')
# 부등호 사용하기
print(10>20)
print(10<20)
print(10>=20)
print(10<=20)
# 객체가 같은지 다른지 비교하기
print(1==1.0)
print(1 is 1.0)
print(1 is not 1.0)
# p.89 값 비교에 is 쓰지 않기(vscode와 python 값의 결과가 다름)
a=-6
print(a is -6)
a=-5
print(a is -5)
# 논리 연산자 사용하기
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not False)
print(not True)
# not, and, or 순으로 논리 연산
print(not False and False or True)

# 논리 연산자와 비교 연산자를 함께 사용하기
print(10==10 and 10!=5)
print(10>5 or 10<3)
print(not 10>5)
print(not 1 is 1.0)
# 단락평가: 첫번째 순서부터 실시하고 첫번째 결과로 결과가 확실하다면 첫번째 값을 결과도출
#           두번째값으로 결과값이 확실해지면 두번째 갑을 결과도출
#          - 항상 논리값이 bool만 나오는 것이 아님
print(True and 'python')
print('python'or False)
# 8-4 연습문제: 합격 여부 출력하기
# 국어, 영어, 수학, 과학 / 한 과목이라도 50점 미만이면 불합격
kor=92
eng=47
math=86
sci=81
print(sci>=50 and kor>=50 and math>=50 and eng>=50)
# 8-5 연습문제: 합격 여부 출력하기
# 국어, 영어, 수학, 과학 점수 입력, 국어 90점 이상, 영어 80초과, 수학 85초과, 과학 80이상
# - 단 한과목이라도 조건에 만족하지 않으면 불합격
score=input()
score=score.split(' ')
kor=int(score[0])
eng=int(score[1])
math=int(score[2])
sci=int(score[3])
print(kor>=90 and eng>80 and math>85 and sci>=80)