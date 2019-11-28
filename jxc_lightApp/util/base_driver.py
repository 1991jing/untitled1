import time
from appium import webdriver

#from  selenium import webdriver


class BaseDriver(object):



    def basedriver(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "SM-G9350",  # SJE5T17A19007623 SM-G9350
            "appPackage": "com.kingdee.jdy",
            "appActivity": "com.kdweibo.android.ui.activity.StartActivity",
            # "com.kingdee.eas.eclite.ui.login.LoginActivity", #adb shell dumpsys window windows | findstr “Current”
            "udid": "127.0.0.1:21503",
            "app": "C:\\Users\\Administrator\\Desktop\\jdy_release_android_360_v6.5.2.apk",
            'noReset': 'false',
            "unicodeKeyboard": 'true',
            "resetKeyboard": 'true',
            "noSign": 'true',
            "recreateChromeDriverSessions": 'true',
            "automationName": "UiAutomator1"
        }
        globals()
        driver = webdriver.Remote('http://localhost:4700/wd/hub', desired_caps)
        driver.implicitly_wait(5)

        size = driver.get_window_size()
        width = size['width']
        height = size['height']

    # 向左滑动
        print("向左滑动")
        x1 = width / 10 * 9
        y1 = height / 2
        x = width / 10
        driver.swipe(x1, y1, x, y1)
        driver.swipe(x1, y1, x, y1)


    #向右滑动
        print('向右滑动')
        x1 = width / 10
        y1 = height / 2
        x = width / 10 * 9
        driver.swipe(x1, y1, x, y1)


        return driver



if __name__ == '__main__':
    dr = BaseDriver()
    dr.basedriver()
