from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen('https://www.pythonscraping.com/pages/page3.html')
soup=BeautifulSoup(html,'html.parser')
img_tag=re.compile(r'/img/gifts/img.*.jpg')
images=soup.find_all('img',{'src':img_tag})
print(images)