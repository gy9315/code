from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
driver.implicitly_wait(10)
name=driver.find_elements(By.CLASS_NAME, "green")
for x in name:
    print(x.text)
time.sleep(10)
driver.quit()