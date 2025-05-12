import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
# 시간대 별 가장 많이 승차 하는 역
# 4시 ~ 다음날 2시까지
f=open('../data/subwaytime.csv',encoding='utf-8')
data=csv.reader(f,delimiter=',')
header=next(data)
header1=next(data)
data=list(data)
# ------------------------------------------------
# 확인 4,6,..50
time_total_best=[]
for x in range(24):
    time_best=[]    
    for y in data:
        time_best.append((y[3],y[4+2*x]))
    time_best.sort(key=lambda x:int(x[1]),reverse=True)
    time_total_best.append(time_best[0])
print(len(time_total_best))

plt.bar()
# print(time_total_best)