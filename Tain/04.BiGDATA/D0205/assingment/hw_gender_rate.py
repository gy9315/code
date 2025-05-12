import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

f=open('../data/gender.csv', encoding='euc_kr')  
data=list(csv.reader(f))
fig,axes=plt.subplots(2,5,figsize=(10,10))
plt.suptitle('대구지역 남녀 비율',size=15)
# 인덱스 확인: 1 ~ 9까지
# for x in data:
#     if '대구광역시' in x[0]:
#         print(len(x))
# -----------------------------------------------------------------------
count=0
# 실행결과 출력 list 생성
total_male_list=[]
total_female_list=[]
for x in data:
    if '대구광역시' in x[0]:
        a=x[0]      
        # 전체 맨처음 건너뛰고 전부 남녀 비율 만들면 됨    
        male_list=[int(x[z].replace(',','')) for z in range(106,207)]
        female_list=[int(x[z].replace(',','')) for z in range(209,310)]
        print(f'{re.split('[()]',x[0])[0]}: (남: {(sum(male_list)):,}명, 여: {(sum(female_list)):,}명)')
        b=axes.flatten()[count].pie([sum(male_list),sum(female_list)],labels=['남성','여성'],autopct='%.1f%%',startangle=90,colors=['tomato','royalblue'])
        axes.flatten()[count].set_title(re.split('[()]',x[0])[0][5:]+'인구비율',fontsize=10)
        count+=1
    if count==10:
        break
f.close()
plt.tight_layout()
plt.show()