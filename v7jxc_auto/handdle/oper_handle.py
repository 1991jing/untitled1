# coding=utf-8
from v7jxc_auto.page.page_element import LoginPage

class LoginHandle:
    def __init__(self,i):
        self.login_page = LoginPage(i)


    # 操作登录页面的元素
    def send_username(self,user):
        #输入用户名
        self.login_page.get_username_element().send_keys(user)

    def click_agree(self):
         self.login_page.get_agree_element().click()

    def click_auth(self):
        self.login_page.get_auth_element().click()

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
    # def click_purchase_apply(self):
    #     self.login_page.get_caigou_element().click()





