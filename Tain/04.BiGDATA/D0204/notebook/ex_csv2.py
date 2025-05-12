import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

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
plt.hist(result,bins=500,color='blue')
plt.title("1907년 부터 2024년까지 대구 최고 기온 히스토그램")
plt.show()
# data=csv.reader(f)

# next(data)
# result=[]
# for	row	in	data	:
#     if row[-1] !='':	
#         result.append(float(row[-1]))
# f.close()
# plt.figure(figsize=(10,	2))
# plt.hist(result,	bins=500,	color='blue')	
# plt.rcParams['axes.unicode_minus']	=	False	
# plt.show()