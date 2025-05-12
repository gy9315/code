import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

f = open('../data/gender.csv', encoding='euc_kr')
data = csv.reader(f)
header = next(data)
for i in range(len(header)):
   print(f'[{i:3d}]: {header[i]}', end=', ')
   if (i+1) % 5 == 0:
      print()
      break
   print()


male_num_list = []
female_num_list = []


district = input('시군구 이름을 입력하세요: ')
for row in data:
   if district in row[0]:
      for male in row[106:207]:
         male = male.replace(',','')
         male_num_list.append(-int(male))
      for female in row[209:310]:
         female = female.replace(',','')
         female_num_list.append(int(female))
      break
f.close()


print(f'남성 총 인구수:{sum(male_num_list):,}')
print(male_num_list)
print('-------------------------------')
print(f'여성 총 인구수:{sum(female_num_list):,}')
print(female_num_list)

plt.barh(range(len(male_num_list)), male_num_list, label='남성')
plt.barh(range(len(female_num_list)), female_num_list, label='여성')
plt.title('성별 인구 비율')
plt.legend()
plt.show()