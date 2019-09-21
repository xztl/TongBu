# coding=gbk
import selenium
from appium import webdriver, common
from time import sleep, time
from appium.webdriver.common.touch_action import TouchAction
import os
import time
import re

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
        self.driver.implicitly_wait(5)
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

        rex = re.compile('[^\u4e00-\u9fa5^a-z^A-Z^0-9]')
        # 收集信息的集合 {userName : [{content:说说内容 type:"1 照片 2 视频 3 地址" ,photo:[时间戳,时间戳,时间戳],video:时间戳,webUrl:地址}]}
        dataCollection = dict()

        while True:
            flag = True
            self.verticalScrolling(0.6, 0.4)
            itemArr = self.driver.find_elements_by_id("com.tencent.mm:id/eu7")
            for item in itemArr:
                try:
                    # 昵称
                    nickname = item.find_element_by_id('com.tencent.mm:id/b9i').text
                    nickname = rex.sub('', nickname)
                    # 正文
                    content = item.find_element_by_id('com.tencent.mm:id/eua').text
                    content = rex.sub('', content)
                    print(nickname + "------->" + content)
                    isExist = self.itemExist(dataCollection, nickname, content)
                    if not isExist:
                        # 执行读取数据操作
                        contentGroup = item.find_element_by_id("com.tencent.mm:id/eow")
                        self.touch_tap(contentGroup.location.get('x') + 50, contentGroup.location.get('y') + 50)
                        sleep(2)
                        # 打开的是链接的
                        activityName = self.driver.current_activity
                        if "WebViewUI" in activityName:
                            self.driver.find_element_by_accessibility_id("返回").click()
                        # 打开的是图片的
                        if "SnsBrowseUI" in activityName:
                            imgArr = self.save_images()
                            # 保存数据
                            itemData = {'content': content, 'type': 1, 'photo': imgArr}
                            self.saveItemDataInCollection(dataCollection, nickname, itemData)
                        # 打开的是video的
                        if "SnsOnlineVideoActivity" in activityName:
                            fileInfo = self.save_videos()
                            itemData = {'content': content, 'type': 1, 'video': fileInfo}
                            self.saveItemDataInCollection(dataCollection, nickname, itemData)

                        print(dataCollection)
                except Exception as a:
                    self.verticalScrolling(0.6, 0.5)
                    print(a)

    # 保存视频操作
    def save_videos(self):
        # android.view.View
        currTime = 0
        videoGroup = self.driver.find_element_by_class_name("android.view.View")
        TouchAction(self.driver).long_press(videoGroup, 1000).wait(2000).perform()
        self.driver.find_element_by_xpath("//*[@text='保存视频']").click()
        currTime = time.time() * 1000
        sleep(1)
        # 点击退出界面
        videoGroup.click()
        return currTime

    def save_images(self):
        # com.tencent.mm: id / dgy
        imageArr = []
        try:
            imageViewArr = self.driver.find_elements_by_id("com.tencent.mm:id/dgy")
            for item in imageViewArr:
                fileInfo = self.longClickSave(item)
                imageArr.append(fileInfo)
        except Exception as e:
            imageView = self.driver.find_elements_by_class_name("android.widget.ImageView")
            fileInfo = self.longClickSave(imageView)
            imageArr.append(fileInfo)
            print(e)
        self.driver.find_element_by_class_name("android.widget.ImageView").click()
        sleep(3)
        return imageArr

    # 保存图片的方法
    def save_image(self):
        # android.widget.Gallery
        imageArr = []
        imageGroup = self.driver.find_element_by_class_name("android.widget.Gallery")
        imageViewArr = imageGroup.find_elements_by_class_name("android.widget.ImageView")
        if len(imageViewArr) == 1:
            fileInfo = self.longClickSave(imageViewArr[0])
            imageArr.append(fileInfo)
        else:
            for item in imageViewArr:
                fileInfo = self.longClickSave(item)
                imageArr.append(fileInfo)
        self.driver.find_element_by_class_name("android.widget.ImageView").click()
        sleep(3)
        return imageArr

    # 长按保存 + 滑动到下一张
    def longClickSave(self, element):
        currTime = 0
        TouchAction(self.driver).long_press(element, 1000).wait(2000).perform()
        self.driver.find_element_by_xpath("//*[@text='保存图片']").click()
        # 保存当前时间戳(毫秒级别)
        currTime = time.time() * 1000
        sleep(1)
        # 滑动下一张
        self.horizontalScrolling()
        return currTime

    # 坐标点击
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
    def verticalScrolling(self, start, end):
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        sleep(2)
        self.driver.swipe(screen_width / 2, screen_height * start, screen_width / 2, screen_height * end, 2000)

    # 查找数据集合中是否包含该条数据
    def itemExist(self, dataJson, nickname, content):
        if nickname in dataJson:
            dataArr = dataJson[nickname]
            if len(dataArr) > 0:
                for item in dataArr:
                    if item['content'] == content:
                        return True
                return False
            else:
                return False
        else:
            return False

    # 保存数据到集合
    def saveItemDataInCollection(self, dataJson, nikeName, data):
        if nikeName in dataJson:
            dataArr = dataJson[nikeName]
            dataArr.append(data)
        else:
            dataArr = [data]
            dataJson[nikeName] = dataArr

    # 获取设备保存朋友圈的文件
    def getWeChatFile(self):
        # 保存的图片文件夹 adb pull <手机目录> <电脑目录>
        os.system("adb pull /sdcard/tencent/MicroMsg/WeiXin/  e:/aa")


if __name__ == '__main__':
    weChat = WeChatTest()
    # weChat.getFriendMsg()
    # weChat.addFriends()
    weChat.crawl()
