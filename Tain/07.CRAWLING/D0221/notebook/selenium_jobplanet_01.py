"""
잡플래닛 회사 평점 크롤링
- 전체 평점
- 복지 및 급여
- 업무와 삶의 균형 등

회사명: class=name

https://www.jobplanet.co.kr/companies/30139/reviews/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90

https://wikidocs.net/149338 

"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys  import Keys
import pandas as pd
from tabulate import tabulate

company_dict = {'삼성전자':'https://www.jobplanet.co.kr/companies/30139/reviews/삼성전자',
                 'LG전자':'https://www.jobplanet.co.kr/companies/19514/reviews/lg전자',
                 'SK하이닉스':'https://www.jobplanet.co.kr/companies/20561/reviews/에스케이하이닉스',
                 '네이버':'https://www.jobplanet.co.kr/companies/42217/reviews/네이버'}

xpath_dict = {'전체평점': '//*[@id="premiumReviewStatistics"]/div/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]',                      
              '복지': '//*[@id="premiumReviewStatistics"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/span[2]',
              '워라벨': '//*[@id="premiumReviewStatistics"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/span[2]',
              '사내문화': '//*[@id="premiumReviewStatistics"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/span[2]',
              '승진 기회': '//*[@id="premiumReviewStatistics"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[4]/div[2]/span[2]',
              '경영진': '//*[@id="premiumReviewStatistics"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/span[2]'}

user_id = '잡플래닛 id(이메일주소)'
passwd = '로그인패스워드'

def  login(driver, user_id, pwd):
    driver.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")
    time.sleep(1)

    # 아이디 입력
    login_id  =  driver.find_element(By.ID,  "user_email")
    login_id.send_keys(user_id)

    # 비밀번호 입력
    login_pwd  =  driver.find_element(By.ID,  "user_password")
    login_pwd.send_keys(pwd)

    # 로그인 버튼 클릭
    login_id.send_keys(Keys.RETURN)
    time.sleep(5)


def get_review_score(driver):
    
    compary_score_dict = {}
    for company_name in company_dict.keys():
        score_list = []
        company_url = company_dict.get(company_name)
        driver.get(company_url)
        time.sleep(2)
        # 회사 이름 가져오기
        company = driver.find_element(By.XPATH, '//*[@id="companyName"]/a').text

        print('-' * 80)
        #print(company_name)
        print(company)

        for key in xpath_dict.keys():
            # 전체 5개의 평점 가져오기
            point = driver.find_element(By.XPATH, xpath_dict.get(key)).text        
            print(f'{key}: {point}', end=' ')            
            score_list.append(point)

        print()
        print('-' * 80)
        # 딕셔너리에 모든 평점 추가하기
        compary_score_dict[company_name] = score_list


    print('company_score_dict')
    for key in compary_score_dict.keys():
        print(f'{key}: {compary_score_dict.get(key)}')

    # 딕셔너리를 DataFrame으로 변환
    columns=('전체평점', '복지', '워라벨',
            '사내문화', '승진 기회', '경영진')

    # orient='index': 딕셔너리의 키가 행의 색인이 되고
    # 딕셔너리의 값이 행의 데이터가 됨
    company_score_df = pd.DataFrame.from_dict(compary_score_dict,
                                            orient='index', columns=columns)

    print(tabulate(company_score_df, headers='keys', tablefmt='psql'))
    #company_score_df.to_excel('company_scores.xlsx', index=False)
    company_score_df.to_csv('company_scores.csv', index=False, mode='w', encoding='utf-8-sig')

    

def main():

    driver = webdriver.Chrome()

    # login(driver, user_id, passwd)
    get_review_score(driver)

    time.sleep(5)
    driver.close()


main()

