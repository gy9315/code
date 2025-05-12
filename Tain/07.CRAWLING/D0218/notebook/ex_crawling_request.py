from requests import *
from bs4 import BeautifulSoup
url='http://www.pythonscraping.com/pages/page1.html'
html=get(url)
print(f'html encoding: {html.encoding}')
print(html.text)
# print(html)
bs=BeautifulSoup(html,'html.parser')
print(bs.h1.string)
