import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

def draw_pie_chart(city_name,city_population_list,voting_population):
    non_voting_population=city_population_list-voting_population
    population=[non_voting_population,voting_population]
    colors=['tomato','royalblue']
    plt.pie(population,labels=['18세 미만','투표가능인구'],autopct='%.1f%%',startangle=90,colors=colors)
    plt.legend(loc=1)
    plt.title(city_name+'인구비율')
    plt.show()


def print_population(population_list):
    for x in range(len(population_list)):
        if (x+1)%10==0:
            print(f'{x:3d}세: {population_list[x]:7d}명')
        else: print(f'{x:3d}세: {population_list[x]:7d}명',end=" ")
    print()
    

def draw_geneder_population(title, male_num_list, female_num_list):
# barh(y축 범위, data)
    plt.barh(range(len(male_num_list)), male_num_list, label='남성')
    plt.barh(range(len(female_num_list)), female_num_list, label='여성')
    plt.rcParams['axes.unicode_minus'] = False  
    plt.title(title + ' 성별 인구 비율')  
    plt.legend()
    plt.show()


def calculate_population():
    f=open('../data/gender.csv', encoding='euc_kr')  
    data=csv.reader(f)
    male_num_list=[]  
    female_num_list=[]
    district = input('시군구 이름을 입력하세요: ')  
    for row in data:
        if district in row[0]:
            for  male  in  row[106:207]:	# 남성 연령별 인구수 구간
                male=male.replace(',',  '')	# 천단위 콤마 제거
                male_num_list.append(int(male))
            for female in row[209:310]:
                female=female.replace(',', '')  
                female_num_list.append(int(female))
            break
    f.close()

    print(f'남성 총 인구수:{sum(male_num_list):,} ')
    print_population(male_num_list)
    print('-'*50)  
    print(f'여성 총 인구수:{sum(female_num_list):,} ')  
    print_population(female_num_list)
    draw_geneder_population(district, male_num_list, female_num_list)

calculate_population()