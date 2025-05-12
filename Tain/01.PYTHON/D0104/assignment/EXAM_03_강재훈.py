# 1
home='Jeju'
type='B'
ssn='Fall'
tall=182.3
pi=3.141592
ctr='Korea'
# 2
num=int(input('궁금한 구구단:'))
for data in range(1,10):
    print(f'{num} * {data} = {num*data}')
# 3
num=31
float(num)
num_float=float(num)
msg=2022
str(msg)
msg_str=str(msg)
float=98.1
int(float)
float_int=int(float)
str(msg)
msg_str=str(msg)
# 4
## 4-1
num='881120-1068234'
print(num[:7], num[8:])
print(num.split('-')[0],num.split('-')[1])
## 4-2
str_1='a:b:c:d'
print(str_1[::2])
# ------------------------------------
str_2=''
for data in str_1.split(':'):
    str_2=str_2+data
print(str_2)
# ------------------------------------
print(''.join(str_1.split(':')))
## 4-3
msg='에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.'
price=int(msg[7:9]+msg[10:13])
mon=int(msg[20:22])
total=str(price*mon)
print(f'에어컨 금액: {total[0]},{total[1:4]},{total[4:]}원')
# ----------------------------------------------------------------------------
msg='에어컨이 월 1,148,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.'
str=str(int(msg[msg.find('자')+1:msg.find('개월')].strip())*int(msg[msg.find('월')+1:msg.find('원')].strip().replace(',',"")))
str_num=''
if len(str)>5:
    if len(str)%3:       
        for data in range(1,(len(str)//3)+1):
            str_num=','+str[-(3*data):len(str)+3-3*data]+str_num
        str_num=str[0:len(str)%3]+str_num
    else:
        for data in range(1,int(len(str)/3)): 
            str_num=','+str[-(3*data):len(str)+3-3*data]+str_num
        str_num=str[:3]+str_num
elif 3<len(str)<6: str_num=str[:-3]+','+str[-3:]
else: str_num=str
print(f'에어컨 금액: {str_num}원')
# ---------------------------------------------------------------------------
# 4-4
msg='가로 10cm, 세로 11cm인 직사각형 넓이 계산'
x=int(msg[3:5])
y=int(msg[12:14])
z=x*y
print(f'직사각형 넓이 : 가로 {x} X 세로 {y} = {z}')
# 5 
## 5-1
path=r'"C:\User\Public\kyobo\eLibrary\B2C\edir.info"'
print(path)
## 5-2
a=9
b=-5
c=100
d=0
e=72
print(f'가장 큰 값: {max(a,b,c,d,e)}')
print(f'가장 작은 값: {min(a,b,c,d,e)}')
print(f'절대값: {abs(a)} {abs(b)} {abs(c)} {abs(d)} {abs(e)}')
## 5-3
data="오늘은 \"2025년 1월 1일 새해\"입니다."
print(data)
## 5-4
data='   하늘과 바람과 별과 시\n\n\t서시(序詩)\n\t\t   윤동주\n\n죽는 날까지 하늘을 우러러\n한 점 부끄럼이 없기를,\n잎새에 이는 바람에도\n나는 괴로워했다.\n별을 노래 하는 마음으로\n모든 죽어가는 것을 사랑해야지\n그리고 나한테 주어진 기을\n걸어가야겠다.\n\n오늘 밤에도 별이 바람에 스치운다.'
print(data)