import pandas as pd
from tabulate import tabulate
dustDF=pd.read_excel('../data/dust.xlsx')
print(tabulate(dustDF.head(),headers='keys',tablefmt='pretty'))
# print(dustDF.info())
# 날짜 datatime으로 변경 필요
# 기체 np.nan 5개 처리필요
# -----------------------------------------------------------
for x in dustDF.columns:   
    print(x) 
    print(dustDF.loc[:,x][dustDF.loc[:,x].isna()]) 
# -----------------------------------------------------------
# 결측치 값: [84,85,327,328,589,590]
# +[691,712]
# print(dustDF.columns)
dustDF.columns=['date', 'so2', 'co', 'o3', 'no2', 'PM10', 'PM2.5']
print(dustDF.columns)
# print(dustDF['date'].str[-2:])
# print(dustDF['date'].str[-2:]=='24')
# 조건설정
# ---------------------------------------------------------------------------------------------------------------------------------------------
a=dustDF['date'].str[-2:]=='24'
# print(dustDF['date'][a])
b=dustDF['date'][a].apply(lambda x: x[0:-5]+str(int(x[-5:-3])+1)+' '+'00' if int(x[-5:-3])>=9 else x[0:-5]+'0'+str(int(x[-5:-3])+1)+' '+'00')
dustDF['date'][a]=b
# print(dustDF['date'][a])
dustDF.drop(index=[dustDF.shape[0]-1],inplace=True)
# ---------------------------------------------------------------------------------------------------------------------------------------------
dustDF.ffill(inplace=True)
# dustDF.to_excel('dust_hour.xlsx',index=False)
dustDF['date']=pd.to_datetime(dustDF['date'],format='%Y-%m-%d %H')
print(dustDF.info())