import csv
f=open('../data/daegu.csv',mode='r',encoding='utf-8')
data=csv.reader(f,delimiter=',')
file=open('../data/daegu1.csv',mode='w',encoding='utf-8',newline='')
data1=csv.writer(file,delimiter=',')
header=next(data)
data1.writerow(header)
for x in data:
    date_string=x[0].split('-')
    x[0]='-'.join([date_string[0].replace('\t',''),date_string[1],date_string[2]])
    data1.writerow(x)
file.close()
f.close() 

