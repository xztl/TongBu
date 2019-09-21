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
        print('��ʼ��½')
        loginBtn = self.driver.find_element_by_id("com.tencent.mm:id/edu")
        loginBtn.click()

        print('¼���˺�')
        phoneEdt = self.driver.find_element_by_id("com.tencent.mm:id/li")
        phoneEdt.send_keys("17308053023")

        print('�����һ��')
        loginNext = self.driver.find_element_by_id("com.tencent.mm:id/b0f")
        loginNext.click()
        sleep(4)

        print('��������')
        passwordEdt = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
        passwordEdt.send_keys("Aa123456")

        print('��¼---->')
        loginBtn = self.driver.find_element_by_id("com.tencent.mm:id/b0f")
        loginBtn.click()
        sleep(5)

    # ��Ӻ���
    def addFriends(self):
        sleep(30)
        print('���- + --->')
        add = self.driver.find_element_by_id("com.tencent.mm:id/qk")
        add.click()

        print('�����Ӻ���')
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

        # ��ȡ����
        localTxt = self.driver.find_element_by_id("	com.tencent.mm:id/b82").text
        self.location = localTxt

        goMarkPage = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout")
        goMarkPage.click()

        friendName = self.driver.find_element_by_id("com.tencent.mm:id/b8p")
        self.name = friendName
        print('friendName' + friendName)

        markPageBack = self.driver.find_element_by_accessibility_id("����")
        markPageBack.click()

        print("��Ӻ���")
        addFriends = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout")
        addFriends.click()

        addFriendsBack = self.driver.find_element_by_accessibility_id("����")
        addFriendsBack.click()

        searchPageBack = self.driver.find_element_by_accessibility_id("����")
        searchPageBack.click()

        goHome = self.driver.find_element_by_accessibility_id("����")
        goHome.click()

    # ��ȡָ�����ѵ�����
    def getFriendMsg(self):
        # ���ҵ�����
        huiHua = self.driver.find_elements_by_id('com.tencent.mm:id/b9i')
        for item in huiHua:
            if '��֮��' in item.text:
                # �ҵ���ϵ�˴�������
                item.click()
                sleep(5)
                # �ҵ���ϵ����Ϣ����
                openInfo = self.driver.find_element_by_accessibility_id("������Ϣ")
                openInfo.click()
                # ���ͷ��
                headImg = self.driver.find_element_by_xpath(
                    "//android.widget.FrameLayout[@content-desc=\"��ǰ����ҳ��,������Ϣ\"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
                headImg.click()
                # �������Ȧ���
                friendPhoto = self.driver.find_element_by_xpath("//*[@text='����Ȧ']")
                TouchAction(self.driver).tap(friendPhoto).perform()
                sleep(10)
                # ��ʼץȡ����Ȧ���� ����ID com.tencent.mm:id/or      item����� 	com.tencent.mm:id/ers
                diction = dict()
                currItem = dict()
                # ��ʼѭ�����б�
                while True:
                    flag = True
                    self.driver.swipe(500, 800, 500, 500, 2000)
                    sleep(5)
                    # �õ����еĵı��� bounds
                    infoList = self.driver.find_elements_by_id('com.tencent.mm:id/or')
                    for info in infoList:
                        print(info.text)

    # ��ȡ�����б�
    def getFriendListMsg(self):
        # �������Ȧ
        friendPage = self.driver.find_element_by_xpath("//*[@text='ͨѶ¼']")
        TouchAction(self.driver).tap(friendPage).perform()
        # �������ݼ���
        friendCollection = dict()
        # ��ȡ���е���ϵ���ǳ�

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
                print('�����б��ȡ���')
                flag = False
            except Exception:
                pass

            if flag is False:
                break
        #  ��ȡ�б�ɹ� ��ʼѭ���������
        print(friendCollection)

    # ֱ����ȡ����Ȧ��
    def crawl(self):
        sleep(2)
        # �������
        findPage = self.driver.find_element_by_xpath("//*[@text='����']")
        self.touch_tap(findPage.location.get('x'), findPage.location.get('y'))
        sleep(2)
        # �������Ȧ
        goFriendPage = self.driver.find_element_by_xpath("//*[@text='����Ȧ']")
        self.touch_tap(goFriendPage.location.get('x'), goFriendPage.location.get('y'))
        sleep(2)

        rex = re.compile('[^\u4e00-\u9fa5^a-z^A-Z^0-9]')
        # �ռ���Ϣ�ļ��� {userName : [{content:˵˵���� type:"1 ��Ƭ 2 ��Ƶ 3 ��ַ" ,photo:[ʱ���,ʱ���,ʱ���],video:ʱ���,webUrl:��ַ}]}
        dataCollection = dict()

        while True:
            flag = True
            self.verticalScrolling(0.6, 0.4)
            itemArr = self.driver.find_elements_by_id("com.tencent.mm:id/eu7")
            for item in itemArr:
                try:
                    # �ǳ�
                    nickname = item.find_element_by_id('com.tencent.mm:id/b9i').text
                    nickname = rex.sub('', nickname)
                    # ����
                    content = item.find_element_by_id('com.tencent.mm:id/eua').text
                    content = rex.sub('', content)
                    print(nickname + "------->" + content)
                    isExist = self.itemExist(dataCollection, nickname, content)
                    if not isExist:
                        # ִ�ж�ȡ���ݲ���
                        contentGroup = item.find_element_by_id("com.tencent.mm:id/eow")
                        self.touch_tap(contentGroup.location.get('x') + 50, contentGroup.location.get('y') + 50)
                        sleep(2)
                        # �򿪵������ӵ�
                        activityName = self.driver.current_activity
                        if "WebViewUI" in activityName:
                            self.driver.find_element_by_accessibility_id("����").click()
                        # �򿪵���ͼƬ��
                        if "SnsBrowseUI" in activityName:
                            imgArr = self.save_images()
                            # ��������
                            itemData = {'content': content, 'type': 1, 'photo': imgArr}
                            self.saveItemDataInCollection(dataCollection, nickname, itemData)
                        # �򿪵���video��
                        if "SnsOnlineVideoActivity" in activityName:
                            fileInfo = self.save_videos()
                            itemData = {'content': content, 'type': 1, 'video': fileInfo}
                            self.saveItemDataInCollection(dataCollection, nickname, itemData)

                        print(dataCollection)
                except Exception as a:
                    self.verticalScrolling(0.6, 0.5)
                    print(a)

    # ������Ƶ����
    def save_videos(self):
        # android.view.View
        currTime = 0
        videoGroup = self.driver.find_element_by_class_name("android.view.View")
        TouchAction(self.driver).long_press(videoGroup, 1000).wait(2000).perform()
        self.driver.find_element_by_xpath("//*[@text='������Ƶ']").click()
        currTime = time.time() * 1000
        sleep(1)
        # ����˳�����
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

    # ����ͼƬ�ķ���
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

    # �������� + ��������һ��
    def longClickSave(self, element):
        currTime = 0
        TouchAction(self.driver).long_press(element, 1000).wait(2000).perform()
        self.driver.find_element_by_xpath("//*[@text='����ͼƬ']").click()
        # ���浱ǰʱ���(���뼶��)
        currTime = time.time() * 1000
        sleep(1)
        # ������һ��
        self.horizontalScrolling()
        return currTime

    # ������
    def touch_tap(self, x, y, duration=100):  # �������  ,x1,x2,y1,y2,duration
        '''
        method explain:�������
        parameter explain����x,y������ֵ,��duration��:����ֵ�����˵�����ٶ�
        Usage:
            device.touch_coordinate(277,431)      #277.431Ϊ���ĳ��Ԫ�ص�x��yֵ
        '''
        screen_width = self.driver.get_window_size()['width']  # ��ȡ��ǰ��Ļ�Ŀ�
        screen_height = self.driver.get_window_size()['height']  # ��ȡ��ǰ��Ļ�ĸ�
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        self.driver.tap([(x1, y1), (x1, y1)], duration)

    # �����������
    def horizontalScrolling(self):
        screen_width = self.driver.get_window_size()['width']  # ��ȡ��ǰ��Ļ�Ŀ�
        screen_height = self.driver.get_window_size()['height']  # ��ȡ��ǰ��Ļ�ĸ�
        self.driver.swipe(screen_width * 0.8, screen_height / 2, screen_width * 0.1, screen_height / 2, 2000)

    # �����������
    def verticalScrolling(self, start, end):
        screen_width = self.driver.get_window_size()['width']  # ��ȡ��ǰ��Ļ�Ŀ�
        screen_height = self.driver.get_window_size()['height']  # ��ȡ��ǰ��Ļ�ĸ�
        sleep(2)
        self.driver.swipe(screen_width / 2, screen_height * start, screen_width / 2, screen_height * end, 2000)

    # �������ݼ������Ƿ������������
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

    # �������ݵ�����
    def saveItemDataInCollection(self, dataJson, nikeName, data):
        if nikeName in dataJson:
            dataArr = dataJson[nikeName]
            dataArr.append(data)
        else:
            dataArr = [data]
            dataJson[nikeName] = dataArr

    # ��ȡ�豸��������Ȧ���ļ�
    def getWeChatFile(self):
        # �����ͼƬ�ļ��� adb pull <�ֻ�Ŀ¼> <����Ŀ¼>
        os.system("adb pull /sdcard/tencent/MicroMsg/WeiXin/  e:/aa")


if __name__ == '__main__':
    weChat = WeChatTest()
    # weChat.getFriendMsg()
    # weChat.addFriends()
    weChat.crawl()
