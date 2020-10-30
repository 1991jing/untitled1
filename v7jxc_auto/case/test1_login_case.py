# coding=utf-8
import sys
import multiprocessing
from v7jxc_auto.util.server import Server
from HTMLTestRunner import *
from appium import webdriver
from v7jxc_auto.util.write_user_command import WriteUserCommand

from v7jxc_auto.business.login_business import LoginBusiness
import unittest
import time
from v7jxc_auto.util.base_driver import *
from BeautifulReport import BeautifulReport


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        self.param = parame
        global params
        params = parame


class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):

        print("这个是setupclass里面的参数:", params)
        cls.login_business = LoginBusiness(params)

        # cls.login_business.login_button_one_click()

    def setUp(self):
        print ("this is setup")


    def test_01_login_user_error(self):
        print ("测试登录错误")
        self.login_business.login_user_error()
        self.assertTrue(True)

    def test_02_login_pass(self):
        print ("测试登录成功")
        self.login_business.login_pass()


    def tearDown(self):
        time.sleep(1)
        print ("this is teardown")
        if sys.exc_info()[0]:
            self.login_business.login_handle.login_page.driver.save_screenshot("../data/test033.png")
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        Server=appium_init()
        Server.kill_appium()
        print ("this is class teardown")

class appium_init():
    def __init__(self):
        self.server = Server()
    def get_main(self):
        self.server.main()
        time.sleep(5)
    def kill_appium(self):
        self.server.kill_server()

def get_suite(i):
    print ("get_suite里面的",i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01_login_user_error",parame=i))
    suite.addTest(CaseTest("test_02_login_pass",parame=i))
    # unittest.TextTestRunner().run(suite)
    from pathlib import Path
    name=Path(__file__).name.split(".py")[0]
    filePath = u'D:\\v7app_auto\\untitled1\\v7jxc_auto\\util\\report\\test.html'  # 确定生成报告的路径
    html_file2 = "D:/v7app_auto/untitled1/v7jxc_auto/util/report/"+name+str(i)+"/"
    # fp = file(html_file,"wb")
    result = BeautifulReport(suite)
    result.report(filename='V7移动测试报告', description='测试v7APP报告', report_dir=html_file2)
    # 运行测试用例
    print("")
    print("----------All Done!-------")

def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count

if __name__ == '__main__':
    appium_init().get_main()
    threads = []
    for i in range(get_count()):
        t = multiprocessing.Process(target=get_suite,args=(i,))
        threads.append(t)
    for j in threads:
        j.start()




