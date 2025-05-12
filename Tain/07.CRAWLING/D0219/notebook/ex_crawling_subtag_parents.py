from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://www.pythonscraping.com/pages/page3.html')
soup=BeautifulSoup(html,'html.parser')
table_tag=soup.select_one('table#giftList')
style_tag=soup.style
# print(style_tag.parent)

img=soup.select_one('#gift1 > td:nth-child(4) > img')
a=img.parent.previous_sibling.text.split('\n')[1]
print(a)