# 형식/서식지정 문자열
# - % 알파벳 1개
# - %d 10진수,%f 실수, %s 문자열
# -----------------------------
# 정수 2개 덧셈 결과 출력하기
num1=9
num2=7
print(num1+num2)
print(num1,'+',num2,'=',num1+num2,sep='')

print('num1+ num2 = num1+num2')

print('%d+%d=%d' %(num1,num2,num1+num2))
print('%f+%f=%f' %(num1,num2,num1+num2))
num=input('정수를 입력하시오:')
num3=input('정수를 입력하시오:')
num=int(num)
num3=int(num3)
print('%d+%d=%d' %(num,num3,num+num3))
