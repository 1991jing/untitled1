# -*- coding:utf-8 -*-

# from selenium import webdriver
#
# driver = webdriver.Chrome("C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")  # 打开
# driver.maximize_window()  # 最大化窗口
# driver.get("http://www.baidu.com")
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.common.keys import Keys
import time,datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
print("---测试开始---")
mobileEmulation = {'deviceName': 'Galaxy S5'} # iPhone X
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(executable_path="D:/v7app_auto/untitled1/v7jxc_auto/data/chromedriver.exe",chrome_options=options)
driver.get('https://m.jdy.com/')
time.sleep(5)
print(0)
#driver.find_element_by_xpath("//*[@id='user']").click()#//*[@id="user"]/a
#driver.find_element_by_xpath("//*[@id='user']/a").send_keys(Keys.ENTER)
element=WebDriverWait(driver,20,0.5).until(driver.find_element_by_xpath("//*[@id='user']"))
element.click()


# driver.find_element_by_id("user").click()
# js0 = 'document.getElementById("user").click();'
# driver.execute_script(js0)
print(1)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='login_username']").send_keys('kingdeetestv3')
driver.find_element_by_xpath("//*[@id='login_pwd']").send_keys('a1234567')
time.sleep(2)


#登录
WebDriverWait(driver,20,0.5).until( driver.find_element_by_id('login_btn'))
driver.find_element_by_xpath("//*[@id='login_btn']").click()

time.sleep(2)
element=WebDriverWait(driver,20,0.5).until(driver.find_element_by_xpath("//*[@id='user']"))
element.click()

time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[1]/div/div/div[5]/ul/li[2]/a').click() # /html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/ul/li[3]/a

# tt=driver.find_element_by_xpath('//*[@id="serviceList"]/table/tbody[2]/tr[4]/td[4]/a')
# print(tt)
time.sleep(2)
#新增商品
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]").click()
#+号
time.sleep(2)
#driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[3]").click()
js = 'document.getElementsByClassName("add icon icon-plus")[0].click();'
driver.execute_script(js)
#goods="test_goods_"+time.strftime('%Y-%m-%d-%H:%M:%S')
goods="test_goods_"+str(random.randrange(0,10000))
print(goods)
time.sleep(5)
driver.find_elements_by_css_selector("[placeholder='请输入']")[2].send_keys(goods)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/a").click()
#搜索新增商品
time.sleep(5)
#t=driver.find_element_by_css_selector("input.ui-cell-input")
#print(t)
#ActionChains(driver).move_to_element(driver.find_element_by_css_selector("input.ui-cell-input")).send_keys(goods).perform()
#tt=driver.find_element_by_tag_name("input data-v-6f0c43f1")
#tt=driver.find_element_by_css_selector("div.slot-content showSearchIcon>input").send_keys(goods)

js2 = 'document.getElementsByClassName("ui-cell-input")[0].value="%s";' %goods
 #     'document.getElementsByClassName("add icon icon-plus")[0].click();'
driver.execute_script(js2)
js4 = 'document.getElementsByClassName("ui-cell-input")[0].click();'
driver.execute_script(js4)
print(3)
# ActionChains(driver).move_to_element(driver.find_element_by_css_selector(".icon icon-search-gray")).click().perform()
# tt.send_keys(goods)
js3 = 'document.querySelectorAll("span")[1].style.display="block";'
driver.execute_script(js3)
time.sleep(5)
js32 = 'document.getElementsByClassName("icon icon-search-gray")[0].click();'
# print("--")
driver.execute_script(js32)
print(22)
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/header/div/div[2]/div/span").click()

print("---测试ok---")
print("---测试结束---")

#input_16bd046f571  /html/body/div/div[2]/div[1]/div/div[1]/div[1]/div[3]
#新增客户
# driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[1]/span[2]/div/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div/div[2]/div[2]").click()
# driver.find_element_by_xpath('//*[@id="input_1548310724303"]').send_keys('ABC')
# driver.find_element_by_xpath('//*[@id="input_1548310724309"]').click()
# driver.find_element_by_xpath('//*[@id="vux-scroller-rnzee"]/div[1]/div[1]/div/div[3]').click()
# driver.find_element_by_xpath('//*[@id="input_1548310884011"]').send_keys("this is a test.")
# driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/a/text()').click()
driver.close()

