import pandas as pd
DF=pd.read_csv('./DATA/people.csv')
check=pd.read_csv('./DATA/social_distance.csv')
print(check)
DF.dropna(inplace=True)
# ['정류소명', '승객수_집계', 'label', 'X', 'Y', '가장가까운도로']
values=DF.loc[:,'승객수_집계'].values
total,bins=pd.cut(values,bins=[0,1000,2000,4000,5000,6000,8000,10000,30000,70000,200000],labels=range(10),retbins=True)
a=pd.DataFrame(total)
new=pd.concat([DF,a],axis=1).drop(columns=['정류소명', '승객수_집계', 'label', 'X', 'Y'])
new.columns=['도로명','인구점수']
check.loc[:,'인구점수']=0
for x,y in enumerate(new.도로명):
  check.loc[check.도로명==y]=new.loc[x,'인구점수']
print(check.loc[0])