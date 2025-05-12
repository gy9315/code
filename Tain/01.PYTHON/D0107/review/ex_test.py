num='1234567'
print(num.rjust(10))
print(format(int(num),','))
print('%-10s'%'바보')
print('{:x^10}'.format('바보'))
print('%10.2f'%10)
num=', python.'
print(num.strip(',.'))
import string
num=', python.;abcd'
import string
print(num.strip(string.punctuation))
num='123123'
print(num.find('1',4))
msg='2023년은 토끼해입니다. 2024년은 무슨 해 인가요? 나는 2024년이 기다려집니다.'
num1=msg[msg.find('2023'):len('2023')]
num2=msg[msg.find('2024'):msg.find('2024')+len('2024')]
num3=msg[msg.find('2024',msg.find('2024')+1):msg.find('2024',msg.find('2024')+1)+len('2024')]
print(num3)
## 3-2
num8=range(8,51,8)
num3=range(3,51,3)
num=list(num8)+list(num3)
print(f'최대값: {max(num)}, 최소값: {min(num)}, 합계: {sum(num)}, 평균: {sum(num)/len(num)} ')
add=lambda  x,y:x+y
print(add(1,2))
num=123.1234566
print(round(num),round(num,0))
print('{:10.2f}'.format(num))
print('%10.2f'%num)
print('%10.2f'%num)
print(f'{num:10.2f}')
# ----------------------------------------------
add=lambda x=int: '합격' if x>=60 else '불합격'
print(add(3))
data='3'
data1='5'
print(data.isdecimal()&data1.isdecimal())