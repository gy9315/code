# [1] 데이터를 저장하는 코드르 작성
## 자신의 고향도시를 저장
## 자신의 혈액형을 저장
## 좋아하는 계절을 저장
## 키를 저장
## 전화번호를 저장
## 파이값을 저장
## 국적을 저장
home='jeju'
blood='B'
season='가을'
tall=182.1
num='010-6564-7162'
nation='Korea'
# [2] 알고 싶은 구구단을 입력 받은 후 구구단을 출력하세요
num=int(input('궁금한 구구단:'))
count=1
print(f'{num} * 1 = {num*1}')
count=count+1
print(f'{num} * {count} = {num*count}')
count=count+1
print(f'{num} * {count} = {num*count}')
count=count+1
print(f'{num} * {count} = {num*count}')
count=count+1
print(f'{num} * {count} = {num*count}')
count=count+1
print(f'{num} * {count} = {num*count}')
count=count+1
print(f'{num} * {count} = {num*count}')
count=count+1
print(f'{num} * {count} = {num*count}')
count=count+1
print(f'{num} * {count} = {num*count}')
# [3] 조건에 맞도록 코드를 작성하세요
## 정수 31 -> 실수로 일시적 변환
num=31
print(float(num))
## 정수 31 -> 실수로 완전히 변환
num1=float(num)
print(num1)
## 정수 2022 -> 문자열로 일시적 변환
num=2022
print(str(num))
## 정수 2022 -> 문자열로 완전히 변환
num1=str(num)
print(num1)
## 실수 98.1 -> 정수로 일시적 변환
num=98.1
print(int(num))
## 실수 98.1 -> 정수로 완전히 변환
num1=int(num)
print(num1)
## 실수 98.1 -> 문자열로 일시적 변환
num=98.1
print(str(num))
## 실수 98.1 -> 문자열로 완전히 변환
num1=str(num)
print(num1)
# [4] 데이터를 출력하도록 코드를 작성
## [4-1] 주민번호 881120-1068234
## 주민등록번호를 연원일(YYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력
ad='881120-1068234'
print('19'+str(ad[:6]))
print(ad[-7:])
## [4-2] 문자열 a:b:c:d
## 해당 문자열에서 a, b, c, d만 출력
str_='a:b:c:d'
num=0
print(str_[num])
num=num+2
print(str_[num])
num=num+2
print(str_[num])
num=num+2
print(str_[num])
## [4-3] 에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매
## 총 금액 출력 -> 에어컨 금액: 000원
str_='에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매'
pay=str_[7:9] + str_[10:13]
mon=str_[20:22]
all=int(pay)*int(mon)
print(all)
m=str((all//(10**6)) + 10**3)
m=m[1:4]
print(m)
n=str(((all//10**3)-int(m)*(10**3))+(10**3))
n=n[1:4]
print(n)
l=str((all-(all//10**3)*(10**3))+10**3)
l=l[1:4]
print('에어컨 금액: %s,%s,%s원' %(m,n,l))
## [4-4] 문자열 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
## 대문자만 출력 and 소문자만 출력
msg='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
large=msg[0]+msg[2]+msg[4]+msg[6]+msg[8]+msg[10]+msg[12]+msg[14]+msg[16]+msg[18]+msg[20]+msg[22]+msg[24]+msg[26]+msg[28]+msg[30]+msg[32]+msg[34]
small=msg[1]+msg[3]+msg[5]+msg[7]+msg[9]+msg[11]+msg[13]+msg[15]+msg[17]+msg[19]+msg[21]+msg[23]+msg[25]+msg[27]+msg[29]+msg[31]+msg[33]+msg[35]
print(msg[0:35:2])
print(msg[1:36:2])
print(large)
print(small)
## [4-5] '가로 10cm, 세로 11cm인 직사각형 넓이 계산' 문자열
## 직사각형 넓이 계산 후 출력 -> 직사각형 널비: 가로 10 X 세로 10 = 110
str_='가로 10cm, 세로 11cm인 직사각형 넓이 계산'
row=int(str_[3:5]) 
print(str_.find('11'))
line=int(str_[12:14])
print(f'직사각형 넓이: 가로{line} X 세로{row} = {line*row}')