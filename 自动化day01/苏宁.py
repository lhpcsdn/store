from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 打开搜狗浏览器进入苏宁
driver = webdriver.Chrome()
driver.get(r'https://www.suning.com/')
# 最大化窗口
driver.maximize_window()

# 输入并搜索
driver.find_element(By.XPATH, '//*[@id="searchKeywords"]').send_keys('笔记本')
driver.find_element(By.XPATH, '//*[@id="searchSubmit"]').click()

# 等待5秒，加入购物车
time.sleep(5)
driver.find_element(By.XPATH, '//*[@name="ssdsn_search_pro_buy02-1_0_0_12316056406_0000000000"]').click()

time.sleep(3)
driver.quit()
