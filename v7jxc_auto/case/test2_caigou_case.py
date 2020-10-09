# coding=utf-8
import sys
# from HtmlTestRunner import *
import HtmlTestRunner
import os,sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
sys.path.append(rootPath)
sys.path.append(PathProject)

from v7jxc_auto.business.caigou_business import CaigouBusiness
from v7jxc_auto.util.server import Server
from v7jxc_auto.util.write_user_command import WriteUserCommand
import unittest
import multiprocessing
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
        cls.caigou_buiness = CaigouBusiness(params)



    def setUp(self):
        self.driver=self.caigou_buiness.driver
        print ("this is setup")


    def test_01(self):
        print ("采购1个商品")
        self.caigou_buiness.get_purchase_order()
        # self.assertTrue(True)


    def test_02(self):
        print ("销售订单下推销售出库单")
        self.caigou_buiness.get_sale_order()
        # self.assertTrue(True)


    def tearDown(self):
        print ("this is teardown")
        # if sys.exc_info()[0]:
        #     self.caigou_buiness.caigou_handle.login_page.driver.save_screenshot("../data/test033.png")
        # time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        Server=appium_init()
        Server.kill_appium()
        print ("this is class teardown")

def get_suite(i):
    print ("get_suite里面的",i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01",parame=i))
    suite.addTest(CaseTest("test_02",parame=i))
    unittest.TextTestRunner().run(suite)

    # suite.addTest(CaseTest("test_02",parame=i))
    # html_file = "D:/v7app_auto/untitled1/v7jxc_auto/util/report/report"+str(i)+".html"
    # fp = open(html_file,"wb")
    # runner=HtmlTestRunner.HTMLTestRunner(stream=fp)
    # runner.run(suite)#执行测试用例


class appium_init():
    def get_main(self):
        server = Server()
        server.main()
        time.sleep(5)
    def kill_appium(self):
        server = Server()
        server.kill_server()



def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count

if __name__ == '__main__':

    appium_init().get_main()
    threads = []
    for i in range(get_count()):
        print (i)
        t = multiprocessing.Process(target=get_suite,args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
