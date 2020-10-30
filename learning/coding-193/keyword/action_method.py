# coding=utf-8
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ActionMethod:

    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(0)
        self.get_by_local = 0(self.driver)

    def input(self, *args):
        '''
        输入值
        '''
        # key,value
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        element.send_keys(args[1])

    def on_click(self, *args):
        '''
        元素点击
        '''
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        element.click()

    def sleep_time(self, *args):
        time.sleep(int(args[0]))

    # 获取屏幕的宽高
    def get_size(self, *args):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self, *args):
        #[100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向右边滑动
    def swipe_right(self, *args):
        #[100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向上滑动
    def swipe_up(self, *args):
        #[100,200]direction
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 6
        y = self.get_size()[1] / 10*2
        self.driver.swipe(x1, y1, x1, y, 1000)

    # 向下滑动
    def swipe_down(self, *args):
        #[100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def get_element(self, args: object) -> object:
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return None
        return element
        
	def get_tost_element(self,*args):
		'''
		获取tostelement
		'''
		time.sleep(2)
		tost_element = ("xpath","//*[contains(@text,"+args[0]+")]")
		return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(tost_element))

