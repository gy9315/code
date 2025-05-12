import csv
f=open('../data/subwayfee.csv',encoding='utf-8')
data=csv.reader(f,delimiter=',')
# x=0
# for y in data:
#     if x<5:
#         print(y)
#     x+=1
# column=['\ufeff사용월', '호선명', '역ID', '지하철역', '유임승차', '유임하차', '무임승차', '무임하차']
# 유임 승차 대 무임 승차 비율이 가장 높은 역 계산
# 각 역 별 승차 비율 확인
# 최대 승차 비율로 바꿈 
# 데이터 전부 읽기
max_ratio=[1]*5
max_station=['1']*5
num_subway=['1']*5
non_staion=[]
fee_num=['1']*5
total_num=['1']*5
for x in data:
    a=x[4]
    if x[4].strip().isnumeric() and x[6].strip().isnumeric():
        fee_data=int(x[4])
        non_fee_data=int(x[6])
        if fee_data!=0:
            ratio=fee_data/sum(list(map(int,[x[4],x[6]])))
            count=0
            if sum(list(map(int,[x[4],x[6]])))>=10000 and ratio<=0.5:
                y=0
            # ['운천','운천'...,'운천]
                while count==0:
                    if max_ratio[y]>ratio:
                        max_ratio.pop()
                        max_ratio.insert(y,ratio)
                        max_station.pop()
                        max_station.insert(y,x[3])
                        num_subway.pop()
                        num_subway.insert(y,x[1])
                        fee_num.pop()
                        fee_num.insert(y,x[4])
                        total_num.pop()
                        total_num.insert(y,int(x[4])+int(x[6]))
                        count=1
                        c=1
                    else: 
                        y+=1
                        if y==len(max_ratio)-1:count=1
        elif fee_data==0: 
            non_staion.append(x[3])
            print(x)
    if '영등포'==x[3]:
        print(x)
f.close()
# -------------------------------------------------------------------------------------------------------
# 출력값
print('-'*50)
print('무임 승차비율 상위 5 list')
print('-'*50)
for x in range(len(max_station)):
    print(f'무임승차 비율 순위 {x+1}번: {num_subway[x]} {max_station[x]}역\n전체 인원: {int(total_num[x]):,}명 유임승차 인원: {int(fee_num[x]):,}명 비율: {max_ratio[x]*100:.1f}%')
    print()
print('-'*50)
print(f'유임승차가 없는 역: {non_staion}')
        
        
    
