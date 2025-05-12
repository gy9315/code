from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlopen
import re
import time
import os
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
count=0
url_list=[]
for post_id in range(1,100): 
    url=f'https://www.wevity.com/?c=find&s=1&mode=end&gub=1&sp=name&sw=%EA%B3%B5%EB%AA%A8%EC%A0%84&gp={post_id}'
    driver.get(url)
    time.sleep(2)
    soup=BeautifulSoup(driver.page_source,'html.parser')
    links=soup.select('div.tit > a')
    for x in links:
        url_list.append(x.text.strip())
a=pd.DataFrame([url_list]).T
a.to_csv('add_info.csv')
# total_info=[]
# for url in url_list:
#     base_url=f'https://www.wevity.com/{url}'
#     driver.get(base_url)
#     soup=BeautifulSoup(driver.page_source,'html.parser')
#     topic=soup.select_one('div.tit-area > h6.tit').text.strip()
#     context=soup.select('ul.cd-info-list > li ')
#     # list1=(x.text for x in context if len(x)!=0)
#     tags=['분야','응모대상','주최/주관','접수기간','총 상금','1등 상금','후원/협찬']
#     data_list=[]
#     for x,y in enumerate(context):
#         if y.text!='\n' and len(y.text) !=0:
#             a=y.text.replace('\t','').replace('\n','').strip('')
#             # for tag in tags:
#             #     a=a.replace(tag,'')    
#             data_list.append(a)
#     data_list[4]=data_list[4].split('D-')[0]
#     # for x in range(3):
#     #     del data_list[7]
#     data_list=[x for x in data_list if len(x) != 0]
#     final_list=[]
#     for x in data_list[0].split(', '):
#         a=[topic,x]
#         a.extend(data_list[1:])
#         final_list.append(a)
#     total_info.extend(final_list)
# DF=pd.DataFrame(total_info)
# for tag in tags:
#     DF=DF.applymap(lambda x:x.replace(tag,''))
# DF=DF.iloc[:,:-2]
# DF.drop(columns=[4],inplace=True)
# DF.loc[:,'접수시작']=DF[5].apply(lambda x:x.split('~')[0].strip())
# DF.loc[:,'접수마감']=DF[5].apply(lambda x:x.split('~')[1].strip())
# DF.drop(columns=[5],inplace=True)
# DF.columns=['name','category','qual','company','total_prize','first_prize','register_start','register_end']
# DF.to_csv('info.csv')

