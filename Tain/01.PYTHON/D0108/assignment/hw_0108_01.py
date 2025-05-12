# 1
## 1-1
msg=1,5,3,9,1,1,2,8,7,4,2
msg=set(msg)
print(f'데이터: {msg}, 타입: {type(msg)}, 개수: {len(msg)}') 
## 1-2
msg=[1,1,5,2,6,9,2]
msg1=[5,9,1,3,4,2,8,7,1,2,5]
msg_union=list(set(msg).union(set(msg1)))
print(msg_union)
## 1-3
msg='Happy Christmas'
msg_set=set(msg.lower())
list(msg_set).sort()
print(''.join(list(msg_set)))
## 1-4
num6=set(range(1,7))
num9=set(range(4,10))
print(num6-num9)
print(num6|num9)
print(num6&num9)
## 1-5
list_=[9,3,1,8,7,2,1,4,2,3,5,7]
list_set=set(list_)
print(sum(list(list_set))/len(list_set))
## 1-6
set1={1,2,3}
set1.update([4,5,6,7,8])
print(set1)
## 1-7
dict1={'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dict1['name'], dict1['birth'])
print(dict1.get('gender','no-data'))
## 1-8
## bool
## 1-9
data=['Happy',"",[12],[],('A'),( ),{1:89,2:12}, { },1,0,None,set()]
data1=[bool(x) for x in data]
print(data1)
## 1-10
data1=input('학번, 이름, 전공, 학년 순서대로 입력해주세요:')
data2=input('학번, 이름, 전공, 학년 순서대로 입력해주세요:')
data3=input('학번, 이름, 전공, 학년 순서대로 입력해주세요:')
data=[]
datan=[]
data.append(data1.split(',')[1].strip());data.append(data2.split(',')[1].strip());data.append(data3.split(',')[1].strip())
print(data)
data1s=data1.split(',')[2:]
data1s.insert(0,data1.split(',')[0])
print(data1s)
data2s=data2.split(',')[2:]
data2s.insert(0,data2.split(',')[0])
data3s=data3.split(',')[2:]
data3s.insert(0,data3.split(',')[0])
datan.extend([data1s]);datan.extend([data2s]);datan.extend([data3s])
print(datan)
data_dict=dict(zip(data,datan))
print(data_dict)
# --------------------------------------------------------------------
data1=data1.split(',')
data2=data2.split(',')
data3=data3.split(',')
data=[data1.pop(1),data2.pop(1),data3.pop(1)]
datan=[data1,data2,data3]
data_dict=dict(zip(data,datan))
print(data_dict)