from appium import webdriver
from time import sleep
#from  selenium import webdriver
from jxc_lightApp import publicFunction,baoCunChengGongPage
from jxc_lightApp.findElement import FindElement

def get_driver():
    desired_caps = {
                          "platformName": "Android",
                          "platformVersion": "9",
                          "deviceName": "SM-G9350",  #SJE5T17A19007623 SM-G9350
                          "appPackage": "com.kingdee.jdy",
                          "appActivity": "com.kdweibo.android.ui.activity.StartActivity",#"com.kingdee.eas.eclite.ui.login.LoginActivity", #adb shell dumpsys window windows | findstr “Current”
                          "udid": "127.0.0.1:21503",
                           "app":"C:\\Users\\Administrator\\Desktop\\jdy_release_android_360_v6.5.2.apk",
                           'noReset': 'true',
                          "unicodeKeyboard": 'true',
                          "resetKeyboard": 'true',
                          "noSign": 'true',
                          "recreateChromeDriverSessions": 'true',
                          "automationName": "UiAutomator1"
                        }
    globals()
    driver = webdriver.Remote('http://localhost:4700/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver

def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height

#向左滑动
def swipe_left():
    size =get_size()
    x1 = get_size()[0]/10*9
    y1 = get_size()[1]/2
    x = get_size()[0]/10
    driver.swipe(x1,y1,x,y1)

def swipe_right():
    size =get_size()
    x1 = get_size()[0]/10
    y1 = get_size()[1]/2
    x = get_size()[0]/10*9
    driver.swipe(x1,y1,x,y1)

def swipe_on(direction):
    if direction == 'left':
        swipe_left()
    elif direction == 'right':
        swipe_right()

driver = get_driver()
swipe_on('left')
swipe_on('left')
swipe_on('left')
swipe_on('right')


def login():
    #登录
    get_by_local = FindElement(driver)

    get_by_local.get_element('login_button_one').click()
    get_by_local.get_element('username').send_keys("kingdeetestv3")
    get_by_local.get_element('password').send_keys("a1234567")
    get_by_local.get_element('login_button').click()


    # driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/"
    #                      "android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText").send_keys("kingdeetestv3")
    #
    # driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout"
    #                      "/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.EditText").send_keys("a1234567")

#driver.find_element_by_id("com.kingdee.jdy:id/login").click()
login()






#开单
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                         "/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.View[1]/android.widget.ListView/android.widget.RelativeLayout"
                         "/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]").click()

driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                         "/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.TextView").click()




driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                         "/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.TextView[2]").click()

driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView"
                         "/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout"
                         "/android.widget.RelativeLayout/android.widget.TextView[2]").click()

driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                         "/android.widget.LinearLayout[2]/android.widget.FrameLayout[2]/android.widget.TextView").click()
#选择仓库
driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView"
                         "/android.widget.FrameLayout[1]/android.widget.TextView").click()


driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]"
                             "/android.support.v7.widget.RecyclerView[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()


driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                             "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView").click()


driver.find_element_by_id("com.kingdee.jdy:id/tv_choose_confirm").click()
#保存

driver.find_element_by_id("com.kingdee.jdy:id/tv_commit").click()

t=baoCunChengGongPage.sale_finish(driver)

publicFunction.objDisplay(driver,t)





