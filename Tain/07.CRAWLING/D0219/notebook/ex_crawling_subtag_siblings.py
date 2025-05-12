from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://www.pythonscraping.com/pages/page3.html')
soup=BeautifulSoup(html,'html.parser')
table_tag=soup.select_one('table#giftList')
print(f'children의 개수: {len(list(table_tag.children))}')
count=0
contents=[]
print(f'descendants : {len(list(table_tag.descendants))}')
for x in table_tag.descendants:
    count+=1
    print(f'{count}\n{x}')

for x in table_tag.tr.next_siblings:
    print(x)
    print('-'*30)


print(soup.select_one('tr#gift3').next_sibling)
print(ord(soup.select_one('tr#gift3').next_sibling))

print(soup.select_one('tr#gift3').next_sibling.next_sibling)