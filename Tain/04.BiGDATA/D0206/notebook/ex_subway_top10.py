import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
f=open('../data/subwaytime.csv',encoding='utf-8')
data=csv.reader(f,delimiter=',')
next(data)
next(data)
fig,axes=plt.subplots(1,2,figsize=(15,5))
fig.set_facecolor('lightgray')
plt.suptitle('출근시간대 승차 인원',color='royalblue',size=15)
station_list=[]
for x in data:
    x[4:]=map(int,x[4:])
    a=sum(x[10:15:2])
    station_list.append((x[3],a))
station_list.sort(key=lambda x:x[1],reverse=True)
a=station_list[:10]
station=[a[x][0][:2] for x in range(len(a))]
station_num=[a[x][1] for x in range(len(a))]
all_station_num=[station_list[x][1] for x in range(len(station_list))]
axes[0].bar(station,station_num,color='tomato')
axes[0].set_title('상위 10개 승차 인원수')
axes[1].bar(range(len(all_station_num)),all_station_num,color='tomato')  
axes[1].set_title('전체 역의 승차 인원수')   
plt.show()   
