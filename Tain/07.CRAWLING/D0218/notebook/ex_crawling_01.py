from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('http://www.pythonscraping.com/pages/page1.html')
bs=BeautifulSoup(html,'html.parser')
print(bs.find('h1'))
# print(bs.h1)
# print(bs.h1.string)
print(bs.h1.text)
# a태그에 접근
