from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.common.keys import Keys
import time, datetime
from selenium import webdriver

print("---测试开始---")

mobileEmulation = {'deviceName': 'Galaxy S5'}  # iPhone X
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(
    executable_path="C:/Users/kingdee/AppData/Local/Google/Chrome/Application/chromedriver.exe",
    chrome_options=options)
driver.get('https://m.jdy.com/')
time.sleep(5)
#这一步偶尔失焦点击不到
driver.find_element_by_xpath("/html/body/div[1]/div").click()
driver.find_element_by_id("user").click()

time.sleep(2)
driver.find_element_by_xpath("//*[@id='login_username']").send_keys('kingdeetestv3')
driver.find_element_by_xpath("//*[@id='login_pwd']").send_keys('a1234567')
time.sleep(2)
# 登录
driver.find_element_by_xpath("//*[@id='login_btn']").click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[1]/div/div/div[5]/ul/li[2]/a').click()

time.sleep(2)
# 新增商品
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]").click()
# +号
time.sleep(2)

js = 'document.getElementsByClassName("add icon icon-plus")[0].click();'
driver.execute_script(js)
goods = "test_goods_" + str(random.randrange(0, 10000))
print(goods)
time.sleep(5)
driver.find_elements_by_css_selector("[placeholder='请输入']")[2].send_keys(goods)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/a").click()
# 搜索新增商品
time.sleep(5)

js2 = 'document.getElementsByClassName("ui-cell-input")[0].value="%s";' % goods

driver.execute_script(js2)
js4 = 'document.getElementsByClassName("ui-cell-input")[0].click();'
driver.execute_script(js4)
print(3)

js3 = 'document.querySelectorAll("span")[1].style.display="block";'
driver.execute_script(js3)
time.sleep(5)
js32 = 'document.getElementsByClassName("icon icon-search-gray")[0].click();'

driver.execute_script(js32)
print(22)
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/header/div/div[2]/div/span").click()

print("---测试结束---")

