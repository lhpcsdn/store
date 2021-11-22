from appium import webdriver
import time


class HomePage:
    # 保证driver使用全局同一个
    def __init__(self, driver):
        self.driver = driver

    # 登录
    def login(self, phone, password):
        # 进入我页面点击授权同意
        self.driver.find_element_by_accessibility_id("我").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol").click()
        time.sleep(2)

        # 输入账号验证码
        self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_phone").send_keys("123456789")
        self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_sms").send_keys("123456")
        self.driver.find_element_by_id("com.sina.weibo:id/btn_login_view_sms").click()
        time.sleep(6)

        # 获取失败的结果数据
        result = self.driver.find_element_by_id("com.sina.weibo:id/tv_login_view_tips").text
        return result

    # # 获取失败的结果数据
    # def getLoginErrorResult(self):
    #     return self.driver.find_element_by_id("com.sina.weibo:id/tv_login_view_tips").text

    # 首页
    def home(self):
        # 点击首页
        self.driver.find_element_by_accessibility_id("首页").click()
        time.sleep(6)
        # 获取结果
        result = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView").text
        return result

    # 视频
    def video(self):
        # 点击视频
        self.driver.find_element_by_accessibility_id("视频").click()
        time.sleep(6)
        # 获取结果
        result = self.driver.find_element_by_id("com.sina.weibo:id/followAnimView").text
        return result

    # 发现
    def discover(self):
        # 点击发现
        self.driver.find_element_by_accessibility_id("发现").click()
        time.sleep(6)
        # 获取结果
        result = self.driver.find_element_by_id("com.sina.weibo:id/textView_title").text
        return result

    # 消息
    def news(self):
        # 点击消息
        self.driver.find_element_by_accessibility_id("消息").click()
        time.sleep(6)
        # 获取结果
        result = self.driver.find_element_by_id("com.sina.weibo:id/tv_help").text
        return result
