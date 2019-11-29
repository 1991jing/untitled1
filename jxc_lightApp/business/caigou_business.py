from jxc_lightApp.handdle.caigou_handle import CaigouHandle

from jxc_lightApp.handdle.oper_handle import LoginHandle
import time

from jxc_lightApp.handdle.oper_handle import LoginPage


class CaigouBusiness(object):
    def __init__(self):
        #self.caigou_handle = CaigouHandle()

        # self.login_page =  LoginPage()
        #
        # self.login_page.get_loginone_button_element().click()
        # self.login_page.get_username_element().send_keys('kingdeetestv3')
        # self.login_page.get_password_element().send_keys('a1234567')
        # self.login_page.get_login_button_element().click()
        #
        # self.login_page.get_menu_yingyong_button_element().click()

        #采购前操作
        self.caigou_handle = LoginHandle()

        self.caigou_handle.click_loginone_button()

        self.caigou_handle.send_username('kingdeetestv3')
        self.caigou_handle.send_password('a1234567')
        self.caigou_handle.click_login()
        time.sleep(3)
        self.caigou_handle.click_menu_yingyong_button()



    def get_purchase_order(self):
        self.caigou_handle.click_purchase_apply()
        self.caigou_handle.click_supplier()

        self.caigou_handle.choose_supplier()
        self.caigou_handle.choose_goods()
        self.caigou_handle.choose_depository()
        self.caigou_handle.depository_one()
        self.caigou_handle.click_goods_one()
        self.caigou_handle.addone_button()
        #加入购物车
        self.caigou_handle.add_to_cart()
        #选择第二个商品
        self.caigou_handle.click_goods_second()
        self.caigou_handle.addone_button()
        self.caigou_handle.add_to_cart()
        #选择好了
        self.caigou_handle.get_goodschoice()
        self.caigou_handle.bill_remake_message("this is a Appium test.")
        #下单
        self.caigou_handle.bill_get()
        #返回
        self.caigou_handle.click_back()



