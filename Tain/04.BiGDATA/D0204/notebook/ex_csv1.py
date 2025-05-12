import csv
import matplotlib.pyplot as plt

f=open(r'C:\Users\gy931\OneDrive\Desktop\KDP-7\04.BiGDATA\data\daegu.csv',mode='r',encoding='EUC-KR')
data=csv.reader(f,delimiter=',')
header=next(data)
print(header)         
result=[]
for row in data:
    if row[4]!='':
       result.append(float(row[4])) 
f.close()
plt.figure(figsize=(10,2))
plt.plot(range(len(result)),result,'r')
plt.show()