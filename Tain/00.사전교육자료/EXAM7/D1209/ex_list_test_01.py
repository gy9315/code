# list 자료형 다루기
# [실습-1] 숫자 3개를 입력받아서 빈 리스트에 저장
# 단, input은 3번 사용
num1=int(input('숫자를 입력해주세요:'))
num2=int(input('숫자를 입력해주세요:'))
num3=int(input('숫자를 입력해주세요:'))
nums=[num1,num2,num3] # append() method 사용가능
# num=[]
# num.append(num1)
# num.append(num2)
# num.append(num3)
print(type(nums))
# [실습-2] 좋아하는 과일이름을 영어로 입력 받아주세요
#          그리고 아래 조건에 맞도록 결과를 출력하세요
# - 과일이름을 대문자로 출력
# - 과일이름을 소문자로 출력
# fruit1=input('좋아하는 과일이름을 영어로 입력주세요:')
# fruit2=input('좋아하는 과일이름을 영어로 입력주세요:')
# fruit3=input('좋아하는 과일이름을 영어로 입력주세요:')
# fruits=[fruit1,fruit2,fruit3]
# print(f'대문자로 출력: {(fruit1.upper),(fruit2.upper),(fruit3.upper)}')
# print(f'소문자로 출력: {fruit1.lower,fruit2.lower,fruit3.lower}')
# [실습-3] 아래 데이터에 대한 합계와 평균을 출력하세요
# - 데이터: 88, 66, 99, 77
# - 데이터는 한개의 변수명으로 저장
# - 출력형태 ->  합계: 000, 평균:000
data=[88,66,99,77]
print(f'합계: {data[0]+data[1]+data[2]+data[3]}')
print(f'합계: {(data[0]+data[1]+data[2]+data[3])/len(data)}')
print(f'최소값/최대값: {min(data)}/{max(data)}')
# [실습-4] 좋아하는 문장을 입력 받은 후 아래와 같이 출력해주세요
# - 입력: 오늘은 좋은날
# - 출력1) ['오늘은','좋은날']
# - 출력2) '오눌은♥좋은날'
set=input('좋아하는 문장을 입력:')
set=set.strip()
set=set.split(' ')
print(set)
con='♥'
print(con.join(set))