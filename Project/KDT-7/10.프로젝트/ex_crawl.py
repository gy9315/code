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
driver.get("https://m.cafe.daum.net/ygy2317")
input("")
count=0
posts=[]
for post_id in range(1813, 1979): 
    url=f'https://m.cafe.daum.net/ygy2317/8Dzy/{post_id}?searchView=Y'
    driver.get(url)
    time.sleep(2)
    try:
        article_element = driver.find_elements(By.XPATH, '//*[@id="article"]')
        for y,x in enumerate(article_element):
            text=x.text.strip()
            compile=re.compile(r'(.+)\s:\s(.*)(?=\n)')
            text=re.findall(compile,text)
            # print(f'post: {post_id},y: {y}')
            # print(text)
            # print('*'*100)
            posts.extend(text)
    except Exception as e:
        print(f"{post_id}실패: {e}")
# print(posts)
    count+=1
driver.quit()
post_list=[[x.strip(),re.sub(r'\([^)]*\)','',y)] for x,y in posts if len(re.sub(r'\([^)]*\)','',y))>1 and not '/' in x]
pd.DataFrame(post_list,columns=['인물','대사']).to_csv('sinario.csv',index=False)