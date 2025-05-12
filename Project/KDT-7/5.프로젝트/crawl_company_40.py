from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import pandas as pd

# 기업소개 년차 기업형태 매출액
# 업종
# 지역
# 평균연봉, 최저, 최고, ,2022년도 대비 연봉인상률,연봉신뢰도
# 매출액 정보
# ---------------------------------------------------------
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
# 기업정보 및 지역 불러오기 
DF=pd.read_csv('./DATA/company_list.csv',header=None)
total_company_name_attr=[]
for x in range(DF.shape[0]):
    company_name,region_name=list(DF.iloc[x])
# for x in range(1):
#     company_name,region_name=['아진산업(주)','경북']
# ---------------------------------------------------------
    xpath_dict = {'업력': '//*[@id="content"]/div/div[2]/section[2]/div[2]/div[2]/ul/li[1]/strong',          
                '기업형태': '//*[@id="content"]/div/div[2]/section[2]/div[2]/div[2]/ul/li[2]/div/button/strong',
                '사원수': '//*[@id="content"]/div/div[2]/section[2]/div[2]/div[2]/ul/li[3]/div/strong',
                '업종': '//*[@id="content"]/div/div[2]/section[2]/div[2]/div[2]/div/dl/div[1]/dd',
                '사업내용': '//*[@id="content"]/div/div[2]/section[2]/div[2]/div[2]/div/dl/div[4]/dd/p'}

    xpath_sdict = {'평균연봉': '//*[@id="tab_avg_salary"]/div/div[1]/div[2]/p/em',                      
                '최저연봉': '//*[@id="tab_avg_salary"]/div/div[1]/div[2]/div/span[2]/em',
                '최고연봉': '//*[@id="tab_avg_salary"]/div/div[1]/div[2]/div/span[4]/em',
                '22년 대비': '//*[@id="tab_avg_salary"]/div/div[1]/div[3]/dl[1]/dd/em',
                '연봉신뢰도': '//*[@id="tab_avg_salary"]/div/div[1]/div[3]/dl[3]/dd/span'}

    xpath_fdict = {'매출액': ['//*[@id="content"]/div/div[2]/section[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div/span[2]',
                        '//*[@id="content"]/div/div[2]/section[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/span[2]',
                        '//*[@id="content"]/div/div[2]/section[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/div/span[2]',
                        '//*[@id="content"]/div/div[2]/section[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/div[4]/div/span[2]'],                      
                '영업이익': ['//*[@id="content"]/div/div[2]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/span[2]',
                        '//*[@id="content"]/div/div[2]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div/span[2]',
                        '//*[@id="content"]/div/div[2]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[3]/div/span[2]',
                        '//*[@id="content"]/div/div[2]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[4]/div/span[2]']}    

    company_name_attr=[company_name]
    driver.get(f'https://www.saramin.co.kr/zf_user/search/company?searchType=auto&keydownAccess=&searchword={company_name}&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y')
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    urllist=[]
    # 기업정보 -> 기업찾아가기
    for x in soup.select('div.item_corp'):
        ddinfo=x.select('dl dt')
        for y in ddinfo:
            if y.text=='기업주소':
                a=y.next_sibling.next_sibling
                region=a.text
                b=bool(re.search(f'.*{region_name}.*',region))
                if b==True:
                    company=x.b
                    if x.a['title']==company_name:
                        urllist.append(x.a['href'])
                            
    # 기업정보
    #  5개 정보
    print(urllist)
    # --------------------------------------------
    company_url='https://www.saramin.co.kr'+urllist[0]
    # --------------------------------------------
    driver.get(company_url)
    html=urlopen(company_url)
    soup=BeautifulSoup(html,'html.parser')
    a=soup.select('ul.company_summary strong.company_summary_tit')
    list_company_attr5=['','','','','']
    for x in a:
        name=x.text.strip()
        if bool(re.search(r'.*\d+(년차)$',name)):
            list_company_attr5[0]=name
        elif bool(re.search(r'.*(업|기타)$',name)):
            list_company_attr5[1]=name
        elif bool(re.search(r'.*만원$',name))==False:
            check=re.search(r'\d+',name)
            a=re.search(r'\d+',name).group()
            list_company_attr5[2]=a+'명'
    a=soup.select('div.company_details_group')
    for x in a:
        if x.select_one('dt.tit').text=='업종':
            list_company_attr5[3]=x.select_one('dt.tit').next_sibling.next_sibling.text
        if x.select_one('dt.tit').text=='사업내용':
            b=x.select_one('dt.tit').next_sibling.next_sibling.select_one('p')['title']
            list_company_attr5[4]=b
        else: pass
    company_name_attr.extend(list_company_attr5)
    # --------------------------------------
    # 기업 상세정보 파악하기
    driver.get(company_url)
    for x in ['연봉정보','재무정보']:
        for y in range(1,7):
            path=f'//*[@id="content"]/div/div[1]/div/nav/ul/li[{y}]/button'
            try:
                a=driver.find_element(By.XPATH,path)
                print(a)
                if driver.find_element(By.XPATH,path).text==x:
                    detail_url=driver.find_element(By.XPATH,path).get_attribute('onclick').replace('window.location.href=','').replace(';','').strip("'")
                    # 
                    print(detail_url)
                    company_url=r'https://www.saramin.co.kr'+detail_url
                    break
                else: company_url=''
            except NoSuchElementException: company_url=''
        if x=='연봉정보':
            if len(company_url)>=1:
                print(company_url)
                driver.get(company_url)
            # 5개정보
                for x in range(len(xpath_sdict)):
                    try:
                        attr=driver.find_element(By.XPATH,xpath_sdict[list(xpath_sdict.keys())[x]]).text
                    except NoSuchElementException:
                        attr=''
                    company_name_attr.append(attr)
            else: company_name_attr.extend(['']*5)  
            # 8개정보
        # -------------------------------------------------------------------------------------------------
        else:
            if len(company_url)>=1: 
                driver.get(company_url)
                for x in range(len(xpath_fdict)):
                        for y in xpath_fdict[list(xpath_fdict.keys())[x]]:
                            try:
                                attr=driver.find_element(By.XPATH,y).text
                            except NoSuchElementException:
                                attr=''
                            company_name_attr.append(attr)
            else: company_name_attr.extend(['']*8)        
    total_company_name_attr.append(company_name_attr)
print(total_company_name_attr)
companyDF=pd.DataFrame(total_company_name_attr)
companyDF.columns=['기업명','엽력','기업형태','사원수','업종','사업내용','평균연봉','최저연봉','최고연봉','22년 대비 증감률','연봉신뢰도','매출액(2020)','매출액(2021)'
            ,'매출액(2022)','매출액(2023)','영업이익(2020)','영업이익(2021)','영업이익(2022)','영업이익(2023)']
companyDF.to_csv('company_attr.csv',encoding='utf-8')
driver.quit()