import csv
def get_lowhigh_temp(data):
    header=next(data)
    lowest_temp=100
    highest_temp=-999
    for row in data:
        if row[3]=='':
            row[3]=100
        row[3]=float(row[3])
        if row[4]=='':
            row[4]=-999
        row[4]=float(row[4])
        if row[3] < lowest_temp:
            lowest_temp=row[3]
            lowest_date=row[0]
        if row[4] > highest_temp:
            highest_temp=row[4]
            highest_date=row[0]
    print('*'*50)
    print(f'대구 최저 기온 날짜: {lowest_date}, 온도: {lowest_temp}')
    print(f'대구 최고 기온 날짜: {highest_date}, 온도: {highest_temp}')
    

def main():
    f=open(r'C:\Users\gy931\OneDrive\Desktop\KDP-7\04.BiGDATA\data\daegu.csv',mode='r',encoding='EUC-KR')
    data=csv.reader(f,delimiter=',')
    get_lowhigh_temp(data)
    f.close()            
main()