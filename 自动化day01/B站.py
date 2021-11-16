from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开搜狗浏览器进入B站
driver = webdriver.Chrome()

try:
    # 进入B站并最大化窗口
    driver.get(r'http://www.bilibili.com/')
    driver.maximize_window()
    # 等待5秒
    time.sleep(5)

    # 搜索并点击
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div/form/input').send_keys('我的音乐你听吗')
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div/form/div').click()

    # 并转换所在窗口
    driver.switch_to.window(driver.window_handles[1])

    # 点击播放
    driver.find_element(By.XPATH,
                        '/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul[1]/li/div/div/div[3]/ul/li[1]/a/div/div[1]').click()
    time.sleep(5)

    # 切换窗口并点击登录
    driver.switch_to.window(driver.window_handles[2])

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/span[1]/div/span/div').click()

    # 切换窗口并点击QQ登录
    driver.switch_to.window(driver.window_handles[3])
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div[3]/div/div/div/div[6]/a[2]').click()
    time.sleep(5)

    # 点击账号密码登录输入账号密码
    driver.switch_to.frame('ptlogin_iframe')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[9]/a[1]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div[3]/form/div[1]/div/input').send_keys('1539533097')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div[3]/form/div[2]/div[1]/input').send_keys('2167365108@li')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div[3]/form/div[4]/a/input').click()
    time.sleep(5)

    # 切换到当前窗口并点赞
    driver.switch_to.window(driver.window_handles[3])
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[4]/div[1]/div[1]/i').click()

    # 关闭
    time.sleep(10)
    driver.quit()

except Exception as e:
    print('error:', e)
finally:
    time.sleep(3)
    driver.quit()


