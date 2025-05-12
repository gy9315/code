import pandas as pd
DF=pd.read_csv('./DATA/지역총생산.csv',encoding='utf-8')
print(DF.columns)
for x in DF.columns[2:]:
    DF[x]=DF[x].str.replace(',','')
    DF[x]=DF[x].astype('float')
print(DF.dtypes)
DF.to_csv('army_grdp.csv')