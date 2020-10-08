# coding=utf-8
import sys

from HtmlTestRunner import *
import multiprocessing
from appium import webdriver
from v7jxc_auto.util.server import Server

from v7jxc_auto.util.write_user_command import WriteUserCommand
from v7jxc_auto.business.login_business import LoginBusiness
from v7jxc_auto.business.xiaoshou_business import XiaoshouBusiness

import unittest

from v7jxc_auto.util.base_driver import *


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        self.param = parame
        global params
        params = parame


class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        global params
        print("这个是setupclass里面的参数:", params)
        cls.caigou_buiness = XiaoshouBusiness(params)



    def setUp(self):
        print ("this is setup")


    def test_01(self):
        print ("采购1个商品")
        self.caigou_buiness.get_purchase_order()



    def tearDown(self):
        time.sleep(1)
        print ("this is teardown")
        # if sys.exc_info()[0]:
        #     self.caigou_buiness.caigou_handle.login_page.driver.save_screenshot("../data/test033.png")
        # time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        print ("this is class teardown")

def appium_init():
    server = Server()
    server.main()
    time.sleep(5)

def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count

def get_suite(i):
    print ("get_suite里面的",i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01",parame=i))
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    appium_init()
    # suite = unittest.TestSuite()
    # suite.addTest(CaseTest("test_01"))
    # unittest.TextTestRunner().run(suite)
    threads = []
    for i in range(get_count()):
        print (i)
        t = multiprocessing.Process(target=get_suite,args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
