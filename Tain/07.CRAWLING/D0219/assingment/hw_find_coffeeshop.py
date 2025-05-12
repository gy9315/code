import re
import pandas as pd
from tabulate import tabulate 
coffeeDF=pd.read_csv('./hollys_branch.csv',index_col=0)
   
def find_coffee():
    while True:
        try:
            region=input('검색할 매장의 지역을 입력하세요:').strip().split(' ')
        except:
            region=list(input('검색할 매장의 지역을 입력하세요:').strip())
        value=all(bool(re.search('[가-힣]+',x)) for x in region)  
        if value==True:
            # 정규표현식
            regex=[]
            for x in region:
                    regex.append(f'.*{x}.*')
            regex=[re.compile(x) for x in regex]
            a=coffeeDF[coffeeDF['지역'].apply(lambda x: all(bool(y.search(x)) for y in regex))]
            a.index=range(1,a.shape[0]+1)
            print(f'검색된 매장 수: {a.shape[0]}')
            print(tabulate(a,tablefmt='pretty',headers=a.columns))
        elif region[0]=='quit':
            print('종료합니다.')
            break
        else: 
            print('제대로 지역을 입력해주세요!')
        
find_coffee()