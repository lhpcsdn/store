'''
任务1：
    完成新浪微博的，
    首页面，发现，视频，消息，我自动化框架开发。
'''

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

url = "127.0.0.1:4723/wd/hub"

param = {
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.sina.weibo",
    "appActivity": "com.sina.weibo.SplashActivity"
}

driver = webdriver.Remote(url, param)

print(driver)
time.sleep(10)

# 点击并进入主页面
el19 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]")
el19.click()
time.sleep(5)

# 点击首页点赞
el1 = driver.find_element_by_accessibility_id("首页")
el1.click()
time.sleep(5)
el2 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"喜欢\"])[3]")
el2.click()
time.sleep(5)

# 点击视频切换视频并点赞
el3 = driver.find_element_by_accessibility_id("视频")
el3.click()
time.sleep(5)
TouchAction(driver).press(x=420, y=1056).move_to(x=438, y=403).release().perform()
time.sleep(5)
el4 = driver.find_element_by_id("com.sina.weibo:id/story_new_footer_like")
el4.click()
time.sleep(5)

# 点击发现并滑动
el5 = driver.find_element_by_accessibility_id("发现")
el5.click()
TouchAction(driver).press(x=430, y=1365).move_to(x=435, y=449).release().perform()
time.sleep(5)

# 点击消息再退出
el8 = driver.find_element_by_accessibility_id("消息")
el8.click()
time.sleep(5)
el9 = driver.find_element_by_id("com.sina.weibo:id/iv_title_back")
el9.click()
time.sleep(5)

# 进入我页面点击授权同意
el14 = driver.find_element_by_accessibility_id("我")
el14.click()
time.sleep(5)
el15 = driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol")
el15.click()
time.sleep(5)

# 输入账号验证码后退出
el16 = driver.find_element_by_id("com.sina.weibo:id/et_login_view_phone")
el16.send_keys("123456789")
time.sleep(5)
el17 = driver.find_element_by_id("com.sina.weibo:id/et_login_view_sms")
el17.send_keys("1234")
time.sleep(5)
el18 = driver.find_element_by_id("com.sina.weibo:id/iv_title_back")
el18.click()
time.sleep(5)

print('ok')
