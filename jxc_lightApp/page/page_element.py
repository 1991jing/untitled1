import time

from jxc_lightApp.util.findElement import FindElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from jxc_lightApp.util.base_driver import BaseDriver


class LoginPage(object):
    # 获取登录页面所有的页面元素信息
    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.basedriver()
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

    ##采购页面的元素
    def get_menu_yingyong_button_element(self):
        return self.fd.get_element('menu_yingyong_button')

    def get_caigou_element(self):
        return self.fd.get_element(key='caigou',meg='caigou_element')

    def get_xzgongyingshang_button_element(self):
        return self.fd.get_element(key='xzgongyingshang_button',meg='caigou_element')

    def get_xzgongyingshang_element(self):
        return self.fd.get_element(key='xzgongyingshang',meg='caigou_element')

    def get_xzshangping_button_element(self):
        return self.fd.get_element(key='xzshangping_button',meg='caigou_element')

    def get_xzcangku_element(self):
        return self.fd.get_element(key='xzcangku',meg='caigou_element')

    def get_cangku_element(self):
        return self.fd.get_element(key='1haocang',meg='caigou_element')

    def get_jia1_element(self):
        return self.fd.get_element(key='jia1',meg='caigou_element')

    def get_jiarugouwuche_button_element(self):
        return self.fd.get_element(key='jiarugouwuche_button',meg='caigou_element')

    def get_xzshangp1_element(self):
        return self.fd.get_element(key='xzshangp1',meg='caigou_element')

    def get_xzshangp2_element(self):
        return self.fd.get_element(key='xzshangp2',meg='caigou_element')

    def get_xuanzehaole_button_element(self):
        return self.fd.get_element(key='xuanzehaole_button',meg='caigou_element')

    def get_bill_remake_element(self):
        return self.fd.get_element(key='bill_remake',meg='caigou_element')

    def get_commit_button_element(self):
        return self.fd.get_element(key='commit_button',meg='caigou_element')

    def get_back_element(self):
        return self.fd.get_element(key='back',meg='caigou_element')

    def get_chakan_button_elemenet(self):
        return self.fd.get_element(key='chakan_button',meg='caigou_element')

    def get_caigoulishi_button_elemnt(self):
        return  self.fd.get_element(key='caigoulishi_button',meg='caigou_element')

    def get_jixukaidan_button_element(self):
        return self.fd.get_element(key='jixukaidan_button',meg='caigou_element')

    def get_shenhe_button_element(self):
        return self.fd.get_element(key='shenhe_button',meg='caigou_element')


#销售页面元素
    def xs_xiaoshou_element(self):
        return self.fd.get_element(key='xiaoshou',meg='xiaoshou_element')

    def xs_xzkehu_element(self):
        return self.fd.get_element(key='xzkehu',meg='xiaoshou_element')

    def xs_kehu1_element(self):
        return self.fd.get_element(key='kehu1',meg='xiaoshou_element')

    def xs_xzshangping_button_element(self):
        return self.fd.get_element(key='xzshangping_button',meg='xiaoshou_element')

    def xs_xzcangku_element(self):
        return self.fd.get_element(key='xzcangku',meg='xiaoshou_element')

    def xs_cangku_element(self):
        return self.fd.get_element(key='cangku',meg='xiaoshou_element')

    def xs_xzshangp1_element(self):
        return self.fd.get_element(key='shangp1',meg='xiaoshou_element')

    def xs_jiarugouwuche_button_element(self):
        return self.fd.get_element(key='jiarugouwuche_button',meg='xiaoshou_element')

    def xs_xuanzehaole_button_element(self):
        return self.fd.get_element(key='xuanzehaole_button',meg='xiaoshou_element')

    def xs_commit_button_element(self):
        return self.fd.get_element(key='commit_button',meg='xiaoshou_element')

    def xs_back_element(self):
        return self.fd.get_element(key='back',meg='xiaoshou_element')

    def xs_get_chakan_button_elemenet(self):
        return self.fd.get_element(key='chakan_button',meg='xiaoshou_element')

    def xs_get_caigoulishi_button_elemnt(self):
        return  self.fd.get_element(key='caigoulishi_button',meg='xiaoshou_element')

    def xs_get_jixukaidan_button_element(self):
        return self.fd.get_element(key='jixukaidan_button',meg='xiaoshou_element')

    def xs_get_beizhu(self):
        return self.fd.get_element(key='bill_remark',meg='xiaoshou_element')


if __name__ == '__main__':
    LG=LoginPage()
    print('1')
    print(LG.get_loginone_button_element())
    print('2')
    LG.get_loginone_button_element().click()