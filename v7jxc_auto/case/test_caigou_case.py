# coding=utf-8
import sys

from HTMLTestRunner import *
from appium import webdriver

from v7jxc_auto.business.login_business import LoginBusiness
from v7jxc_auto.business.caigou_business import CaigouBusiness

import unittest
import time
from v7jxc_auto.util.base_driver import *


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

        cls.caigou_buiness = CaigouBusiness()



    def setUp(self):
        print ("this is setup")


    def test_01(self):
        print ("采购2个商品")
        self.caigou_buiness.get_purchase_order()



    def tearDown(self):
        time.sleep(1)
        print ("this is teardown")
        if sys.exc_info()[0]:
            self.caigou_buiness.caigou_handle.login_page.driver.save_screenshot("../data/test033.png")
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        print ("this is class teardown")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01"))
    unittest.TextTestRunner().run(suite)

