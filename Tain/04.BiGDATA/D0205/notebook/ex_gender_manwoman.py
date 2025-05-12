import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

f=open('../data/gender.csv', encoding='euc_kr')  
data=list(csv.reader(f))
city_list=['서울특별시','부산광역시','대구광역시','인천광역시','대전광역시','광주광역시']
fig,axes=plt.subplots(2,3,figsize=(10,10))
plt.suptitle('지역 별 남녀 인구 추이',size=15)
for x,a in zip(city_list,range(len(city_list))):
    for y in data:
        if x in y[0]:
            male_list=[int(y[z].replace(',','')) for z in range(106,207)]
            female_list=[int(y[z].replace(',','')) for z in range(209,310)]
            break
    axes.flatten()[a].plot(male_list,label='남성')
    axes.flatten()[a].plot(female_list,label='여성')
    axes.flatten()[a].set_title(f'{x} 남녀 인구 추이')
    axes.flatten()[a].set_xlabel('나이')
    axes.flatten()[a].set_ylabel('인구')
    axes.flatten()[a].legend(loc=1)
plt.tight_layout()
f.close()
plt.show()