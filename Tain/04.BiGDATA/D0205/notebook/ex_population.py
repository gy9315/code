import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib
f=open('../data/age.csv',encoding='euc-kr')
data=csv.reader(f)
header=next(data)
result=[]
for row in data:
    if '산격3동' in row[0]:
        str_list=re.split('[()]',row[0])
        print(str_list)
        city=str_list[0]
        for data in row[3:]:
            data=data.replace(',','')
            result.append(int(data))
f.close()
plt.title(f'{city} 인구 현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()
