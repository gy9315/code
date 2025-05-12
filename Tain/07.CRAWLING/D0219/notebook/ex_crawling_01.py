from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
soup=BeautifulSoup(html,'html.parser')
person=soup.select('span.green')
for x in person:
    a=x.text
    print(a)
a=soup.find_all(string='the prince')
print(f'the prince count: {len(a)}')