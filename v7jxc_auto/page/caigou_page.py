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







