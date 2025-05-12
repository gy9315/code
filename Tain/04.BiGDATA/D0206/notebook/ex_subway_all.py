import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
f=open('../data/subwayfee.csv',encoding='utf-8')
data=csv.reader(f,delimiter=',')
next(data)
# x=0
# for y in data:
#     if x<5:
#         print(y)
#     x+=1
# column=['\ufeff사용월', '호선명', '역ID', '지하철역', '유임승차', '유임하차', '무임승차', '무임하차']
# 유임 승하차 무임 승하차(zip)
fee_updata=[]
fee_downdata=[]
non_fee_updata=[]
non_fee_downdata=[]
subway_station=[]
for x in data:
    subway_station.append((x[1]+' '+x[3]))
    for y in range(4,8):
        if y==4: fee_updata.append(x[y])
        if y==5: fee_downdata.append(x[y])
        if y==6: non_fee_updata.append(x[y])
        if y==7: non_fee_downdata.append(x[y])
f.close()   
# -------------------------------------------------------------------------------------------------------
# pie차트 저장
count=0
for x,y,z,a,b in zip(fee_updata,fee_downdata,non_fee_updata,non_fee_downdata,subway_station):
    if count<11:
        labels=['유임승차','유임하차','무임승차','무임하차']
        color= ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
        explods=[0.05,0.05,0.05,0.05] 
        plt.pie([x,y,z,a],labels=labels,colors=color,explode=explods,shadow=True,autopct='%.1f%%')
        plt.legend(loc=1,bbox_to_anchor=(1.2,1))
        plt.title(f'{b}의 승·하차 인원 분석')
        plt.savefig('img/'+b+'.png')
        plt.close()
        count+=1
    
