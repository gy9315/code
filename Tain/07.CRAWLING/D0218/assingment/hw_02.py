from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
url=urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%8C%80%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=quote&tqi=iJdI5dpzLiwsssX1TX4ssssssmo-501029')
soup=BeautifulSoup(url,'html.parser')
# print(soup)
area=soup.select_one('div.title_area h2.blind')
small_area=soup.select_one('div.title_area span.select_txt_sub')
# print(small_area)
temp_info=soup.select('div.temperature_text strong')
# 현재온도 정보
temp=temp_info[0].text
# 날씨 상태
weather_info=soup.select('span.weather')
print(weather_info)
air_list=soup.select('ul.today_chart_list')
# 미세먼지 정보보
air_info=air_list[0].text
air_info=air_info.strip().split('    ')
# ----------------------------------------------------------
temp=soup.select_one('div.graph_inner._hourly_weather')
temp1=[]
for x in temp:
    for y in x.text.split('  '):
        if y!='' and y!=' ':
            temp1.append(y.strip())
print(temp1)
# ------------------------------------------------
print(f'{area.text}: {small_area.text[:-2]}')
print(f'현재온도: {temp_info[0].text}')
print(f'날씨상태: {weather_info[0].text}')
print(f'공기상태: ')
for x in air_info:
    print(x.strip())
print('-'*30)
print(f'{"시간대 별 날씨 및 온도":^22}')
print('-'*30)
for x,y,z in zip(temp1[::3],temp1[1::3],temp1[2::3]):
    if len(y)==4:
        print(f'{x:>5}{y:^8}{z:>4}')
    elif x.isalpha():
        print(f'{x:>4}{y:^10}{z:>4}')     
    else: print(f'{x:>5}{y:^10}{z:>4}')
    
    
            
    