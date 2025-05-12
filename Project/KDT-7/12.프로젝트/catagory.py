import pandas as pd
DF=pd.read_csv('./info1.csv',index_col=0)
col=DF.category.unique()
num=0
for x in col:
    a=DF.loc[DF['category']==x,:]
    len1=a.shape[0]
    a.index=range(num,num+len1)
    num+=len1
    x='-'.join(x.split('/'))
    a.to_csv(f'{x}.csv')


