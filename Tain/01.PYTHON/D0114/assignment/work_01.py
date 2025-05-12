# [201]
def print_coin():
    print("비트코인")
# [202]
print_coin()
# [203]
for x in range(100):
    print_coin()
# [204]
def print_coins():
    for x in range(100):
        print_coin()
# [205]
## 함수호출이 먼저 발생
# [206]
## A \n B \n C \n A \n B
# [207]
## A \n C \n B
# [208]
## A \n C \n B \n E \n D
# [209]
## B \n A
# [210]
## B \n C \n B \n C \n B \n C \n A
# [211]
## 안녕 \n Hi
# [212]
## 7 \n 15
# [213]
## 문자열 미 입력
# [214]
## b에 str이 아닌 int를 입력함
# [215]
def plus():
    # msg=input()
    msg=msg+':D'
    print(msg)    
# [216]
# plus()
# [217]
def print_upper_price():
    # msg=input()
    msg=int(msg)*1.3
    print(msg) 
# [218]
def print_sum(a,b):
    return a+b
# [219]
def print_arithmetic_operation(a, b):
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} * {b} = {a*b}')
    print(f'{a} / {b} = {a/b}')
print_arithmetic_operation(3, 4)
# [220]
def print_max(a,b,c):
    x=[0]
    for y in (a,b,c):
        if y>x[0]:
            x.clear()
            x.append(y)
    print(x[0])
print_max(3,5,6)
# [221]
def print_reverse(a:str):
    print(a[::-1])
print_reverse("python")
# [222]
def print_score(a:list):
    print(sum(a)/len(a))
print_score([1, 2, 3])
# [223]
def print_even(a:list):
    list1=list(map(lambda x:x if not x%2 else '',a))
    list1=[x for x in list1 if len(str(x))!=0] 
    print(list1)
print_even ([1, 3, 2, 10, 12, 11, 15])
# [224]
def print_keys(a:dict):
    for x in a.keys():
        print(x)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# [225]
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(a:dict,b):
    print(a.get(b))
print_value_by_key  (my_dict, "10/26")
# [226]
def print_5xn(a:str):    
    for x in range(0,len(a),5):
        print(a[x:x+5])        
print_5xn("아이엠어보이유알어걸")
# [227]
def print_mxn(a:str,b:int=1):    
    for x in range(0,len(a),b):
        print(a[x:x+b])        
print_mxn("아이엠어보이유알어걸",3)
print_mxn("아이엠어보이유알어걸")
# [228]
def calc_monthly_salary(a:int):
    print(round(a/12))
calc_monthly_salary(12000000)
# [229]
## 지역변수 바인딩
# [230]
## 지역변수 바인딩
# [231]
## 4
# [232]
def make_url(a:str):
    print(f'www.{a}.com')
make_url("naver")
# [233]
def make_list(a):
    print(list(a))
make_list("abcd")

# [234]
def pickup_even(a:list):
    list1=[]
    for x in a:
        if not x%2:
            list1.append(x)
    print(list1)    
pickup_even([3, 4, 5, 6, 7, 8])
# [235]
def convert_int(num:str.isdecimal):
    num=int(num.replace(',',''))
    print(num)
convert_int("1,234,567")
# [236]
## 22
# [237]
## 22
# [238]
## 140
# [239]
## 16
# [240]
## 28