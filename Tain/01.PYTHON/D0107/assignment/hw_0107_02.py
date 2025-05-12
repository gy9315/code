# [1]
## 1-1
list_=[]
list_.extend([10,40,"홍길동",False,40,False])
## 1-2
index1=list_.index(False)
index2=list_.index(False,list_.index(False)+1)
print(f'첫 번째 False의 인덱스/type: {index1}/{type(list_[index1])}')
print(f'두 번째 False의 인덱스/type: {index2}/{type(list_[index2])}')
## 1-3
nums=[1,6,3,9,10]
datas=['a',"b",'f','z']
print(nums+datas)
## 1-4
print(nums*10)
## 1-5
print(nums[::-1])
print(nums[3::3])
print(nums[2::2])
## 1-6
## append
## [10,3,91]
## [10,91]
## ERROR: X not in list
## insert
## [10,24,91]
nums=[]
nums.append(10)
nums.append(3)
nums.append(91)
print(nums)
nums.remove(3)
print(nums)
nums.insert(1,24)
print(nums)
## 1-7
nums=[1,2,3,1,2,3,5,6,7,3]
print(len(nums))
print(nums.count(3))
print(nums.index(6))
nums.pop()
print(nums)
nums.pop(3)
print(nums)
## 1-8
nums=[1,2,3,1,2,3]
data=['a','b']
nums_data=nums+data 
print(nums_data)
nums.extend(data)
print(nums)
## 1-9
data=['a','c',True,1,9,23,'Happy',21]
data.pop()
print(data)
data.remove(23)
data[1]='b'
print(data)
data.insert(1,2022)
print(data)
## 1-10
datas1=[9,30,1,21,5,8,0]
datas=[9,30,1,21,5,8,0]
print(f'{datas} sorted()활용 오름차순: {sorted(datas)}')
print(f'{datas} sorted()활용 내림차순: {sorted(datas,reverse=1)}')
datas.sort()
print(f'{datas1} sort method활용 오름차순: {datas}')
datas.sort(reverse=1)
print(f'{datas1} sort method활용 내림차순: {datas}')
# [2]
## 2-1
## tuple 추가/삭제/변경 등 불가, 데이터를 변경없이 보관하고자 할 떄 사용
#   * 단, 변경 시 list로 형 변환 -> 데이터를 변경 후 -> 다시 tuple로 재 형 병환
## 2-2
msg=(10,30,89,10,23,1,2,7,11)
## 2-3
print(msg[0],msg[1],msg[2],msg[3],msg[4],msg[5],msg[6],msg[7],msg[8])
print(msg[2::2])
print(msg[3::3])
## 2-4
## ERROR, Tuple은 변경/삭제/추가 불가
## 2-5
year=2022,;year=(2022,)
datas=(False,100,19.8,"Good")
datas=False,100,19.8,"Good"
# [3]
## 3-1
msg=input('주민번호를 입력해주세요(예:000000-0000000 "6자리-7자리" ):')
year='20'+msg.split('-')[0][:2].strip()
mon=msg.split('-')[0][2:4].strip()
day=msg.split('-')[0][4:6].strip()
print(f'{year}년 {mon}월 {day}일 생 {2024-int(year)}세')
## 3-2
num8=range(8,51,8)
num3=range(3,51,3)
num=list(num8)+list(num3)
num.sort()
print(f'최대값: {max(num)}, 최소값: {min(num)}, 합계: {sum(num)}, 평균: {sum(num)/len(num)} ')