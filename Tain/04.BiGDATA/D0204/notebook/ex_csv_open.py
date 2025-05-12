# import csv
# f=open(r'C:\Users\gy931\OneDrive\Desktop\KDP-7\04.BiGDATA\data\daegu.csv',mode='r',encoding='EUC-KR')
# data=csv.reader(f,delimiter=',')
# file=open(r'C:\Users\gy931\OneDrive\Desktop\KDP-7\04.BiGDATA\data\daegu1.csv',mode='w',encoding='EUC-KR',newline='')
# data1=csv.writer(f,delimiter=',')
# count=0
# for x in data:
#     if count<20:
#         print(x)
#     count+=1
#     for y in range(len(x)):
#         x[y]=x[y].replace('\t','')
#     print(x)
#     data1.writerow(x)

import csv
f=open(r'C:\Users\gy931\OneDrive\Desktop\KDP-7\04.BiGDATA\data\daegu.csv',mode='r',encoding='EUC-KR')

# f=open(r'04.BiGDATA\data\daegu_temp.csv','r')
# f=open(r'04.BiGDATA\data\daegu_temp.csv','r')
# f=open('./04.BiGDATA/data/daegu_temp.csv','r',encoding='utf-8')
data=csv.reader(f,delimiter=',')
# count=0
# for x in data:
#     if count<20:pass
#         # print(x)
#     count+=1

file=open(r'C:\Users\gy931\OneDrive\Desktop\KDP-7\04.BiGDATA\data\daegu1.csv',mode='w',encoding='EUC-KR',newline='')
data1=csv.writer(file)
for x in data:
    for y in range(len(x)):
        x[y]=x[y].replace('\t','')
    data1.writerow(x)
file.close()
file=open(r'C:\Users\gy931\OneDrive\Desktop\KDP-7\04.BiGDATA\data\daegu1.csv',mode='r',encoding='EUC-KR',newline='')
data1=csv.reader(file)
count=0
for x in data1:
    if count<20:
        print(x)
    
    count+=1