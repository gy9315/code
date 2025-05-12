
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.request import urlopen
import re
url='https://finance.naver.com/item/main.naver?code=000660' 
html=urlopen(url)
soup=BeautifulSoup(html,'html.parser')
a=soup.select('div#middle.new_totalinfo dl.blind')
count=0
list1=[]
for x in a[0]:
    if x!='' or x!='\n':
        if count>=5 and count<=21 and count%2:
            list1.append(x.text.split(' ')[:2])
    count+=1
print(list1)