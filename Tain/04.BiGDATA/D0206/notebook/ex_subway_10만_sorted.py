import csv
import numpy as np
# def max5(data):
#     next(data)
#     a=[(int(x[4])/(int(x[4])+ int(x[6]))) for x in data]
#     return a[0]
        
# f=open('../data/subwayfee.csv',encoding='utf-8')
# data=csv.reader(f,delimiter=',')
# sorted(data, key=lambda x:[(int(x[4])/(int(x[4])+ int(x[6]))) for x in data][0])
np.random.seed(11)
a=np.random.randint(0,11,9)
b=np.random.randint(0,11,9)
print(len(a))
print(b)
c=zip(a,b)
for x in c:
    print(x)
a,b=zip(*c)
print
# # x=0
# # for y in data:
# #     if x<5:
# #         print(y)
# #     x+=1
# # column=['\ufeff사용월', '호선명', '역ID', '지하철역', '유임승차', '유임하차', '무임승차', '무임하차']
# # 유임 승차 대 무임 승차 비율이 가장 높은 역 계산
# # 각 역 별 승차 비율 확인
# # 최대 승차 비율로 바꿈 
# # 데이터 전부 읽기
# # sorted 함수 사용해서 정렬하기
# next(data)
# print(data[0])
# for x in data:
#     if x[6]!=0:
        

# f.close()
# # -------------------------------------------------------------------------------------------------------
# # 출력값
# print('-'*50)
# print('무임 승차비율 상위 5 list')
# print('-'*50)
# # debuging
# # -------------------------------------------------------------------------------------------------------
# print(total_num_list)
# # -------------------------------------------------------------------------------------------------------
# for x in range(len(max_station)):
#     print(f'무임승차 비율 순위 {x+1}번: {num_subway[x]} {max_station[x]}역, 비율: {max_ratio[x]*100:.1f}%')
# print('-'*50)
# print(f'유임승차가 없는 역: {non_staion}')
        
        
    
