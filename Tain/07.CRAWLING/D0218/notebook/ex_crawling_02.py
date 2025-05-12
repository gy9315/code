from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request
html=urlopen('https://www.daangn.com/hot_articles')
bs=BeautifulSoup(html,'html.parser')
print(bs.find('h1'))

print(bs.h1.text)