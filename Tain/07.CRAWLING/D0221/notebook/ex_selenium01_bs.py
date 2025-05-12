from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
url='https://blog.naver.com/swf1004/221631056531'
html=urlopen(url)
soup=BeautifulSoup(html,'html.parser')
# 동적컨텐츠는 urlopen해도 확인할 수 없음
print(soup.select('iframe'))
# frame=soup.select('div.se-module')
# list1=[]
# for x in frame:
#     a=x.text.replace('\n','')
#     print(a)
#     list1.append(a)
