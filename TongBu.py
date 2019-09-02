import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from processor import Processor

# 滑动点
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700
# 滑动间隔
SCROLL_SLEEP_TIME = 1
# 等待元素加载时间
TIMEOUT = 300

class WeChat(object):
    def __init__(self):
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "MI_5",
            "appPackage": "com.tencent.mm",
            "appActivity": ".ui.LauncherUI",
            "noReset": "True"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(1000)

    # 弃用
    # def login(self):
    #     print('开始登陆')
    #     loginBtn = self.driver.find_element_by_id("com.tencent.mm:id/edu")
    #     loginBtn.click()
    #
    #     print('录入账号')
    #     phoneEdt = self.driver.find_element_by_id("com.tencent.mm:id/li")
    #     phoneEdt.send_keys("17308053023")
    #
    #     print('点击下一步')
    #     loginNext = self.driver.find_element_by_id("com.tencent.mm:id/b0f")
    #     loginNext.click()
    #     sleep(4)
    #
    #     print('输入密码')
    #     passwordEdt = self.driver.find_element_by_xpath(
    #         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
    #     passwordEdt.send_keys("Aa123456")
    #
    #     print('登录---->')
    #     loginBtn = self.driver.find_element_by_id("com.tencent.mm:id/b0f")
    #     loginBtn.click()
    #     sleep(5)

    # 添加好友
    def addFriends(self):
        sleep(30)
        print('点击- + --->')
        add = self.driver.find_element_by_id("com.tencent.mm:id/qk")
        add.click()

        print('点击添加好友')
        addLayout = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]")
        addLayout.click()

        goSearch = self.driver.find_element_by_id("com.tencent.mm:id/li")
        goSearch.click()

        searchEdt = self.driver.find_element_by_id("com.tencent.mm:id/li")
        searchEdt.send_keys("jackli674297026")

        searchBtn = self.driver.find_element_by_id("com.tencent.mm:id/ra")
        searchBtn.click()
        sleep(30)

        # 获取地区
        localTxt = self.driver.find_element_by_id("	com.tencent.mm:id/b82").text
        self.location = localTxt

        goMarkPage = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout")
        goMarkPage.click()

        friendName = self.driver.find_element_by_id("com.tencent.mm:id/b8p")
        self.name = friendName
        print('friendName' + friendName)

        markPageBack = self.driver.find_element_by_accessibility_id("返回")
        markPageBack.click()

        print("添加好友")
        addFriends = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout")
        addFriends.click()

        addFriendsBack = self.driver.find_element_by_accessibility_id("返回")
        addFriendsBack.click()

        searchPageBack = self.driver.find_element_by_accessibility_id("返回")
        searchPageBack.click()

        goHome = self.driver.find_element_by_accessibility_id("返回")
        goHome.click()

    def enter(self):
        # 选项卡
        # tab = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/bq"]/android.widget.LinearLayout/android.widget.RelativeLayout[3]')))
        tab = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="发现"]')))
        tab.click()
        # 朋友圈
        moments = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@text="朋友圈"]')))
        moments.click()

    def crawl(self):
        """
        爬取
        :return:
        """
        while True:
            # 当前页面显示的所有状态
            # items = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/cve"]//android.widget.FrameLayout')))
            items = self.wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, '//android.widget.FrameLayout[@content-desc="当前所在页面,朋友圈"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView//android.widget.FrameLayout')))

            # 上滑
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            # 遍历每条状态
            for item in items:
                try:
                    # 昵称
                    nickname = item.find_element_by_id('com.tencent.mm:id/b9i').get_attribute('text')
                    # 正文
                    content = item.find_element_by_id('com.tencent.mm:id/eua').get_attribute('text')
                    # 日期
                    date = item.find_element_by_id('com.tencent.mm:id/ep0').get_attribute('text')
                    # 处理日期
                    date = self.processor.date(date)
                    print(nickname, content, date)
                    # data = {
                    #     'nickname': nickname,
                    #     'content': content,
                    #     'date': date,
                    # }
                    # 插入MongoDB
                    # self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
                    sleep(SCROLL_SLEEP_TIME)
                except NoSuchElementException:
                    pass


if __name__ == '__main__':
    weChat = WeChat()
    wechat.enter()
    wechat.crawl()