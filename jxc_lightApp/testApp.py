import sys

from appium import webdriver

from jxc_lightApp.util.dos_cmd import DosCmd
# from  selenium import webdriver
from jxc_lightApp.util.findElement import FindElement

dos = DosCmd()

dos.excute_cmd('start appium -p 4700 -bp 4701 -U 127.0.0.1:21503')



def get_driver():
    desired_caps = {
                          "platformName": "Android",
                          "platformVersion": "9",
                          "deviceName": "SM-G9350",  #SJE5T17A19007623 SM-G9350
                          "appPackage": "com.kingdee.jdy",
                          "appActivity": "com.kdweibo.android.ui.activity.StartActivity",#"com.kingdee.eas.eclite.ui.login.LoginActivity", #adb shell dumpsys window windows | findstr “Current”
                          "udid": "127.0.0.1:21503",
                           "app":"C:\\Users\\Administrator\\Desktop\\jdy_release_android_360_v6.5.2.apk",
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


# def login():
    #登录
get_by_local = FindElement(driver)

get_by_local.get_element('login_button_one').click()
get_by_local.get_element('username').send_keys("kingdeetestv3")
get_by_local.get_element('password').send_keys("a1234567")
get_by_local.get_element('login_button').click()

get_by_local.get_element('menu_yingyong_button').click()



# login()
try:
#做采购单
    get_by_local.get_element_cg('caigou').click()
    get_by_local.get_element_cg('xzgongyingshang_button').click()
    get_by_local.get_element_cg('xzgongyingshang').click()
    get_by_local.get_element_cg('xzshangping_button').click()
    get_by_local.get_element_cg('xzcangku').click()
    get_by_local.get_element_cg('1haocang').click()
    get_by_local.get_element_cg('xzshangp1').click()
    get_by_local.get_element_cg('jia1').click()
    get_by_local.get_element_cg('jiarugouwuche_button').click()
    get_by_local.get_element_cg('xzshangp2').click()
    get_by_local.get_element_cg('jia2').click()
    get_by_local.get_element_cg('jiarugouwuche_button').click()
    get_by_local.get_element_cg('xuanzehaole_button').click()
    get_by_local.get_element_cg('bill_remake').send_keys('This is a test.')
    get_by_local.get_element_cg('commit_button').click()
    get_by_local.get_element_cg('caigoulishi_button').text



except:
    driver.get_screenshot_as_file('./data/test.png')

get_by_local.get_element_cg('back').click()



get_by_local.get_element('menu_shouye_button').click()

# try:
#销售开单
get_by_local.get_element_xs('xiaoshou').click()
get_by_local.get_element_xs('xzkehu').click()
get_by_local.get_element_xs('kehu1').click()
get_by_local.get_element_xs('xzshangping_button').click()
get_by_local.get_element_xs('xzcangku').click()
get_by_local.get_element_xs('xzshangp1').click()
get_by_local.get_element_xs('jiarugouwuche_button').click()
get_by_local.get_element_xs('xuanzehaole_button').click()
get_by_local.get_element_xs('commit_button').click()
get_by_local.get_element_xs('back').click()
if sys.exc_info()[0]:
    driver.get_screenshot_as_file('./data/test3.png')
# except:
#     driver.get_screenshot_as_file('./data/test2.png')


#销售
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout"
#                          "/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.View[1]/android.widget.ListView/android.widget.RelativeLayout"
#                          "/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]").click()
#
#
#
#
#选择客户
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
#                          "/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.TextView").click()
#
#
#客户1
# driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
#                          "/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.TextView[2]").click()
#新增商品
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView"
#                          "/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout"
#                          "/android.widget.RelativeLayout/android.widget.TextView[2]").click()
#选择仓库
# driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout"
#                          "/android.widget.LinearLayout[2]/android.widget.FrameLayout[2]/android.widget.TextView").click()
# #仓库
# driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView"
#                          "/android.widget.FrameLayout[1]/android.widget.TextView").click()
#
#选择商品
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]"
#                              "/android.support.v7.widget.RecyclerView[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
#
#确定
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
#                              "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView").click()
#
#加入购物车
# driver.find_element_by_id("com.kingdee.jdy:id/tv_choose_confirm").click()
# #保存
#
# driver.find_element_by_id("com.kingdee.jdy:id/tv_commit").click()

# t=baoCunChengGongPage.sale_finish(driver)
#
# publicFunction.objDisplay(driver)





