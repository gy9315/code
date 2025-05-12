# str 타입 전용 함수 즉, method
# - 사용법: 변수명.method()
# -------------------------------------------
# [3] 원소 갯수 method: count()
data='HappyHappy'
# 제일 뒤에서 부터'p' index 찾기
print(f'p의 count: {data.count("p")}')
print(f'p의 index: {data.count("pp")}')
# [4] 특정 문자열을 다른 문자열로 변경하는는 method: count()
print(f'H를 h로 변경: {data.replace("H","h")}')
# [실습]
msg='에어컨이 월 1,148,584원에 무이자 36개월.'
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