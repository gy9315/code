# [1]
## 1-1
jumsu=[98,71,90,82,88]
## 1-2
msg='Good Luck Happy New Year'
msg=msg.split()
print(f'msg의 개수: {len(msg)}, 데이터: {msg}')
## 1-3
score_list=[]
score=input('중간고사 5과목 점수를 순서대로 입력해주세요(예: 1,2,3,4,5):')
score_list.append(int(score.split(',')[0].strip()))
score_list.append(int(score.split(',')[1].strip()))
score_list.append(int(score.split(',')[2].strip()))
score_list.append(int(score.split(',')[3].strip()))
score_list.append(int(score.split(',')[4].strip()))
print(score_list)
## 1-4
list_=[1,3,5,7,9,11]
list_.extend([13,15])
print(list_)
## 1-5
list_=[1,3,5,7,9,11]
list_.pop(5)
## 1-6
fruits=['kiwi','banana','orange','apple']
fruits.sort(reverse=1)
## 1-7
list_=[1,2,3,4,5,6]
list_.clear()
## 1-8
msg=['가나다','한글','가방','국가','쏘핫']
print(f'msg 최대값: {max(msg)}')
print(f'msg 최소값: {min(msg)}')
print(f'msg 개수(길이): {len(msg)}')
# ------------------------------------------------------------------
# 2
## 2-1
data="hello@naver.com"
msg='123ABC'
print(len(data.split('@'))==2 and '.com' in data)
print(data.isalpha())
print(msg.isnumeric())
print(msg.isalnum())
print(msg.isspace())
## 2-2
msg='!@Happy a Good Day~^^'
print(f'{msg} 시작 "!@": {msg.startswith("!@")}')
print(f'{msg} 끝 "^^": {msg.endswith("^^")}')
## 2-3
msg='2023년은 토끼해입니다. 2024년은 무슨 해 인가요? 나는 2024년이 기다려집니다.'
num1=msg[msg.find('2023'):len('2023')]
num2=msg[msg.find('2024'):msg.find('2024')+len('2024')]
num3=msg[msg.find('2024',msg.find('2024')+1):msg.find('2024',msg.find('2024')+1)+len('2024')]
print(int(num1)+int(num2)+int(num3))
