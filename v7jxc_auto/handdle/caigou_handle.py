from v7jxc_auto.page.caigou_page import CaigouPage
from v7jxc_auto.business.login_business import LoginBusiness
from v7jxc_auto.handdle.oper_handle import LoginPage


class CaigouHandle:
    def __init__(self):

        self.login_page =  LoginPage()

        self.login_page.get_loginone_button_element().click()
        self.login_page.get_username_element().send_keys('kingdeetestv3')
        self.login_page.get_password_element().send_keys('a1234567')
        self.login_page.get_login_button_element().click()

        self.login_page.get_menu_yingyong_button_element().click()

        self.caigou_page = CaigouPage(self.login_page)





    # def click_purchase_apply(self):
    #     self.caigou_page.get_caigou_element().click()
    #
    # def click_supplier(self):
    #     self.caigou_page.get_xzgongyingshang_button_element().click()
    #
    # def choose_supplier(self):
    #     self.caigou_page.get_xzgongyingshang_element().click()
    #
    # def choose_goods(self):
    #     self.caigou_page.get_xzshangping_button_element().click()
    #
    # def choose_depository(self):
    #     self.caigou_page.get_xzcangku_element().click()
    #
    # def depository_one(self):
    #     self.caigou_page.get_cangku_element().click()
    #
    # def click_goods_one(self):
    #     self.caigou_page.get_xzshangping_button_element().click()
    #
    # def addone_button(self):
    #     self.caigou_page.get_jia1_element().click()
    #
    # def add_to_cart(self):
    #     self.caigou_page.get_jiarugouwuche_button_element().click()
    #
    # def click_goods_second(self):
    #     self.caigou_page.get_xzshangp2_element().click()
    #
    # def get_goodschoice(self):
    #     self.caigou_page.get_xuanzehaole_button_element().click()
    #
    # def bill_remake_message(self,message):
    #     self.caigou_page.get_bill_remake_element().send_keys(message)
    #
    # def  bill_get(self):
    #     self.caigou_page.get_commit_button_element().click()
    #
    # def click_back(self):
    #     self.caigou_page.get_back_element().click()

