from v7jxc_auto.handdle.caigou_handle import CaigouHandle

from v7jxc_auto.handdle.oper_handle import LoginHandle
import time

from v7jxc_auto.handdle.oper_handle import LoginPage
from v7jxc_auto.base.base_driver import BaseDriver
from v7jxc_auto.util.findElement import FindElement
import time
from selenium.webdriver.common.keys import Keys


class XiaoshouBusiness(object):

    def __init__(self,i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local= FindElement(self.driver)
        self.gz=self.get_size()

    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

        #向左滑动
    def swipe_left(self):
        size = self.gz
        x1 = self.get_size()[0]/10*9
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10
        self.driver.swipe(x1,y1,x,y1)

    def swipe_right(self):
        size =self.gz
        x1 = self.get_size()[0]/10
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10*9
        self.driver.swipe(x1,y1,x,y1)

        # def swipe_on(self,direction):
        #     if direction == 'left':
        #         swipe_left()
        #     elif direction == 'right':
        #         swipe_right()

        # 启动参数需增加 desired_caps["chromedriverExecutable"] = 'D:\\code\\softspace\\66-68\\chromedriver.exe'

    def switch_to_context(self):
        time.sleep(2)  # 因为无法监控，加上web页面加载比较慢所以等待时间比较长
        # 获取页面所有的上下文
        cons = self.driver.contexts  #['NATIVE_APP', 'WEBVIEW_com.kingdee.jdy', 'WEBVIEW_com.android.launcher2']
        print(cons)
        # 获取当前窗口的上下文
        print(self.driver.current_context)
        #driver.switch_to.context("NATIVE_APP")
        self.driver.switch_to.context(cons[2])
        print(self.driver.current_context)


    def get_purchase_order(self):

        self.get_by_local.get_element("agree").click()
        try:
            self.get_by_local.get_element("Get_permission").click()
            self.get_by_local.get_element("Get_permission").click()
        except:
            print("跳过获取权限")

        #滑动
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        self.swipe_right()

        #登录
        self.get_by_local.get_element('login_button_one').click()
        self.get_by_local.get_element('username').send_keys("kingdeetest5854")
        self.get_by_local.get_element('password').send_keys("a1234567")
        self.get_by_local.get_element('login_button').click()

        #5854选择账套
        zhangtao=self.driver.find_elements_by_id("com.kingdee.jdy:id/tv_fdb_company_name")
        for zt in zhangtao:
            print(zt.text)
            if zt.text=="AUTO_TEST":
                zt.click()
            else:
                print("不是AUTO_TEST这个账套")



        self.driver.find_element_by_id("com.kingdee.jdy:id/tv_fdb_enter").click()

        # 应用
        t=self.driver.find_elements_by_id("com.kingdee.jdy:id/footer_menu_item_icon")
        t[1].click()
        time.sleep(3)

        #选择做采购出库单
        e=self.driver.find_elements_by_id("com.kingdee.jdy:id/ic_app_name")
        print(e)
        for ii in e:
            print(ii.text)
        e[10].click()
        # login()
        time.sleep(5)
        #做采购单

        self.switch_to_context()


        self.get_by_local.get_element('add',meg="caigou_element").click()
        self.switch_to_context()
        # print (driver.page_source)

        self.get_by_local.get_element('add_supplier',meg="caigou_element").send_keys(u"河源供应商")
        #select_supplier
        self.switch_to_context()

        self.get_by_local.get_element('select_supplier',meg="caigou_element").click()

        self.switch_to_context()

        self.get_by_local.get_element('add_goods',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('h1_warehouse',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('search_warehouse_baihuo',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('search_box',meg="caigou_element").send_keys(u"益达").send_keys(Keys.ENTER)
        self.switch_to_context()
        self.get_by_local.get_element('select_goods',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('goods_quantity',meg="caigou_element").clear().send_keys(10)

        self.get_by_local.get_element('confirm',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('confirm_select',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('Settlement',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('pay',meg="caigou_element").click()
        self.get_by_local.get_element('account',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('select_account',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('pay_for',meg="caigou_element").send_keys(50)


        self.switch_to_context()
        self.get_by_local.get_element('show_more',meg="caigou_element").click()
        time.sleep(3)


        # get_by_local.get_element('remake',meg="caigou_element").send_keys("test an order...")



        # ActionChains(driver).send_keys(u"test an order.").perform()
        # get_by_local.get_element('remake',meg="caigou_element").send_keys(u"test an order.")
        #driver.switch_to.active_element.send_keys(u"test an order.")

        self.get_by_local.get_element('Place_order',meg="caigou_element").click()
        print(self.driver.contexts)
        # driver.get_screenshot_as_file('./data/test_mn.png')


        time.sleep(2)
        self.switch_to_context()
        self.get_by_local.get_element('purinbound_list',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('select_date',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('date_today',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('purinbound_staus',meg="caigou_element").click()
        self.switch_to_context()
        self.get_by_local.get_element('unaudited',meg="caigou_element").click()
        self.switch_to_context()
        #打印订单编号
        print(self.get_by_local.get_element('billno',meg="caigou_element").text)

        self.get_by_local.get_element('billno',meg="caigou_element").click()
        self.switch_to_context()
        #审核单据
        self.get_by_local.get_element('audit_button',meg="caigou_element").click()




