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

def get_voting_populatin(city):
    f=open('../data/age.csv',encoding='euc-kr')
    data=csv.reader(f)
    header=next(data)
    city_name=''
    city_population=0
    voting_population=0
    for x in data:
        if city in x[0]:
            city_population=int(x[1].replace(',',''))
            city_name=re.split('[()]',x[0])[0]
            for y in x[21:]:
                y=int(y.replace(',',''))
                voting_population+=y
            break
    f.close()
    print(f'{city_name} 전체 인구수: {city_population}명 투표 가능 인구수: {voting_population}')
    draw_pie_chart(city_name,city_population,voting_population)
    
    
get_voting_populatin('대구')