## [4-4] 문자열 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
## 대문자만 출력 and 소문자만 출력
msg='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'

large=msg[0]+msg[2]+msg[4]+msg[6]+msg[8]+msg[10]+msg[12]+msg[14]+msg[16]+msg[18]+msg[20]+msg[22]+msg[24]+msg[26]+msg[28]+msg[30]+msg[32]+msg[34]
small=msg[1]+msg[3]+msg[5]+msg[7]+msg[9]+msg[11]+msg[13]+msg[15]+msg[17]+msg[19]+msg[21]+msg[23]+msg[25]+msg[27]+msg[29]+msg[31]+msg[33]+msg[35]
print(large)
print(small)
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