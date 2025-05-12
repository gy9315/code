from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlopen
import re
import time
import os
import requests

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  
driver=webdriver.Chrome(options=options)
hrefs=set()
for x in range(1,34):
    url=f'https://www.kbchachacha.com/public/search/themeList.kbc?themeSeq=413#!?page={x}&sort=-orderDate&makerCode=102'
    driver.get(url)
    time.sleep(3)
    link_elements=driver.find_elements(By.CSS_SELECTOR, "div.item a.link")
    base_url = "https://www.kbchachacha.com"
    for el in link_elements:
        href = el.get_attribute("href")
        if href:
            hrefs.add(href if href.startswith("http") else base_url + href)
print(hrefs)
driver.quit()

options=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=options)
for url in hrefs:
    driver.get(url)
    time.sleep(2)
    car_name_element=driver.find_element(By.CSS_SELECTOR, "strong.car-buy-name")
    car_name_text_raw=car_name_element.text.replace("\n", " ").strip()
    car_name_text = ''.join(
        ch.lower() if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z' else ch
        for ch in car_name_text_raw
    )
    kia_models = [
        "모닝", "비스토", "프라이드", "k2", "세피아", "k3", "k4", "씨드", "스펙트라", "EV4", "스팅어",
        "k5", "k7", "k8", "엔터프라이즈", "오피러스", "k9", "엘란", "스토닉", "KX1", "쏘넷", "시로스",
        "레토나", "니로", "셀토스", "EV3", "스포티지", "EV6", "EV5", "쏘렌토", "모하비", "EV9",
        "카니발", "카렌스", "레이"
    ]
    matched_model = None
    for model in kia_models:
        if model.lower() in car_name_text:
            matched_model = model
            break

    if matched_model:
        base_prefix=matched_model
    else:
        base_prefix = re.sub(r"[^\w가-힣]", "_", car_name_text_raw)
    save_dir=f"./kia_images/{base_prefix}"
    os.makedirs(save_dir, exist_ok=True)
    existing_files=os.listdir(save_dir)
    pattern=re.compile(rf"^{re.escape(base_prefix)}\((\d+)\)_\d\.jpeg$")
    existing_counts=[
        int(match.group(1)) for filename in existing_files if (match := pattern.match(filename))
    ]
    next_count=max(existing_counts, default=0) + 1
    file_prefix=f"{base_prefix}({next_count})"
    image_elements=driver.find_elements(By.CSS_SELECTOR, 'div.page01 a[data-slide-index] img')
    for img in image_elements:
        index=img.find_element(By.XPATH, "..").get_attribute("data-slide-index")
        if index in ["1", "2", "3", "4"]:
            img_url=img.get_attribute("src")
            file_path=os.path.join(save_dir, f"{file_prefix}_{index}.jpeg")
            try:
                response=requests.get(img_url)
                if response.status_code==200:
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                else:
                    print(f"다운로드 실패: {img_url}")
            except Exception as e: pass
driver.quit()
