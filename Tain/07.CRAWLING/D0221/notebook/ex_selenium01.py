from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
driver=webdriver.Chrome()
driver.get('https://blog.naver.com/swf1004/221631056531')
driver.switch_to.frame('mainFrame')
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
frame=soup.select('div.se-module')
list1=[]
for x in frame:
    a=x.text.replace('\n','')
    print(a)
    list1.append(a)
