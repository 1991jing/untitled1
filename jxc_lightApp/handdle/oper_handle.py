# coding=utf-8
from jxc_lightApp.page.page_element import LoginPage

class LoginHandle:
    def __init__(self):
        self.login_page = LoginPage()

    # 操作登录页面的元素
    def send_username(self, user):
        '''
        输入用户名
        '''
        self.login_page.get_username_element().send_keys(user)

    def send_password(self, password):
        '''
        输入密码
        '''
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        '''
        点击登录按钮
        '''
        self.login_page.get_login_button_element().click()



    def get_fail_tost(self, message):
        '''
        获取tost，根据返回信息进行反数据
        '''
        tost_element = self.login_page.get_tost_element(message)
        if tost_element:
            return True
        else:
            return False

    def click_loginone_button(self):
        self.login_page.get_loginone_button_element().click()


    def click_menu_yingyong_button(self):
        self.login_page.get_menu_yingyong_button_element().click()



    ##采购操作
    def click_purchase_apply(self):
        self.login_page.get_caigou_element().click()

    def click_supplier(self):
        self.login_page.get_xzgongyingshang_button_element().click()

    def choose_supplier(self):
        self.login_page.get_xzgongyingshang_element().click()

    def choose_goods(self):
        self.login_page.get_xzshangping_button_element().click()

    def choose_depository(self):
        self.login_page.get_xzcangku_element().click()

    def depository_one(self):
        self.login_page.get_cangku_element().click()

    def click_goods_one(self):
        self.login_page.get_xzshangp1_element().click()

    def addone_button(self):
        self.login_page.get_jia1_element().click()

    def add_to_cart(self):
        self.login_page.get_jiarugouwuche_button_element().click()

    def click_goods_second(self):
        self.login_page.get_xzshangp2_element().click()

    def get_goodschoice(self):
        self.login_page.get_xuanzehaole_button_element().click()

    def bill_remake_message(self,message):
        self.login_page.get_bill_remake_element().send_keys(message)

    def  bill_get(self):
        self.login_page.get_commit_button_element().click()

    def click_cg_chakandanju(self):
        self.login_page.get_chakan_button_elemenet().click()

    def click_back(self):
        self.login_page.get_back_element().click()

    def click_shenhe(self):
        self.login_page.get_shenhe_button_element().click()




    #销售操作
    def click_xiaoshou(self):
        self.login_page.xs_xiaoshou_element().click()

    def click_xs_xzkehu(self):
        self.login_page.xs_xzkehu_element().click()

    def click_xs_kehu1(self):
        self.login_page.xs_kehu1_element().click()

    def click_xs_xzshangping_button(self):
        self.login_page.xs_xzshangping_button_element().click()

    def click_xs_xzcangku(self):
        self.login_page.xs_xzcangku_element().click()

    def click_xs_cangku(self):
        self.login_page.xs_cangku_element().click()

    def click_xs_xzshangping1(self):
        self.login_page.xs_xzshangp1_element().click()

    def click_xs_jiarugouwuche_button(self):
        self.login_page.xs_jiarugouwuche_button_element().click()

    def click_xs_xuanzehaole_button(self):
        self.login_page.xs_xuanzehaole_button_element().click()

    def click_xs_commit_button(self):
        self.login_page.xs_commit_button_element().click()

    def click_xs_back(self):
        self.login_page.xs_back_element().click()

    def xs_bill_remake_message(self,message):
        self.login_page.get_bill_remake_element().send_keys(message)




