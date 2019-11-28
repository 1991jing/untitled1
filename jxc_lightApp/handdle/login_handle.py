# coding=utf-8
from jxc_lightApp.page.login_page import LoginPage

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

    def get_loginone_button(self):
        self.login_page.get_loginone_button_element().click()

