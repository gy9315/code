# [1]
jumsu={'국어':98,'음악':71,'미술':90,'체육':82,'과학':88}
jumsu_values=jumsu.values()
jumsu_list=list(jumsu_values)
print(f'총합: {sum(jumsu_list)}, 평균: {sum(jumsu_list)/len(jumsu_list)}')
# [2]
sports={'김연아':'피겨스케이팅','류현진':'야구','박지성':'축구','귀도':'파이썬'}
sports_keys=sports.keys()
sports_values=sports.values()
sports_items=sports.items()
print(f'keys: {sports_keys}, values: {sports_values}, items: {sports_items}')
# [3]
person={}
user1=input('예시) 홍길동,000-0000-0000\n이름, 전화번호를 입력해주세요:')
user1=user1.split(',')
person[user1[0].strip()]=user1[1].strip()
user2=input('예시) 홍길동,000-0000-0000\n이름, 전화번호를 입력해주세요:')
user2=user2.split(',')
person[user2[0].strip()]=user2[1].strip()
print(person)
# [4]
foods={'한식':'불고기','중식':'자장면','일식':'스시'}
print(f'한식: {foods["한식"]}, 일식: {foods["일식"]}')
# [6]
sports={'김연아':'피겨스케이팅','류현진':'야구','박지성':'축구','귀도':'파이썬'}
sports['손흥민']='축구'
# [7]
student={'배트맨':{'국어':90,'수학':89,'윤리':98,'국사':99},'마징가':{'국어':82,'수학':71,'윤리':80,'국사':91},'슈퍼맨':{'국어':77,'수학':100,'윤리':92,'국사':90},'슈렉':{'국어':94,'수학':82,'윤리':93,'국사':71},'피오나':{'국어':78,'수학':99,'윤리':91,'국사':83} }
# [8]
num1=range(2,51,2)
num2=range(5,51,5)
num3=range(7,51,7)
num_list=list(num1)+list(num2)+list(num3)
num_list2=list(num1)
num_list2.extend(list(num2)+list(num3))
print(num_list)
print(num_list2)