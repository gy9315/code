from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import urllib.error as error  
query='chatgpt'
html=urlopen(f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={query}')
soup=BeautifulSoup(html,'html.parser')
# -----------------------------------------------------------------
# 정보수집

titles=soup.select('div.title_area > a')
info=soup.select('div.dsc_area')
count=len(titles)
for x in range(count):
    title=titles[x].text
    url=titles[x]['href']
    info1=info[x].text
    print(f'{title} [{url}]')
    print(info1)
    print('*'*80)