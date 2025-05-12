# 1
## 1-1
data='Happy New Year 2022' 
data=data.replace('2022','2023')
## 1-2
msg='christmas'
msg=msg.upper()
## 1-3
phone_number='010-1111-2222'
print(phone_number.replace('-',''))
## 1-4
count='5,969,782,550'
print(f'{int(count.replace(',',''))}, {type(int(count.replace(',','')))}')
## 1-5
msg='산토끼 토끼야 어디를 가느냐 폴짝 폴짝 뛰면서 어디를 가느냐'
print(msg.count('어디를'))
## 1-6
msg='1,234,567,890'
msg=msg.split(',')
## 1-7
msg='koko@naver.com'
print(msg.find('@'))
## 1-8
msg="                  오늘은 날씨가 너무 좋군요!!    "
print(f'문자의 길이: {len(msg.strip())}')
# ------------------------------------------------------
# 2
print('{:^15}'.format('*'))
print('{:^15}'.format('*'*3))
print('{:^15}'.format('*'*5))
print('{:^15}'.format('*'*7))
print('{:^15}'.format('*'*9))
print('{:^15}'.format('*'*11))
print('{:^15}'.format('*'*13))
print('{:^15}'.format('*'*15))
print('{:^15}'.format('*'*4))
print('{:^15}'.format('*'*4))
print('{:^15}'.format('Merry Chrismas'))
print('{:^15}'.format('2025'))
# --------------------------------------------
for s in range(12):
    if s<=7:
       print('{:^15}'.format("*"*(2*s+1)))
    if 8<=s<10: print('{:^15}'.format("*"*4))
    if s==10: print('{:^15}'.format('Merry Christmas'))
    if s==11: print('{:^15}'.format('2025'))
# ------------------------------------------------------
# 3
# 3-1
data=input('숫자 2개를 입력하시오(예: 1,2):')
data1=int(data.split(',')[0].strip())
data2=int(data.split(',')[1].strip())
print(f'{data1} + {data2} = {data1+data2} ')
print(f'{data1} - {data2} = {data1-data2} ')
print(f'{data1} * {data2} = {data1*data2} ')
print(f'{data1} / {data2} = {data1/data2} ')
## 3-2
data=input('좋아하는 단어를 입력해주세요:')
print(data.upper())
print(f'"a"가 있는지 여부: {"a" in data}')
# 3-3
data='가나*마바사*자***파하'
print(f'첫 번째 "*"의 index: {data.find('*')}')
print(f'세 번째 "*"의 index: {data.find("*",data.find("*",data.find("*")+1)+1)}')
# 3-4
msg='Hello'
print(msg[::-1])