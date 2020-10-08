#coding=utf-8
import time
from appium import webdriver
from v7jxc_auto.util.write_user_command import WriteUserCommand
from v7jxc_auto.util.findElement import FindElement


class BaseDriver():
    def android_driver(self,i):

        print ("this is android_driver:",i)

        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_'+str(i),'deviceName')
        port = write_file.get_value('user_info_'+str(i),'port')


        print(devices)
        print(port)

        capabilities = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": devices,  #SJE5T17A19007623 SM-G9350
            "appPackage": "com.kingdee.jdy",
            "appActivity": "com.kdweibo.android.ui.activity.StartActivity",#"com.kingdee.eas.eclite.ui.login.LoginActivity", #adb shell dumpsys window windows | findstr “Current”
            "udid": devices,#NAB0220629016963  127.0.0.1:21503
            "app":"D:\\v7app_auto\\untitled1\\v7jxc_auto\\data\\jdy_release_android_jdy_v7.0.3.apk",
            'noReset': 'false',
            "unicodeKeyboard": 'true',
            "resetKeyboard": 'true',
            "noSign": 'true',
            "recreateChromeDriverSessions": 'true',
            "automationName": "UiAutomator1",
            "chromedriverExecutable":"D:\\v7app_auto\\untitled1\\v7jxc_auto\\data\\chromedriver.exe"

        }
        time.sleep(10)

        globals()
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub",capabilities)
        driver.implicitly_wait(5)

        # get_by_local = FindElement(driver)
        #
        # try:
        #     get_by_local.get_element("agree").click()
        # except:
        #     print("没有点击agree")
        # try:
        #     get_by_local.get_element("Get_permission").click()
        #     get_by_local.get_element("Get_permission").click()
        # except:
        #     print("有没点击权限")
        #
        # size = driver.get_window_size()
        # width = size['width']
        # height = size['height']
        #
        #
        #
        # # 向左滑动
        # print("向左滑动")
        # x1 = width / 10 * 9
        # y1 = height / 2
        # x = width / 10
        # driver.swipe(x1, y1, x, y1)
        # driver.swipe(x1, y1, x, y1)
        #
        # #向右滑动
        # print('向右滑动')
        # x1 = width / 10
        # y1 = height / 2
        # x = width / 10 * 9
        # driver.swipe(x1, y1, x, y1)

        return driver
