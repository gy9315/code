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
temp_total=soup.select('div.forecast_wrap')
air_info=air_info.strip().split('    ')
time_temp_info=[]
# ----------------------------------------------------------
for x in temp_total:
    count=0
    for y in x.text:
        if y.strip()!='':
            time_temp_info.append(y.strip())
time_temp_info=time_temp_info[13:time_temp_info[13:].index('이')]
time_temp_info=''.join(time_temp_info)
time_temp_info=time_temp_info.split('°')
time_temp_info1=[]

for x in time_temp_info:
    time_temp_info1.append(x+'°')
print(time_temp_info1)
time=[]
cloud=[]
temp=[]
for x in time_temp_info1:
    if x[0].isnumeric() and '시' in x:
        time.append(x[:3])
        if '맑음' in x[3:] or '흐림' in x[3:]:
            cloud.append(x[3:5])
            temp.append(x[5:])
        elif '구름많음' in x[3:]:
            cloud.append(x[3:7])
            temp.append(x[7:])
        elif '비' in x[3:] or '눈' in x[3:]:
            cloud.append(x[3])
            temp.append(x[4:])
    elif x[0].isalpha():
        time.append(x[:2])
        if '맑음' in x[2:] or '흐림' in x[2:]:
            cloud.append(x[2:4])
            temp.append(x[4:])
        elif '구름많음' in x[2:]:
            cloud.append(x[2:6])
            temp.append(x[7:])
        elif '비' in x[2:] or '눈' in x[2:]:
            cloud.append(x[2])
            temp.append(x[3:])
    else:
        time.append(x[:6])
        if '맑음' in x[6:] or '흐림' in x[6:]:
            cloud.append(x[6:8])
            temp.append(x[8:])
        elif '구름많음' in x[6:]:
            cloud.append(x[6:10])
            temp.append(x[10:])
        elif '비' in x[6:] or '눈' in x[6:]:
            cloud.append(x[6])
            temp.append(x[7:])
# ------------------------------------------------
print(f'{area.text}: {small_area.text[:-2]}')
print(f'현재온도: {temp_info[0].text}')
print(f'날씨상태: {weather_info[0].text}')
print(f'공기상태: ')
for x in air_info:
    print(x.strip())
print('-'*30)
print(f'{"시간대 별 날씨 및 온도":^30}')
print('-'*30)
for x,y,z in zip(time,cloud,temp):
    print(f'{x.strip():>6}  {y:>4}  {z:>5}')


    
            
    