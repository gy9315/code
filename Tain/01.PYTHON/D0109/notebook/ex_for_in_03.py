# 제어문 for ~ in 반복문
# [실습] 좋아하는 숫자를 10명의 사람에게 입력받은 후
#        숫자들을 저장해주세요.
#        그리고 가장 많은 사람들이 좋아하는 숫자가 무엇인지
#        출력해주세요
num=[]
for x in range(10):
    data=input('좋아하는 숫자:')
    num.append(int(data))
num1=[]
num_list=list(set(num))
for x in range(len(num_list)):
    num1.append(num.count(num_list[x]))
num_dict=dict(zip(num_list,num1))
print(num_dict)
max_key=[]
max_value=0
for item in num_dict.items():
    if max_value==item[1]: 
        max_key.append(str(item[0]))
        max_value=item[1]
    elif max_value<item[1]:
         max_key.clear()
         max_key.append(str(item[0]))
         max_value=item[1]
print(max_value)
print(max_key)
print(f'가장 많은 사람들이 좋아하는 숫자: {",".join(max_key)} 횟수: {max_value}번')