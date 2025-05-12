# 함수와 객체와 함수이름 관계
age=10 # 객체 10의 주소를 age에 저장, 참조하고있다
num=age # 객체 10의 주소를 참조하고있다
print(age,num)  
# [함수의 경우]
# 변수명=함수이름
mysum=sum # sum이 정하고있는 주소를 참조하고있다
sum_id=id(sum)
mysum_id=id(mysum)
print(sum([10,20]),mysum([10,20]))
print(type(sum))