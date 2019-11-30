# coding=utf-8
import sys

from HTMLTestRunner import *
from appium import webdriver

from jxc_lightApp.business.login_business import LoginBusiness
from jxc_lightApp.business.xiaoshou_business import XiaoshouBusiness

import unittest
import time
from jxc_lightApp.util.base_driver import *


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', param=None):
        super(ParameTestCase, self).__init__(methodName)
        self.param = param
        global params
        params = param


class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        global params
        print("这个是setupclass里面的参数:", params)

        cls.xiaoshou_buiness = XiaoshouBusiness()



    def setUp(self):
        print ("this is setup")


    def test_01(self):
        print ("销售1个商品")
        self.xiaoshou_buiness.get_sales_slip()



    def tearDown(self):
        time.sleep(1)
        print ("this is teardown")
        if sys.exc_info()[0]:
            self.xiaoshou_buiness.xiaoshou_handle.login_page.driver.save_screenshot("../data/test033.png")
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        print ("this is class teardown")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01"))
    unittest.TextTestRunner().run(suite)

