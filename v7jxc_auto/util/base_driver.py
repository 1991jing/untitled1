import time
from appium import webdriver

#from  selenium import webdriver


class BaseDriver(object):

    def basedriver(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "SM-G9350",  #SJE5T17A19007623 SM-G9350
            "appPackage": "com.kingdee.jdy",
            "appActivity": "com.kdweibo.android.ui.activity.StartActivity",#"com.kingdee.eas.eclite.ui.login.LoginActivity", #adb shell dumpsys window windows | findstr “Current”
            "udid": "127.0.0.1:21503",#NAB0220629016963  127.0.0.1:21503
            "app":"D:\\v7app_auto\\untitled1\\v7jxc_auto\\data\\jdy_release_android_jdy_v7.0.3.apk",
            'noReset': 'false',
            "unicodeKeyboard": 'true',
            "resetKeyboard": 'true',
            "noSign": 'true',
            "recreateChromeDriverSessions": 'true',
            "automationName": "UiAutomator1",
            "chromedriverExecutable":"C:\\Users\\kingdee\\Desktop\\chromedriver.exe"

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

    def switch_to_context(self,driver):
        time.sleep(2)  # 因为无法监控，加上web页面加载比较慢所以等待时间比较长
        # 获取页面所有的上下文
        cons = driver.contexts  #['NATIVE_APP', 'WEBVIEW_com.kingdee.jdy', 'WEBVIEW_com.android.launcher2']
        print(cons)
        # 获取当前窗口的上下文
        print(driver.current_context)
        #driver.switch_to.context("NATIVE_APP")
        driver.switch_to.context(cons[2])
        print(driver.current_context)

if __name__ == '__main__':
    dr = BaseDriver()
    dr.basedriver()



