import sys

from appium import webdriver
import time
from v7jxc_auto.util.dos_cmd import DosCmd
from selenium.webdriver.common.action_chains import ActionChains
from v7jxc_auto.util.findElement import FindElement
from selenium.webdriver.common.keys import Keys
# dos = DosCmd()
#
# dos.excute_cmd('start appium -p 4700 -bp 4701 -U 127.0.0.1:21503')



def get_driver():
    desired_caps = {
                          "platformName": "Android",
                          "platformVersion": "9",
                          "deviceName": "SM-G9350",  #SJE5T17A19007623 SM-G9350
                          "appPackage": "com.kingdee.jdy",
                          "appActivity": "com.kdweibo.android.ui.activity.StartActivity",#"com.kingdee.eas.eclite.ui.login.LoginActivity", #adb shell dumpsys window windows | findstr “Current”
                          "udid": "NAB0220629016963",#NAB0220629016963  127.0.0.1:21503
                           "app":"D:\\v7app_auto\\untitled1\\v7jxc_auto\\data\\jdy_release_android_jdy_v7.0.3.apk",
                           'noReset': 'false',
                          "unicodeKeyboard": 'true',
                          "resetKeyboard": 'true',
                          "noSign": 'true',
                          "recreateChromeDriverSessions": 'true',
                          "automationName": "UiAutomator1",
                          "chromedriverExecutable":"C:/Users/kingdee/AppData/Local/Google/Chrome/Application/chromedriver.exe"

                        }
    globals()
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
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

# 启动参数需增加 desired_caps["chromedriverExecutable"] = 'D:\\code\\softspace\\66-68\\chromedriver.exe'



def switch_to_context():
    time.sleep(2)  # 因为无法监控，加上web页面加载比较慢所以等待时间比较长
    # 获取页面所有的上下文
    cons = driver.contexts  #['NATIVE_APP', 'WEBVIEW_unknown', 'WEBVIEW_stetho_com.kingdee.jdy']
    print(cons)
    # 获取当前窗口的上下文
    print(driver.current_context)
    #driver.switch_to.context("NATIVE_APP")
    driver.switch_to.context(cons[2])
    print(driver.current_context)






driver = get_driver()
get_by_local = FindElement(driver)

get_by_local.get_element("agree").click()
get_by_local.get_element("Get_permission").click()
get_by_local.get_element("Get_permission").click()

swipe_on('left')
swipe_on('left')
swipe_on('left')
swipe_on('right')


# def login():
    #登录


get_by_local.get_element('login_button_one').click()
get_by_local.get_element('username').send_keys("kingdeetest5854")
get_by_local.get_element('password').send_keys("a1234567")
get_by_local.get_element('login_button').click()

#5854选择账套
zt=driver.find_elements_by_id("com.kingdee.jdy:id/iv_fdb_status")
zt[6].click()
driver.find_element_by_id("com.kingdee.jdy:id/tv_fdb_enter").click()

# 应用
t=driver.find_elements_by_id("com.kingdee.jdy:id/footer_menu_item_icon")
t[1].click()
time.sleep(3)

#选择做采购出库单
e=driver.find_elements_by_id("com.kingdee.jdy:id/ic_app_name")
print(e)
for ii in e:
    print(ii.text)
e[10].click()
# login()

#做采购单

switch_to_context()


get_by_local.get_element('add',meg="caigou_element").click()
switch_to_context()
print(driver.current_context)
# print (driver.page_source)

get_by_local.get_element('add_supplier',meg="caigou_element").send_keys(u"河源供应商")
#select_supplier
switch_to_context()

get_by_local.get_element('select_supplier',meg="caigou_element").click()

switch_to_context()

get_by_local.get_element('add_goods',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('h1_warehouse',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('search_warehouse_baihuo',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('search_box',meg="caigou_element").send_keys(u"益达").send_keys(Keys.ENTER)
switch_to_context()
get_by_local.get_element('select_goods',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('goods_quantity',meg="caigou_element").clear().send_keys(10)

get_by_local.get_element('confirm',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('confirm_select',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('Settlement',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('pay',meg="caigou_element").click()
get_by_local.get_element('account',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('select_account',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('pay_for',meg="caigou_element").send_keys(50)


switch_to_context()
get_by_local.get_element('show_more',meg="caigou_element").click()
time.sleep(3)
print (driver.page_source)
print(driver.contexts)

# get_by_local.get_element('remake',meg="caigou_element").send_keys("test an order...")


print(driver.contexts)
# ActionChains(driver).send_keys(u"test an order.").perform()
# get_by_local.get_element('remake',meg="caigou_element").send_keys(u"test an order.")
#driver.switch_to.active_element.send_keys(u"test an order.")

get_by_local.get_element('Place_order',meg="caigou_element").click()
driver.get_screenshot_as_file('./data/test.png')
switch_to_context()
get_by_local.get_element('purinbound_list',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('select_date',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('date_today',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('purinbound_staus',meg="caigou_element").click()
switch_to_context()
get_by_local.get_element('unaudited',meg="caigou_element").click()
switch_to_context()
#打印订单编号
print(get_by_local.get_element('billno',meg="caigou_element").text)

get_by_local.get_element('billno',meg="caigou_element").click()
switch_to_context()
#审核单据
get_by_local.get_element('audit_button',meg="caigou_element").click()

driver.get_screenshot_as_file('./data/test2.png')

