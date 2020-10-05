from v7jxc_auto.handdle.caigou_handle import CaigouHandle

from v7jxc_auto.handdle.oper_handle import LoginHandle
import time

from v7jxc_auto.handdle.oper_handle import LoginPage


class XiaoshouBusiness(object):
    def __init__(self):
        #销售前操作
        self.xiaoshou_handle = LoginHandle()

        self.xiaoshou_handle.click_loginone_button()

        self.xiaoshou_handle.send_username('kingdeetestv3')
        self.xiaoshou_handle.send_password('a1234567')
        self.xiaoshou_handle.click_login()
        time.sleep(3)


    def get_sales_slip(self):
        self.xiaoshou_handle.click_xiaoshou()
        self.xiaoshou_handle.click_xs_xzkehu()
        self.xiaoshou_handle.click_xs_kehu1()
        self.xiaoshou_handle.click_xs_xzshangping_button()
        time.sleep(2)
        self.xiaoshou_handle.click_xs_xzcangku()
        self.xiaoshou_handle.click_xs_cangku()
        self.xiaoshou_handle.click_xs_xzshangping1()
        self.xiaoshou_handle.click_xs_jiarugouwuche_button()
        self.xiaoshou_handle.click_xs_xuanzehaole_button()
        self.xiaoshou_handle.xs_bill_remake_message('这是一个Appium销售单')
        self.xiaoshou_handle.click_xs_commit_button()
        self.xiaoshou_handle.click_xs_back()
