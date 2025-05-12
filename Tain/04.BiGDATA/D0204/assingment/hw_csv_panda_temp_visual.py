import pandas as pd
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
# 입력 연도에 6월부터 9월까지 열대야 일자와 전체 횟수를 출력
# 열대야 최저온도: 25도 이상
# pandas활용하여 표현
# {'날짜':0,'지점':1,'평균기온':2,'최저기온':3,'최고기온’:4}
def main():
    f=open(r'C:\Users\gy931\OneDrive\Desktop\KDP-7\04.BiGDATA\data\daegu1.csv',encoding='utf-8')
    data=list(csv.reader(f))
    temp_list=[]
    for y in range(1990,2025):
        total_temp_list=[]
        for x in data:
            if x[1].isnumeric():    
                date_string=x[0].split('-')
                # 조건 설정
                if int(date_string[0])==y and float(x[3])>=25 and int(date_string[1]) in [6,7,8]:
                    # 온도입력하기
                    total_temp_list.append(x[3])
            else:pass
        # 연도 온도 입력 총 횟수 입력하기
        temp_list.append(len(total_temp_list))
    # 10개씩 출력하기
    count=0
    for x,y in zip(range(1990,2025),temp_list):
        if not count%10:
            print(f'\n{x}년: {y}회',end=" ")
        else:
            print(f'{x}년: {y}회',end=" ")
        count+=1      
    plt.figure(figsize=(19,5))
    plt.bar(range(len(temp_list)),temp_list)
    plt.xticks(range(len(temp_list)),range(1990,2025))
    plt.xlabel('year')
    plt.ylabel('열대야 수')
    plt.title('1990년도에서 2024년도 까지 열대야 현황')
    plt.show()
    f.close()
    
    
main()