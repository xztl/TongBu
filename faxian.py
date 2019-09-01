from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re

# 滑动点
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700
# 滑动间隔
SCROLL_SLEEP_TIME = 1
# 等待元素加载时间
TIMEOUT = 300


driver_server = 'http://127.0.0.1:4723/wd/hub'


class WeChatSpider():
    def __init__(self):
        self.desired_caps = {
              "platformName": "Android",
              "deviceName": "127.0.0.1:62001",
              "appPackage": "com.tencent.mm",
              "appActivity": ".ui.LauncherUI",
              "noReset": True,
              "resetKeyboard": True
        }
        self.driver = webdriver.Remote(driver_server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 300)

    def enter(self):
        # 选项卡
        tab = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/bq"]/android.widget.LinearLayout/android.widget.RelativeLayout[3]')))
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
            items = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/cve"]//android.widget.FrameLayout')))
            # 上滑
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            # 遍历每条状态
            for item in items:
                try:
                    # 昵称
                    nickname = item.find_element_by_id('com.tencent.mm:id/aig').get_attribute('text')
                    # 正文
                    content = item.find_element_by_id('com.tencent.mm:id/cwm').get_attribute('text')
                    # 日期
                    date = item.find_element_by_id('com.tencent.mm:id/crh').get_attribute('text')
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
if __name__ == "__main__":
    wechat = WeChatSpider()
    wechat.enter()
    wechat.crawl()