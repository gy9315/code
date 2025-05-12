import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f=open(r'C:\Users\gy931\OneDrive\Desktop\KDP-7\04.BiGDATA\data\daegu.csv',mode='r',encoding='EUC-KR')
data=csv.reader(f,delimiter=',')
header=next(data)
print(header)         
result=[]
for row in data:
    if row[4]!='' and row[0] !='':
        a=row[0].split('-')[1]
        if int(a)==8:
            result.append(float(row[4])) 
f.close()
plt.hist(result,bins=100,color='blue')
plt.title("8월의 온도분석")
plt.show()