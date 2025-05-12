from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://www.pythonscraping.com/pages/page3.html')
soup=BeautifulSoup(html,'html.parser')
table_tag=soup.select_one('table#giftList')
print(f'children의 개수: {len(list(table_tag.children))}')
count=0
contents=[]
for x in table_tag.children:
    count+=1
    contents.append(x)
    print(f'{count}: {x}')
    print('-'*30)