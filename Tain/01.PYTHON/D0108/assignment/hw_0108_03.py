# [1]
## 1-1
jumsu={'국어':98,'음악':71,'미술':90,'체육':82,'과학':88}
s=list(jumsu.values())
print(f'총 합계: {sum(s)}, 평균: {sum(s)/len(s)}')
## 1-2
msg={"김연아":"피겨스케이팅", "류현진":"야구 ", "박지성":"축구", "귀도":"파이썬"}
print(f'키: {msg.keys()} 값: {msg.values()}, 키와 값: {msg.items()}')
## 1-3
num1=input('이름, 전화번호 입력:')
num2=input('이름, 전화번호 입력:')
num1=num1.split(',')
num2=num2.split(',')
person={num1[0]:num1[1],num2[0]:num2[1]}
# person1=dict(num1[0]:num1[1],num2[0]:num2[1]) 
print(person)
# ## 1-4
food={'한식':'불고기','중식':'자장면','일식':'스시'}
print(food['한식']);print(food['일식'])
## 1-5
food={'한식':'불고기','중식':'자장면','일식':'스시'}
food1=input('좋아하는 나라식사와 음식을 입력해주세요:(예: 한식,비빔밥)')
food1=[x.strip() for x in food1.split(',')]
food[food1[0]]=food1[1]
print(food)
## 1-6
msg={"김연아":"피겨스케이팅", "류현진":"야구 ", "박지성":"축구", "귀도":"파이썬"}
msg['손흥민']='축구'
msg=list(msg.items())
msg.sort(key=lambda x:x[0])
print(msg)
msg=dict(msg)
print(msg)
## 1-7
list_=[]
tuple=()
dict={}
set=set()
str=''
int=0
## 1-8
student={'배트맨':{'국어':90,'수학':89,'윤리':98,'국사':99},'마징가':{'국어':82,'수학':71,'윤리':80,'국사':91},'슈퍼맨':{'국어':77,'수학':100,'윤리':92,'국사':90},'슈렉':{'국어':94,'수학':82,'윤리':93,'국사':71}
         ,'피오나':{'국어':78,'수학':99,'윤리':91,'국사':83}}
# 과목별 최고점수
# 값가져오기 / 값가져오기[0] ~ [3]까지 비교
# if 함수 사용하여 값비교 진행해보기기
list0=[list(list(student.values())[y].values())[0] for y in range(5)]
list1=[list(list(student.values())[y].values())[1] for y in range(5)]
list2=[list(list(student.values())[y].values())[2] for y in range(5)]
list3=[list(list(student.values())[y].values())[3] for y in range(5)]
num=[1,2,3,4,5]
print(max(list1))
print(f' [국어] 최대/최소점수: {max(list0)}/{min(list0)}, [수학] 최대/최소점수: {max(list1)}/{min(list1)}, [윤리] 최대/최소점수: {max(list2)}/{min(list2)}, [국사] 최대/최소점수: {max(list3)}/{min(list3)}')

## 1-9
msg='Good Luck'
msg=msg.upper()
msg=list(msg)
msg.sort()
print(msg)
## 1-10
num2=range(2,51,2)
num5=range(5,51,5)
num7=range(7,51,7)
num=list(num2)+list(num5)+list(num7)
num.sort()
print(num)