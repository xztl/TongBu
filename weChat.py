# coding=gbk

from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import os

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

        dataCollection = dict()

        while True:
            flag = True
            self.driver.swipe(500, 1000, 500, 500, 2000)
            itemArr = self.driver.find_elements_by_id("com.tencent.mm:id/eu7")
            for item in itemArr:
                nickname = item.find_element_by_id('com.tencent.mm:id/b9i').text
                # ����
                content = item.find_element_by_id('com.tencent.mm:id/eua').text
                # ���Ҹ�����¼�Ƿ����
                # findItemExist(dataCollection, nickname, content)
                # ͼƬ  ��Ƶ�� content-desc = ͼƬ
                try:
                    item.find_element_by_id("com.tencent.mm:id/eow").click()
                    sleep(2)
                    activityName = self.driver.current_activity
                    # .plugin.sns.ui.SnsBrowseUI'(ͼƬ)
                    # .plugin.webview.ui.tools.WebViewUI�����ӣ�
                    # '.plugin.sns.ui.SnsOnlineVideoActivity����Ƶ��' �򿪵�������
                    if "WebViewUI" in activityName:
                        self.driver.find_element_by_accessibility_id("����").click()
                    # �򿪵���ͼƬ��
                    if "SnsBrowseUI" in activityName:
                        self.save_img()
                    if "SnsOnlineVideoActivity" in activityName:
                        self

                    flag = False
                except Exception:
                    print(nickname + "û��ͼƬ����Ƶ")
                    pass

    # ��ȡ�豸��������Ȧ���ļ�
    def getWeChatFile(self):
        # �����ͼƬ�ļ��� adb pull <�ֻ�Ŀ¼> <����Ŀ¼>
        os.system("adb pull /sdcard/tencent/MicroMsg/WeiXin/  e:/aa")

    def save_img(self):
        # com.tencent.mm:id/dgy СԲ��
        try:
            iconArr = self.driver.find_elements_by_id("com.tencent.mm:id/dgy")
            for item in iconArr:
                # ����
                imageView = self.driver.find_element_by_class_name("android.widget.ImageView")
                TouchAction(self.driver).long_press(imageView, imageView.location.get('x'), imageView.location.get('y'), 1000)
                self.driver.find_element_by_xpath("//*[@text='����ͼƬ']")
                # ���浱ǰʱ���
                sleep(1)
                # ������һ��
                self.horizontalScrolling()
        except Exception:
            imageView = self.driver.find_element_by_class_name("android.widget.ImageView")
            TouchAction(self.driver).long_press(imageView, imageView.location.get('x'), imageView.location.get('y'),
                                                1000)


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
        self.driver.swipe(500 * 0.3, screen_height / 2, 500 * 0.6, screen_height / 2, 2000)


if __name__ == '__main__':
    weChat = WeChatTest()
    # weChat.getFriendMsg()
    # weChat.addFriends()
    weChat.crawl()
