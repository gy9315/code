from gen_moving import *
# print(person_in_totalDF.columns)
taxDF=pd.DataFrame(np.zeros([3,person_in_totalDF.shape[1]]),columns=person_in_totalDF.columns)
# print(taxDF)
for x in taxDF.columns[1:]:
    time=pd.to_datetime(x,format='%Y.%m')
    if time.year<=2004:
        taxDF[x]=0.05
    elif time.year<2011:
        taxDF[x]=0.04
    elif time.year<=2013:
        if time.month<=9:
            taxDF[x]=0.04
        else:
            taxDF.loc[0,x]=0.01
            taxDF.loc[1,x]=0.02
            taxDF.loc[2,x]=0.03
    else:
            taxDF.loc[0,x]=0.01
            taxDF.loc[1,x]=0.02
            taxDF.loc[2,x]=0.03
taxDF['지역']=['6억 이하','9억 이하','9억 초과']
taxDF.rename(columns={'지역':'구분'},inplace=True)
taxDF.to_csv('tax.csv',encoding='utf-8')