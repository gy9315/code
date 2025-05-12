from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
url='https://m.cafe.daum.net/ygy2317/8Dzy/1813searchView=Y'
urlrequest=Request(url,headers={'user-agent':'mozilla/5.0'})
html=urlopen(urlrequest)
bs=BeautifulSoup(html,'html.parser')
print(bs)
