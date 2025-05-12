import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib
def get_index_of_age_csv():
    f=open('../data/age.csv',encoding='euc-kr')
    data=csv.reader(f)
    header=next(data)
    print('-'*50)
    print('aga.acv index')
    print('-'*50)
    for x in range(len(header)):
        print(f'[{x:3}]: {header[x]}')
    f.close()
    
get_index_of_age_csv()