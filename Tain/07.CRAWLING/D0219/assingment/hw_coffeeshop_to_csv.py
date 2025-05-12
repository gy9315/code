from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import re
query=range(1,50)
total_info_list=[]
for x in query:
    html=urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={x}&sido=&gugun=&store=')
    s=BeautifulSoup(html,'html.parser')
    info_list=[]
    for x in s.select('tbody td.center_t'):
        count=0
        info_list.append(x.text)
    total_info_list.extend(info_list)
# # 순서 (::5)
totalDF=pd.DataFrame({1:total_info_list[::6],2:total_info_list[1::6],3:total_info_list[2::6],4:total_info_list[3::6],
                      5:total_info_list[4::6],6:total_info_list[5::6]})
# totalDF.to_csv('totalDF.csv',encoding='utf-8')
totalDF.drop(columns=[3,5],inplace=True)
totalDF.columns=['지역','매장명','주소','전화번호']
totalDF.to_csv('hollys_branch.csv',encoding='utf-8',index=True)
for x in totalDF.index:
    print(f"[{x+1:>3}] 매장이름: {totalDF.loc[x,'매장명']}, 지역: {totalDF.loc[x,'지역']},주소: {totalDF.loc[x,'주소']}, 전화번호: {totalDF.loc[x,'전화번호']}")