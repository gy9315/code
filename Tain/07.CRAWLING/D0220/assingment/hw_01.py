import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate
from urllib.request import urlopen
import re
def find_company():
    url='https://finance.naver.com/sise/sise_market_sum.naver' 
    html=urlopen(url)
    soup=BeautifulSoup(html,'html.parser')
    info=soup.select('tr[onmouseover="mouseOver(this)"]')
    cname=[]
    curl=[]
    count=1
    for x in info:
        if count<=10:
            curl.append(x.a['href'])
            cname.append(x.a.text)
        count+=1
    print('-'*35)
    print('[네이버 코스피 상위 10대 기업 목록]')
    print('-'*35)
    count=1
    for x in cname:
        print(f'[{count}] {x}')
        count+=1
    return cname,curl

        
def attr_company(attr_html):
    html=urlopen(attr_html)
    soup=BeautifulSoup(html,'html.parser')
    a=soup.select('div#middle.new_totalinfo dl.blind')
    count=0
    list1=[]
    for x in a[0]:
        if x!='' or x!='\n':
            if count>=5 and count<=21 and count%2:
                list1.append(x.text.split(' ')[:2])
        count+=1
    # print(list1)
    return list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[7]
    # return  code,today_value,yester_value,current_value,high_value,low_value

def main():
    while True:
        a,b=find_company()
        attr_num=input('주가를 검색할 기업의 번호를 입력하세요:').strip()
        if attr_num.isnumeric():
            if 1<=int(attr_num)<=10:
                url=b[int(attr_num)-1]
                attr_html=f'https://finance.naver.com{url}'
                print(attr_html)
                name,code,today_value,yester_value,current_value,high_value,low_value=attr_company(attr_html)
                print(f'{name[0]}: {name[1]}')
                print(f'{code[0]}: {code[1]}')
                print(f'{today_value[0]}: {today_value[1]}')
                print(f'{yester_value[0]}: {yester_value[1]}')
                print(f'{current_value[0]}: {current_value[1]}')
                print(f'{high_value[0]}: {high_value[1]}')
                print(f'{low_value[0]}: {low_value[1]}')
            else:print("\033[31m잘못된 번호를 입력하였습니다. 다시 입력하세요\033[0m")
        elif attr_num=='-1':
            print('프로그램 종료')
            break
        else: 
            print("\033[31m잘못된 번호를 입력하였습니다. 다시 입력하세요\033[0m")

main()