# 1
msg='Hello World'
print(msg)
# 2
msg="Marry's cosmetics"
print(msg)
# 3
msg='''신씨가 소리질렀다. "도둑이야"'''
print(msg)
# 4
msg=r'c:\Window'
print(msg)
# 5
## \n은 줄바꿈 이스케이프 문자, \t tab 이스케이프 문자
# 6
## 오늘은 일요일
# 7
print('naver;kakao;sk;samsung')
# 8
print('naver/kakao/sk/samsung')
# 9
print("fisrt",end=' ');print("second")
# 10
print(5/3)
# 11
삼성전자='50,000원'
price=삼성전자[:2]+삼성전자[3:-1]
total=10*int(price)
print(total)
# 12
total='298조'
price='50,000원'
per=15.79
# 13
s='Hello'
t='python'
print(f'{s}! {t}')
# 14
## 8
# 15
a='132'
print(f'{a}의 type: {type(a)}')
# 16
num_str="720"
num_str=int(num_str)
# 17
num=100
num=str(num)
# 18
str='15.79'
str_float=float(str)
# 19
year='2020'
print(int(year),int(year)+1,int(year)+2)
# 20
msg='에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.'
price=int(msg[7:9]+msg[10:13])
mon=int(msg[20:22])
total=price*mon
print(f'에어컨 금액: {total}원')
# 21
letters='python'
print(letters[0],letters[2])
# 22
license_plate='24가 2210'
print(license_plate[-4:])
# 23
str='홀짝홀짝홀짝'
print(str[::2])
# 24
string='PYHTHON'
print(string[-1]+string[-2]+string[-3]+string[-4]+string[2]+string[1]+string[0])
print(string[::-1])
# 25
phone='010-1111-2222'
print(phone[:3],phone[4:8],phone[9:])
# 26
phone='010-1111-2222'
print(phone[:3],phone[4:8],phone[9:],sep='')
# 27
url="http://sharebook.kr"
print(url[-2:])
# 28
## ERROR
# 29
str='abcdfe2a354a32a'
str='A'+str[1:7]+'A'+str[8:11]+'A'+str[12:14]+'A'
print(str)
str='abcdfe2a354a32a'
str=str.replace('a','A')
print(str)
# 30
## aBcd
# 31
## 34
# 32
## HiHiHi
# 33
print('-'*80)
# 34
t1='python';t2='java'
print((t1+' '+t2+' ')*4)
# 35
name1='김민수'
age1=10
name2='이철희'
age2=13
print('이름: %s  나이: %d' %(name1,age1) )
print('이름: %s  나이: %d' %(name2,age2) )
# 36
print('이름: {}  나이: {}' .format(name1,age1) )
print('이름: {}  나이: {}' .format(name2,age2) )
# 37
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')
# 38
msg='5,969,782,550'
msg=int(msg[0]+msg[2:5]+msg[6:9]+msg[10:])
print(int(msg))
msg='5,969,782,550'
msg1=''
for data in msg.split(','):
    msg1=msg1+data
print(int(msg1))
msg='5,969,782,550'
msg=msg.replace(',','')
print(int(msg))
# 39
s='2020/03(E) (IFRS연결)'
print(s[:7])
# 40
data="    삼성전자     "
data1=data[4:8]
print(data1)
data2=data.strip()
print(data2)

