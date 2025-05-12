import pandas as pd
import pymysql as pl
from tabulate import tabulate
import matplotlib.pyplot as plt
import koreanize_matplotlib
conn=pl.connect(host='localhost',user='root',password='1234',db='economic_condition')
cur=conn.cursor(pl.cursors.DictCursor)
sql2='''
select * from food'''
sql3='''
select count(*) as 개수,연도 from utf
where 인허가일자=%s
'''
cur.execute(sql2)
row=cur.fetchall()
foodDF=pd.DataFrame(row)
cur.close()
conn.close()
print(tabulate(foodDF.head(),headers='keys',tablefmt='pretty'))
foodDF['영업중']=foodDF['영업중'].astype('int')
foodDF['폐업률']=foodDF['폐업률'].astype('float')
foodDF['연도']=pd.to_datetime(foodDF['연도'],format='%Y')
화천DF=foodDF[(foodDF['주소']=='강원특별자치도 화천군') & (foodDF['연도'].dt.year>=2014) & (foodDF['연도'].dt.year<=2024)]
철원DF=foodDF[(foodDF['주소']=='강원특별자치도 철원군') & (foodDF['연도'].dt.year>=2014) & (foodDF['연도'].dt.year<=2024)]
양구DF=foodDF[(foodDF['주소']=='강원특별자치도 양구군') & (foodDF['연도'].dt.year>=2014) & (foodDF['연도'].dt.year<=2024)]
print(화천DF)
army_27DF=pd.concat([화천DF.iloc[:,1:6].reset_index(drop=True),철원DF.iloc[:,2:6].reset_index(drop=True),양구DF.iloc[:,2:6].reset_index(drop=True)],axis=1)
print(army_27DF)
fig,axes=plt.subplots(1,3,figsize=(20,5), constrained_layout=True)
plt.suptitle('27사단 이전 전 지역과 주변지역 비교',size=15)

# 폐업 2,6,10
# 창업 1,5,9
# 영업중 3,7,11
# 폐업률 4,8,12
colors=['red','blue','green','purple']
titles=['폐업','창업','영업중','페업률']
for x,a,b,c,d,y in zip(range(len(axes)),range(2,11,4),range(1,10,4),range(3,12,4),range(4,13,4),['화천군','철원군','양구군']):    
    # for x,y in zip(range(len(axes)),['화천군','철원군','양구군'])
    axes1=axes[x].twinx()    
    axes[x].bar(army_27DF['연도'].dt.year*3,army_27DF.iloc[:,a],color='red',label=titles[0])
    axes[x].bar(army_27DF['연도'].dt.year*3+0.8,army_27DF.iloc[:,b],color='blue',label=titles[1])
    # axes[x].bar(army_27DF['연도'].dt.year*3+1.6,army_27DF.iloc[:,c],color='green',alpha=0.5,label=titles[2])        
    axes[x].set_xticks((army_27DF['연도'].dt.year*3)[::2]+0.8, army_27DF['연도'].dt.year[::2])
    axes1.plot((army_27DF['연도'].dt.year*3),army_27DF.iloc[:,d],'yo-',label=titles[3])
    axes[x].set_title(y,pad=15)
    axes[x].set_xlabel('연도')
    axes[x].set_ylabel('개수')
    axes1.set_ylabel('폐업률(%)')
    axes[x].axvline(x=2022*3+0.8, color='r', linestyle='--', linewidth=2, label='해체연도')
    axes[x].legend()    
plt.show()
