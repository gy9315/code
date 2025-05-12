import csv
import pandas as pd
f=open('./04.BiGDATA/data/daegu.csv',mode='r',encoding='utf-8')
data=csv.reader(f)
file=open('./04.BiGDATA/data/daegu1.csv',mode='w',encoding='utf-8',newline='')
data1=csv.writer(file,delimiter=',')
for x in data:
    data1.writerow(x)
file.close()
f.close()