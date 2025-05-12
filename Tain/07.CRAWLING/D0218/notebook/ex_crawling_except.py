from urllib.request import urlopen
from urllib.error import *
from bs4 import BeautifulSoup
try:
    html=urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
# HTTPError-> 객체
    print(e)
except URLError as e:
    print('the server could not be found!')
# else -> 정상작동 시 작동하는 조건
except Exception as e:
# 오류의 정보를 전부 담고 있는 Class=Exception
    print(e)
else: print('it worked')
        
bs=BeautifulSoup(html,'html.parser')
print(bs.find('h1'))
# print(bs.h1)
# print(bs.h1.string)
print(bs.h1.text)