from v7jxc_auto.util.server import Server
import time
from v7jxc_auto.util.write_user_command import WriteUserCommand
import multiprocessing
import unittest
import sys
sys.path.append("D:/v7app_auto/untitled1/v7jxc_auto")
from v7jxc_auto.case.test2_caigou_case import *
from HtmlTestRunner import *
# from v7jxc_auto.case.test3_xiaoshou_case import *

def appium_init():
    server = Server()
    server.main()
    time.sleep(5)

def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count

# def get_suite(i):
#     print ("get_suite里面的",i)
#     suite = unittest.TestSuite()
#     suite.addTest(CaseTest("test_01",parame=i))
#     unittest.TextTestRunner().run(suite)

# def get_suite(i):
#     print ("get_suite里面的",i)
#     suite = unittest.TestSuite()
#     suite.addTest(CaseTest("test_01",parame=i))
#     suite.addTest(CaseTest("test_02",parame=i))
#     html_file = "E:/Teacher/Imooc/AppiumPython/report/report"+str(i)+".html"
#     fp = open(html_file,"wb")
#     HTMLTestRunner(stream=fp).run(suite)

appium_init()

threads = []
for i in range(get_count()):
    print (i)
    t = multiprocessing.Process(target=get_suite,args=(i,))
    threads.append(t)
for j in threads:
    j.start()










