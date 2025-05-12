from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
soup=BeautifulSoup(html,'html.parser')
body_contents=soup.find('div#bodyContent')
pattern='^(/wiki/)((?!:))'