# coding=gbk
import selenium
from appium import webdriver, common
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class WeChatTest(object):
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
        self.name = ""
        self.sex = ""
        self.location = ""
        self.weChatNum = ""

    def login(self):
        print('开始登陆')
        loginBtn = self.driver.find_element_by_id("com.tencent.mm:id/edu")
        loginBtn.click()

        print('录入账号')
        phoneEdt = self.driver.find_element_by_id("com.tencent.mm:id/li")
        phoneEdt.send_keys("17308053023")

        print('点击下一步')
        loginNext = self.driver.find_element_by_id("com.tencent.mm:id/b0f")
        loginNext.click()
        sleep(4)

        print('输入密码')
        passwordEdt = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
        passwordEdt.send_keys("Aa123456")

        print('登录---->')
        loginBtn = self.driver.find_element_by_id("com.tencent.mm:id/b0f")
        loginBtn.click()
        sleep(5)

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
        searchEdt.send_keys("shouji132212681089")

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

    # 爬取指定朋友的数据
    def getFriendMsg(self):
        # 先找到好友
        huiHua = self.driver.find_elements_by_id('com.tencent.mm:id/b9i')
        for item in huiHua:
            if '二之日' in item.text:
                # 找到联系人打开聊天室
                item.click()
                sleep(5)
                # 找到联系人信息界面
                openInfo = self.driver.find_element_by_accessibility_id("聊天信息")
                openInfo.click()
                # 点击头像
                headImg = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[@content-desc=\"当前所在页面,聊天信息\"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
                headImg.click()
                # 点击朋友圈相册
                friendPhoto = self.driver.find_element_by_xpath("//*[@text='朋友圈']")
                TouchAction(self.driver).tap(friendPhoto).perform()
                sleep(10)
                # 开始抓取朋友圈数据 内容ID com.tencent.mm:id/or      item点击： 	com.tencent.mm:id/ers
                diction = dict()
                currItem = dict()
                # 开始循环拿列表
                while True:
                    flag = True
                    self.driver.swipe(500, 800, 500, 500, 2000)
                    sleep(5)
                    # 拿到所有的的标题 bounds
                    infoList = self.driver.find_elements_by_id('com.tencent.mm:id/or')
                    for info in infoList:
                        print(info.text)

    # 获取好友列表
    def getFriendListMsg(self):
        # 点击朋友圈
        friendPage = self.driver.find_element_by_xpath("//*[@text='通讯录']")
        TouchAction(self.driver).tap(friendPage).perform()
        # 定义数据集合
        friendCollection = dict()
        # 获取所有的联系人昵称

        while True:
            flag = True
            self.driver.swipe(500, 800, 500, 500, 2000)
            friendList = self.driver.find_elements_by_id('com.tencent.mm:id/ol')
            for friend in friendList:
                friendName = friend.text
                doesItExist = False
                for item in friendCollection:
                    if item in friendName:
                        doesItExist = True
                if not doesItExist:
                    friendCollection[friendName] = friend

            try:
                self.driver.find_element_by_id('com.tencent.mm:id/b3o')
                print('朋友列表获取完成')
                flag = False
            except Exception:
                pass

            if flag is False:
                break
        #  获取列表成功 开始循环点击进入
        print(friendCollection)

    # 直接爬取朋友圈的
    def crawl(self):
        sleep(2)
        # 点击发现
        findPage = self.driver.find_element_by_xpath("//*[@text='发现']")
        self.touch_tap(findPage.location.get('x'), findPage.location.get('y'))
        sleep(2)
        # 点击朋友圈
        goFriendPage = self.driver.find_element_by_xpath("//*[@text='朋友圈']")
        self.touch_tap(goFriendPage.location.get('x'), goFriendPage.location.get('y'))
        sleep(2)

        dataCollection = dict()

        while True:
            flag = True
            self.verticalScrolling()
            itemArr = self.driver.find_elements_by_id("com.tencent.mm:id/eu7")
            for item in itemArr:
                nickname = item.find_element_by_id('com.tencent.mm:id/b9i').text
                # 正文
                content = item.find_element_by_id('com.tencent.mm:id/eua').text
                # 查找该条记录是否存在
                # findItemExist(dataCollection, nickname, content)
                # 图片  视频： content-desc = 图片
                try:
                    contentGroup = item.find_element_by_id("com.tencent.mm:id/eow")
                    # contentGroup.click()
                    self.touch_tap(contentGroup.location.get('x') + 50, contentGroup.location.get('y') + 50)
                    sleep(2)
                    activityName = self.driver.current_activity
                    # .plugin.sns.ui.SnsBrowseUI'(图片)
                    # .plugin.webview.ui.tools.WebViewUI（链接）
                    # '.plugin.sns.ui.SnsOnlineVideoActivity（视频）' 打开的是链接
                    if "WebViewUI" in activityName:
                        self.driver.find_element_by_accessibility_id("返回").click()
                    # 打开的是图片的
                    if "SnsBrowseUI" in activityName:
                        self.save_img()
                    if "SnsOnlineVideoActivity" in activityName:
                        self

                    flag = False
                except Exception:
                    print(nickname + "没有图片和视频")
                    pass

    # 获取设备保存朋友圈的文件
    def getWeChatFile(self):
        # 保存的图片文件夹 adb pull <手机目录> <电脑目录>
        os.system("adb pull /sdcard/tencent/MicroMsg/WeiXin/  e:/aa")

    def save_img(self):
        # com.tencent.mm:id/dgy 小圆点
        try:
            # 查找小圆点的父类容器
            iconArr = self.driver.find_elements_by_id("com.tencent.mm:id/dgy")
            if len(iconArr) > 0:
                for item in iconArr:
                    # 长按
                    imageView = self.driver.find_element_by_class_name("android.widget.ImageView")
                    TouchAction(self.driver).long_press(imageView, 1000).wait(2000).perform()
                    self.driver.find_element_by_xpath("//*[@text='保存图片']").click()
                    # 保存当前时间戳
                    sleep(1)
                    # 滑动下一张
                    self.horizontalScrolling()
                self.driver.find_element_by_class_name("android.widget.ImageView").click()
                sleep(5)
            else:
                imageView = self.driver.find_element_by_class_name("android.widget.ImageView")
                TouchAction(self.driver).long_press(imageView, imageView.location.get('x'), imageView.location.get('y'),
                                                    1000)
        except NoSuchElementException:
            imageView = self.driver.find_element_by_class_name("android.widget.ImageView")
            TouchAction(self.driver).long_press(imageView, imageView.location.get('x'), imageView.location.get('y'),
                                                1000)

    def touch_tap(self, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
        '''
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
        '''
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        self.driver.tap([(x1, y1), (x1, y1)], duration)

    # 横向滚动界面
    def horizontalScrolling(self):
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        self.driver.swipe(screen_width * 0.8, screen_height / 2, screen_width * 0.1, screen_height / 2, 2000)

    # 竖向滚动界面
    def verticalScrolling(self):
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        sleep(2)
        self.driver.swipe(screen_width / 2, screen_height * 0.6, screen_width / 2, screen_height * 0.4, 2000)

    def findElement(self):
        try:
            WebDriverWait(self.driver, common.WAIT_TIME, 1).until(
                self.driver.find_element_by_id('com.tencent.mm:id/eqp'))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            return False


if __name__ == '__main__':
    weChat = WeChatTest()
    # weChat.getFriendMsg()
    # weChat.addFriends()
    weChat.crawl()
