import time

from v7jxc_auto.util.findElement import FindElement
from v7jxc_auto.util.base_driver import BaseDriver
from v7jxc_auto.page.page_element import LoginPage


class CaigouPage(object):
    # 获取采购页面所有的页面元素信息
    def __init__(self,driver=None):

        self.fd = FindElement(driver)

    def get_caigou_element(self):
        return self.fd.get_element(key='caigou',meg='caigou_element')

    def get_xzgongyingshang_button_element(self):
        return self.fd.get_element(key='xzgongyingshang_button',meg='caigou_element')

    def get_xzgongyingshang_element(self):
        return self.fd.get_element(key='xzgongyingshang',meg='caigou_element')

    def get_xzshangping_button_element(self):
        return self.fd.get_element('xzshangping_button',meg='caigou_element')

    def get_xzcangku_element(self):
        return self.fd.get_element('xzcangku',meg='caigou_element')

    def get_cangku_element(self):
        return self.fd.get_element('1haocang',meg='caigou_element')

    def get_jia1_element(self):
        return self.fd.get_element('jia1',meg='caigou_element')

    def get_jiarugouwuche_button_element(self):
        return self.fd.get_element('jiarugouwuche_button',meg='caigou_element')

    def get_xzshangp2_element(self):
        return self.fd.get_element('xzshangp2',meg='caigou_element')

    def get_xuanzehaole_button_element(self):
        return self.fd.get_element('xuanzehaole_button',meg='caigou_element')

    def get_bill_remake_element(self):
        return self.fd.get_element('bill_remake',meg='caigou_element')

    def get_commit_button_element(self):
        return self.fd.get_element('commit_button',meg='caigou_element')

    def get_back_element(self):
        return self.fd.get_element('back',meg='caigou_element')





