import time

from v7jxc_auto.util.findElement import FindElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from v7jxc_auto.base.base_driver import BaseDriver


class LoginPage(object):
    # 获取登录页面所有的页面元素信息
    def __init__(self,i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.fd = FindElement(self.driver)



    def get_username_element(self):
        '''
        获取用户名元素信息
        '''
        return self.fd.get_element('username')

    def get_password_element(self):
        '''
        获取密码元素信息
        '''
        return self.fd.get_element('password')

    def get_login_button_element(self):
        '''
        获取登陆按钮元素信息
        '''
        return self.fd.get_element('login_button')

    def get_forget_password_element(self):
        '''
        忘记密码元素
        '''
        return self.fd.get_element('forget_password')

    def get_register_element(self):
        '''
        注册元素
        '''
        return self.fd.get_element('register_button')

    def get_tost_element(self,message):
        '''
        获取tostelement
        '''
        time.sleep(2)
        tost_element = ("xpath","//*[contains(@text,"+message+")]")
        return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(tost_element))


    def get_loginone_button_element(self):

        return self.fd.get_element('login_button_one')


    def get_agree_button_element(self):
        return self.fd.get_element("agree").click()


    ##采购页面的元素
    def get_menu_yingyong_button_element(self):
        return self.fd.get_element('menu_yingyong_button')




    #销售页面元素



if __name__ == '__main__':
    LG=LoginPage()
    print('1')
    print(LG.get_loginone_button_element())
    print('2')
    LG.get_loginone_button_element().click()