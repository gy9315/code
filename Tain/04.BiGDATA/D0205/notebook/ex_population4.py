import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

# 차트만들기 공부 꼭 하기기
def draw_pie_chart(city_name,pop_list,label_list):
    plt.pie(pop_list,labels=label_list,autopct='%.1f%%',startangle=90,colors=plt.cm.Pastel1.colors,textprops={'fontsize':6})
    plt.legend(loc=1)
    plt.title(city_name+'학력인구 비율')
    plt.show()

def school_age_population(city):
    f=open('../data/age.csv',encoding='euc-kr')
    data=csv.reader(f)
    header=next(data)
    city_pop=0
    non_school_pop=0
    school_age_pop=0
    city_name=''
    pop_list=[]
    label_list=['초등학생','중학생','고등학생','대학생','비학력인구']
    for x in data:
        if city in x[0]:
            city_pop=int(x[1].replace(',',''))
            city_name=re.split('[()]',x[0])[0]
            x=[x[y].replace(',','') for y in range(len(x))]
            # 초등학생
            ele_pop=sum(list(map(int,x[9:15])))
            pop_list.append(ele_pop)
            # 중학생
            middle_pop=sum(list(map(int,x[15:18])))
            pop_list.append(middle_pop)
            # 고등학생
            high_pop=sum(list(map(int,x[18:21])))
            pop_list.append(high_pop)
            # 대학생
            uni_pop=sum(list(map(int,x[21:25])))
            pop_list.append(uni_pop)
            # 학교전체 인원 구하기
            break
    school_age_pop=sum(pop_list)
    non_school_pop=city_pop-school_age_pop
    pop_list.append(non_school_pop)

    f.close()
    print(city_name)
    print(f'전체 인구수: {city_pop}명, 학력 인구수: {school_age_pop}명, 비율: {(school_age_pop/city_pop)*100:.2f}')    
    draw_pie_chart(city_name=city_name,pop_list=pop_list,label_list=label_list)
    
    
school_age_population('서울특별시')