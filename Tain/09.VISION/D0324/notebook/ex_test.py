from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# 좌표 (지도 내 offset 위치로 조정 필요함)
click_offset_x = 400
click_offset_y = 300

driver = webdriver.Chrome()
driver.get("www.naver.com")  # 분석 페이지 직접 URL로 바꾸세요
driver.maximize_window()
time.sleep(5)

# # 지점 선택 버튼 클릭
# select_button = driver.find_element(By.ID, "selectPoint_bldg03")
# select_button.click()
# time.sleep(2)

# # 지도 클릭
# map_area = driver.find_element(By.ID, "map")  # 정확한 ID나 className 필요 시 확인
# actions = ActionChains(driver)
# actions.move_to_element_with_offset(map_area, click_offset_x, click_offset_y).click().perform()
# time.sleep(2)

# # 선택종료 및 분석 클릭
# analyze_button = driver.find_element(By.ID, "bldg03-finishSet")
# analyze_button.click()
# time.sleep(5)

# # 분석 결과 추출
# total_sunlight = driver.find_element(By.CLASS_NAME, "continuetime").text
# print(f"총 일조량: {total_sunlight}")

# driver.quit()
