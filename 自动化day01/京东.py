from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开浏览器进入京东
driver = webdriver.Chrome()
driver.get(r'https://www.jd.com')
# 最大化窗口
driver.maximize_window()

# 输入笔记本并搜索
driver.find_element(By.ID, 'key').send_keys('笔记本')
driver.find_element(By.XPATH, "//*[@clstag='h|keycount|head|search_a']").click()

# 下拉窗口
js = 'window.scrollTo(0,300)'
driver.execute_script(js)

# 等待3秒
time.sleep(3)
# 加入购物车
driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]").click()
time.sleep(3)
driver.quit()
