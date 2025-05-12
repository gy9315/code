import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib
import math

f=open('../data/gender.csv', encoding='euc_kr')  
data=list(csv.reader(f))
city_list=input('찾고 싶은 지역의 이름을 입력하세요:')
for x in data:
    if city_list in x[0]:
        male_list=[int(x[z].replace(',','')) for z in range(106,207)]
        female_list=[int(x[z].replace(',','')) for z in range(209,310)]
        for y in range(len(male_list)):
            bubble_size=[math.sqrt(male_list[y]+female_list[y])]
        break
print(f'[남성인구]: {sum(male_list)}명')
print(f'[여성인구]: {sum(female_list)}명')

plt.scatter(male_list,female_list,s=bubble_size,c=range(101),alpha=0.5,cmap='jet')
plt.colorbar()
plt.plot(range(max(male_list)),range(max(male_list)),'g--')
plt.title(f'{city_list}지역 남녀 인구 수 비교')
plt.xlabel('남성 인구 수')
plt.ylabel('여성 인구 수')
plt.show()    
    