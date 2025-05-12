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
max_ratio=[0.0]*5
max_station=['1']*5
num_subway=['1']*5
non_staion=[]
total_num_list=[0.0]*5
for x in data:
    a=x[4]
    if x[4].strip().isnumeric() and x[6].strip().isnumeric():
        fee_data=int(x[4])
        non_fee_data=int(x[6])
        if fee_data!=0:
            ratio=fee_data/(fee_data+non_fee_data)
            count=0
            total_num=int(x[4])+int(x[6])
            # ------------------------------------------------------------------------
            if (int(x[4])+int(x[6]))>=100000:
                y=0
                    # ['운천','운천'...,'운천] 반복 입력 방지
                    # 한번입력하면 빠져나오기
                # --------------------------------------------------------------------
                while count==0:
                    if max_ratio[y]<ratio:
                        max_ratio.pop()
                        max_ratio.insert(y,ratio)
                        max_station.pop()
                        max_station.insert(y,x[3])
                        num_subway.pop()
                        num_subway.insert(y,x[1])
                        total_num_list.pop()
                        total_num_list.insert(y,total_num)
                        count=1
                # ---------------------------------------------------------------------
                    else : 
                        y+=1
                        if y==len(max_ratio)-1: count=1
                # ---------------------------------------------------------------------
                
        elif fee_data==0: 
            non_staion.append(x[3])
            print(x)
    # --------------------------------------------------------------------------------------------------
    # 확인
    if '서울역'==x[3]:
        print(x[1])
        print(x)
        print(int(x[4])/(int(x[4])+int(x[6])))
f.close()
# -------------------------------------------------------------------------------------------------------
# 출력값
print('-'*50)
print('무임 승차비율 상위 5 list')
print('-'*50)
# debuging
# -------------------------------------------------------------------------------------------------------
print(total_num_list)
# -------------------------------------------------------------------------------------------------------
for x in range(len(max_station)):
    print(f'무임승차 비율 순위 {x+1}번: {num_subway[x]} {max_station[x]}역, 비율: {max_ratio[x]*100:.1f}%')
print('-'*50)
print(f'유임승차가 없는 역: {non_staion}')
        
        
    
