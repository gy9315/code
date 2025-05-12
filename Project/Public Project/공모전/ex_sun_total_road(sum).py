import pandas as pd
import matplotlib.pyplot as plt

DF=pd.read_csv('./DATA/sun_location(0-2650-2700-3100-3200-5600-5700-6600-6850-).csv')
DF.columns=['도로명','시작위도','시작경도','연속 일조량','총 일조량','중간위도','중간경도','연속 일조량','총 일조량','끝위도','끝경도','연속 일조량','총 일조량']
DF['총 일조량']=DF['총 일조량'].applymap(lambda x:x.translate(str.maketrans({'시':'.','분':'','간':''})))
DF['연속 일조량']=DF['연속 일조량'].applymap(lambda x:x.translate(str.maketrans({'시':'.','분':'','간':''})))
DF['총 일조량']=DF['총 일조량'].applymap(lambda x:int(x.split('.')[0])*60+int(x.split('.')[1]))
DF['연속 일조량']=DF['연속 일조량'].applymap(lambda x:int(x.split('.')[0])*60+int(x.split('.')[1]))
count_road_list=[]
for x in DF['도로명'].unique():
    a=DF[DF['도로명']==x]
    b=a['총 일조량'].sum(axis=1)/3
    total=b.sum(axis=0)/a.shape[0]
    total=round(total.item(),2)
    c=a['연속 일조량'].sum(axis=1)/3
    max=c.sum(axis=0)/a.shape[0]
    max=round(max.item(),2)
    count=a.shape[0]
    count_road_list.append([x,count,total,max])   
count_road_listDF=pd.DataFrame(count_road_list,columns=['도로명','개','총 일조량','연속 일조량'])
# print(count_road_listDF)
def position_check(address):
    print(address)
    print(DF.loc[DF['도로명']==address,['시작위도','시작경도','중간위도','중간경도','끝위도','끝경도']])
    
plt.plot(count_road_listDF['총 일조량'])
plt.show()
total,bin_t=pd.cut(count_road_listDF['총 일조량'],bins=10,labels=range(0,10),retbins=True)
print(bin_t)
max,bin_m=pd.cut(count_road_listDF['연속 일조량'],bins=10,labels=range(0,10),retbins=True)
print(bin_m)
plt.plot(max)
plt.plot(pd.Series(total).astype('int')+10,alpha=0.5)
plt.show()