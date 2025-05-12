import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib
f=open('../data/age.csv',encoding='euc-kr')
data=csv.reader(f)
# count=0
# for x in data:
#     if count<5:
#         print(x)
#     count+=1
f.close()

def parse_district_name(city):
    city_name=re.split('[()]',city)
    return city_name[0]


def print_population(population_list):
    for x in range(len(population_list)):
        if (x+1)%10==0:
            print(f'{x:3d}세: {population_list[x]:7d}명')
        else: print(f'{x:3d}세: {population_list[x]:7d}명',end=" ")
    print()
        

def draw_population(city_name,population_list):
    plt.title(f'{city_name} 인구 현황')
    plt.xlabel('나이');plt.ylabel('인구수');plt.bar(range(101),population_list)
    plt.xticks(range(0,101,10))
    plt.show()
    

def get_population(city):
    f=open('../data/age.csv',encoding='euc-kr')
    data=csv.reader(f)
    next(data)
    populatiion_list=[]
    full_district_name=''
    for x in data:
        if city in x[0]:
            full_district_name=parse_district_name(x[0])
            for y in x[3:]:
                y=y.replace(',','')
                populatiion_list.append(int(y))
            break
    f.close()
    print_population(populatiion_list)
    draw_population(full_district_name,populatiion_list)
    
city=input('인구 구조를 알고 싶은 지역의 이름을 입력하세요')
get_population(city)