# [31]
## 34
# [32]
## HiHiHi
# [33]
print('-'*80)
# [34]
t1 = 'python'
t2 = 'java'
t3=f'{t1} {t2}'
print(t3*3)
# [35]
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: %s 나이: %s'%(name1,age1))
print('이름: %s 나이: %s'%(name2,age2))
# [36]
print('이름: {} 나이: {}'.format(name1,age1))
print('이름: {} 나이: {}'.format(name2,age2))
# [37]
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')
# [38]
상장주식수 = "5,969,782,550"
상장주식수=int(상장주식수.replace(',',''))
# [39]
분기 = "2020/03(E) (IFRS연결)"
print(분기.split(' ')[0])
# [40]
data = "   삼성전자    ".strip()
print(data)
# [41]
ticker = "btc_krw".upper()
print(ticker)
# [42]
ticker="BTC_KRW".lower()
print(ticker)
# [43]
string="hello".capitalize()
print(string)
# [44]
file_name = "보고서.xlsx"
print(file_name.endswith('.xlsx'))
# [45]
file_name = "보고서.xlsx"
print(file_name.endswith('.xlsx') or print(file_name.endswith('.Xlx')))
# [46]
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))
# [47]
a = "hello world".split()
# [48]
ticker = "btc_krw".split('_')
# [49]
date = "2020-05-01".split('-')
a,b,c=date
# [50]
print(f'년: {a}, 월: {b}, 일:{c}')
data = "039490     ".rstrip()
print(data)
# [51]
movie_rank=['닥터 스트레인지','스플릿','럭키']
# [52]
movie_rank.append('베트맨')
# [53]
movie_rank.insert(1,'슈퍼맨')
# [54]
movie_rank.remove('럭키')
print(movie_rank)
# [55]
movie_rank.remove('스플릿')
movie_rank.remove('베트맨')
# [56]
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2
# [57]
nums = [1, 2, 3, 4, 5, 6, 7]
print(f'max: {max(nums)}')
print(f'min: {min(nums)}')
# [58]
nums = [1, 2, 3, 4, 5, 6, 7]
print(sum(nums))
# [59]
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
# [60]
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))
# [61]
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
# [62]
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[::2])
# [63]
print(price[1::2])
# [64]
nums = [1, 2, 3, 4, 5]
print(price[::-1])
# [65]
interest = ['삼성전자', 'LG전자', 'Naver']
interest.pop(1)
print(interest)
# [66]
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))
# [67]
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest))
# [68]
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('\n'.join(interest))
# [69]
string = "삼성전자/LG전자/Naver".split('/')
print(string)
# [70]
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))
# [71]
my_variable=()
# [72]
movie_rank=('닥터 스트레인지','스플릿','럭키')
# [73]
msg=1,
print(type(msg))
# [74]
## 튜플은 수정불가 단, 수정을 원할 시 리스트로 강제변환 후 가능
# [75]
t = 1, 2, 3, 4
## tuple
# [76]
t = ('a', 'b', 'c')
t=list(t)
t[0]='A'
print(tuple(t))
# [77]
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest=list(interest)
# [78]
interest=tuple(interest)
# [79]
## 각 요소마다 a,b,c가 바인딩 되어있음: apple banna cake
# [80]
msg=tuple(range(2,100,2))
print(msg)
# [81]
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,a,b=scores
print(valid_score)
# [82]
a,b,*valid_score=scores
print(valid_score)
# [83]
a,*valid_score,b=scores
print(valid_score)
# [84]
temp={}
# [85]
msg={'메로나':1000,'폴라포':1200,"빵빠레":1800}
# [86]
msg1={'죠스바':1200,'월드콘':1500}
# [87]
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(f'메로나 가격: {ice["메로나"]}')
# [88]
ice['메로나']=1300
# [89]
ice.pop('메로나')
print(ice)
# [90]
## 누가바가 없음
# [91]
inventory={'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}
# [92]
print(f'{inventory["메로나"][0]}원')
# [93]
print(f'{inventory["메로나"][1]}원')
# [94]
msg={'월드콘':[500,7]}
inventory.update(msg)
print(inventory)
# [95]
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_key=list(icecream.keys())
print(icecream_key)
# [96]
icecream_value=list(icecream.values())
print(icecream_value)
# [97]
print(sum(icecream_value))
# [98]
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
# [99]
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
msg=dict(zip(keys,vals))
# [100]
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table=dict(zip(date,close_price))
print(close_table)
# [101]
## bool
# [102]
## False
# [103]
## True
# [104]
## True
# [105]
## True
# [106]
## <=표시로 바꿔야 함
# [107]
## 아무것도 표시 안됨
# [108]
## Hi, there.
# [109]
## 1,2,4
# [110]
## 3,5
# [111]
msg='안녕하세요'
print(msg*2)
# [112]
msg='30'
print(int(msg)+10)
# [113]
msg='30'
if int(msg)%2: print('홀수')
else: print('짝수')
# [114]
msg='245'
data=int(msg)+20 if int(msg)+20<256 else 255
print(data)
# [115]
msg=150
data=255 if int(msg)-20>255 else int(msg)-20 if int(msg)-20 >0 else 0
print(data)
# [116]
msg='02:00'
data='정각입니다.' if int(msg[-2:])==0 else '정각이 아닙니다.'
print(data)
# [117]
msg='사과'
fruit = ["사과", "포도", "홍시"]
data='정답입니다.' if msg in fruit else '오답입니다.'
print(data)
# [118]
msg="Google"
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
data='투자경고 종목입니다.' if msg in warn_investment_list else '투자경고 종목이 아닙니다.'
print(data)
# [119]
msg='봄'
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
data='정답입니다.' if msg in fruit.keys() else '오답입니다.'
print(data)
# [120]
data='정답입니다.' if msg in fruit.values() else '오답입니다.'
print(data)
# [121]
msg='A'
data=msg.lower() if msg.isupper() else msg.upper()
print(data)
# [122]
score=83
data='A' if score>=80 else 'B' if score>=60 else 'C' if score>=40  else  'D' if score>=40 else 'E'
print(f'grade: {data}')
# [123]
msg='100 엔'
num={"달러": 1167,"엔": 1.096,"유로": 1268,"위안": 171}
a,b=msg.split()
print('{:.2f}원'.format(num[b]*int(a)))
# [124]
msg='10';msg1='20';msg3='30'
print(max(msg,msg1,msg3))
# [125]
msg='011-345-1922'
a,b,c=msg.split('-')
num={'011':'SKT','016':'KT','019':'LGU','010':'알수없음'}
print(f'당신은 {num[a]}사용자 입니다.')
# [126]
msg='01400'
a=int(msg[2])
num={(0,1,2):'강북구',(3,4):'도봉구',(6,7,8,9):'노원구'}
print(a)
print(a in list(num.items())[1][0])
if a in list(num.items())[0][0]:
    print('강북구')
elif a in list(num.items())[1][0]:
    print('도봉구')
else: print('노원구')
# [127]
msg='821010-1635210'
a,b=msg.split('-')
if b[0] in '13': data='남자'
else: data='여자'
print(data) 
# [128]
if b[1] in str(range(9)): print('서울입니다.')
else: print('서울이 아닙니다.')
# [129]
def check(a):
    x,y=a.split('-')
    a1=int(x[0])*2+int(x[1])*3+int(x[2])*4+int(x[3])*5+int(x[4])*6+int(x[5])*7
    print(a1)
    b1=int(y[0])*8+int(y[1])*9+int(y[2])*2+int(y[3])*3+int(y[4])*4+int(y[5])*5
    return 11-((a1+b1)%11)
if check(msg)==int(b[-1]): print('유효한 주민번호입니다.')
else: print('유효하지 않은 주민번호입니다.',check(msg))
# [130]
import requests

# [131]
## 사과\n 귤\n 수박
# [132]
## ####\n####\n####\n####
# [133]
## -
# [134]
## -
# [135]
## -
# [136]
for x in [10,20,30]:
    print(x)
# [137]
for x in [10,20,30]:
    print(x)
# [138]
for x in [10,20,30]:
    print(x)
    print('-----------')
# [139]
for x in ['++++',10,20,30]:
    print(x)
# [140]
for x in range(4):
    print('-----------')    
# [141]
리스트 = [100, 200, 300]
for x in 리스트:
    print(x+10)
# [142]
리스트 = ["김밥", "라면", "튀김"]
for x in 리스트:
    print(f'오늘의 메뉴: {x}')
# [143]
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for x in 리스트:
    print(len(x))
# [144]
리스트 = ['dog', 'cat', 'parrot']
for x in 리스트:
    print(f'{x} {len(x)}')
# [145]
for x in 리스트:
    print(x[0])
# [146]
리스트 = [1, 2, 3]
for x in 리스트:
    print(f'3 X {x}')
# [147]
for x in 리스트:
    print(f'3 X {x} = {3*x}')
# [148]
리스트 = ["가", "나", "다", "라"]
for x in 리스트[1:]:
    print(x)
# [149]
for x in 리스트[0]+리스트[2]:
    print(x)
# [150]
for x in 리스트[::-1]:
    print(x)
# [151]
리스트 = [3, -20, -3, 44]
list=[x for x in 리스트 if x<0]
print(list)
# [152]
리스트 = [3, 100, 23, 44]
for x in 리스트:
    if not x%3:
       print(x)
# [153]
리스트 = [13, 21, 12, 14, 30, 18]
a,b,c,*_=리스트
print(_)
for x in 리스트:
    if x<20 and not x%3:
        print(x)
# [154]
리스트 = ["I", "study", "python", "language", "!"]
for x in 리스트:
    if len(x)>=3:
        print(x)
# [155]
리스트 = ["A", "b", "c", "D"]
for x in 리스트:
    if x.islower():continue
    print(x)
# [156]
for x in 리스트:
    if x.isupper():continue
    print(x)
# [157]
리스트 = ['dog', 'cat', 'parrot']
for x in 리스트:
    print(x.upper())
# [158]
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for x in 리스트:
    print(x.split('.')[0])
# [159]
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for x in 리스트:
    if x.endswith('.h'):
        print(x)
# [160]
for x in 리스트:
    if x.endswith('.h') or x.endswith('.c'):
        print(x)

# [161]
for x in range(100):
    print(x)
# [162]
for x in range(2002,2051,4):
    print(x)
# [163]
list=[x for x in range(31) if not x%3]
# [164]
for x in range(0,100,-1):
    print(x)
# [165]
for x in range(10):
    print(x/10)
# [166]
for x in range(10):
    print(f'3 X {x} = {3*x}')
# [167]
for x in range(10):
    if not x%3:
        print(f'3 X {x} = {3*x}')
# [168]
a=0
for x in range(11):
    a=a+x
print(a)
# [169]
a=0
for x in range(1,11,2):
    a=a+x
print(a)
# [170]
a=1
for x in range(1,11,2):
    a=a*x
print(a)
# [171]
price_list = [32100, 32150, 32000, 32500]
for x in price_list:
    print(x)
# [172]
a=-1
for x in price_list:
    a=a+1
    print(f'{a} {x}')
    a=-1
# [173]
a=4
for x in price_list:
    a=a-1
    print(f'{a} {x}')
# [174]
a=90
for x in price_list[1:]:
    a=a+10
    print(f'{a} {x}')
# [175]
my_list = ["가", "나", "다", "라"]
a=0
for x in range(len(my_list[:3])):
    print(my_list[x], my_list[x+1])
# [176] 
my_list = ["가", "나", "다", "라", "마"]
for x in range(len(my_list[:3])):
    print(my_list[x], my_list[x+1], my_list[x+2])
# [177]
my_list = ["가", "나", "다", "라"]
for x in range(len(my_list)-1,0,-1):
    print(my_list[x],my_list[x-1])
# [178]
my_list = [100, 200, 400, 800]
for x in range(len(my_list)-1):
    print(my_list[x+1]-my_list[x])
# [179]
my_list = [100, 200, 400, 800, 1000, 1300]
for x in range(len(my_list)-2):
    print((my_list[x]+my_list[x+1]+my_list[x+2])/3)
# [180]
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility=[high_prices[x]-low_prices[x] for x in range(len(high_prices))]
print(volatility)    
# [181]
list1=['101호','102호']
list2=['201호','202호']
list3=['301호','302호']
lists=[list1,list2,list3]
print(lists)
# [182]
list1=[100,200,300]
list2=[80,210,330]
lists=[list1,list2]
# [183]
stock={'시가':[100,200,300],'종가':[80,210,340]}
# [184]
stock={'10/10':[80,110,70,90],'10/11':[210,230,190,200]}
# [185]
apart = [ [101, 102], [201, 202], [301, 302] ]
for x in range(len(apart)):
    for y in range(len(apart[x])):
        print(apart[x][y],'호',sep="")
# [186]
apart = [ [101, 102], [201, 202], [301, 302] ]
for x in range(len(apart)-1,-1,-1):
    for y in range(len(apart[x])):
        print(apart[x][y],'호',sep="")
# [187]
apart = [ [101, 102], [201, 202], [301, 302] ]
for x in range(len(apart)-1,-1,-1):
    for y in range(len(apart[x])-1,-1,-1):
        print(apart[x][y],'호',sep="")
# [188]
apart = [ [101, 102], [201, 202], [301, 302] ]
for x in range(len(apart)):
    for y in range(len(apart[x])):
        print(apart[x][y],'호',sep="")
        print('----')
# [189]
apart = [ [101, 102], [201, 202], [301, 302] ]
for x in range(len(apart)):
    print(apart[x][1],'호',sep="")
    print('----')
# [190]
apart = [ [101, 102], [201, 202], [301, 302] ]
for x in range(len(apart)):
    for y in range(len(apart[x])):
        print(apart[x][y],'호',sep="")
print('----')
# [191]
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for x in range(len(data)):
    for y in range(len(data[x])):
        print(data[x][y]*1.00014)
# [192]
for x in range(len(data)):
    for y in range(len(data[x])):
        print(data[x][y]*1.00014)
    print('----')
# [193]
result=[]
for x in range(len(data)):
    for y in range(len(data[x])):
        result.append(data[x][y]*1.00014)
# [194]
result1=[]
result2=[]
result3=[]
for x in range(len(data)):
    for y in range(len(data[x])):
        if x==2:
            result3.append(data[x][y]*1.00014)
        if x==1:
            result2.append(data[x][y]*1.00014)
        if x==0:
            result1.append(data[x][y]*1.00014)
result=[result1,result2,result3]
print(result)
# ---------------------------------------------
result5 = []
for x in data:
    sub = []
    for y in x:
        sub.append(y * 1.00014)
    result5.append(sub)
print(result5)
# [195]
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for x in ohlc:
    print(x[-1])
# [196]
for x in ohlc[1:]:
    if x[-1]>=x[0]:
        print(x[-1])
# [197]
for x in ohlc[1:]:
    if x[-1]>=x[0]:
        print(x[-1])
# [198]
list1=[x[1]-x[2] for x in ohlc[1:]]
print(list1)
# [199]
list1=[x[1]-x[2] for x in ohlc[1:] if x[-1]>x[0]]
print(list1)
# [200]
list1=[x[-1]-x[0] for x in ohlc[1:]]
print(sum(list1))