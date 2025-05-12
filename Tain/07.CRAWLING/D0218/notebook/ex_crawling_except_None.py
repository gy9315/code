from urllib.request import urlopen
from urllib.error import *
from bs4 import BeautifulSoup


def get_title(url,tag):
    try:
        html=urlopen(url)
        bs=BeautifulSoup(html,'html.parser')
        value=bs.find(tag)
    except HTTPError as e:
    # HTTPError-> 객체
        return None
    except AttributeError as e:
        print(e)
        return None
    # else -> 정상작동 시 작동하는 조건
    else: return value
    
tag='h1'
url='http://www.pythonscraping.com/pages/page1.html'
value=get_title(url,tag)
if value==None:
    print(f'{tag} could not be found')
else: 
    print(value)
    
# html1=urlopen(url)
# bs=BeautifulSoup(html1,'html.parser')
# print(bs.h1)