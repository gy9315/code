import csv
f=open('../data/subwaytime.csv',encoding='utf-8')
data=csv.reader(f,delimiter=',')
next(data)
next(data)
total=0
result=[]
for x in data:
    x[4:]=map(int,x[4:])
    total+=x[4]
    result.append(x[4])
print(f'총 지하철 역의 수: {len(result)}')
print(f'새벽 4시에 총 승차인원 수: {total}')