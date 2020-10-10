from v7jxc_auto.base.base_driver import BaseDriver
from v7jxc_auto.util.findElement import FindElement
import time



class Public_fu(object):

    def __init__(self,i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local= FindElement(self.driver)
        self.gz=self.get_size()

    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

        #向左滑动
    def swipe_left(self):
        size = self.gz
        x1 = self.get_size()[0]/10*9
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10
        self.driver.swipe(x1,y1,x,y1)

    def swipe_right(self):
        size =self.gz
        x1 = self.get_size()[0]/10
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10*9
        self.driver.swipe(x1,y1,x,y1)


    def switch_to_context(self):
        time.sleep(2)  # 因为无法监控，加上web页面加载比较慢所以等待时间比较长
    # 获取页面所有的上下文
        cons = self.driver.contexts  #['NATIVE_APP', 'WEBVIEW_com.kingdee.jdy', 'WEBVIEW_com.android.launcher2']
        print("xxxxxx:" ,cons)
        # 获取当前窗口的上下文
        print("ssssss:",self.driver.current_context)
        #driver.switch_to.context("NATIVE_APP")
        self.driver.switch_to.context(cons[1])
        print("bbbbbbb:",self.driver.current_context)

    def click_app(self,app=None):
        e=self.driver.find_elements_by_id("com.kingdee.jdy:id/ic_app_name")
        print(e)
        for i in e:
            print(i.text)
            if i.text==app:
                i.click()
                break
        time.sleep(5)

    # def click_app_xsdd(self,app=None):
    #     e=self.driver.find_elements_by_id("com.kingdee.jdy:id/ic_app_name")
    #     print("test")
    #     print(e)
    #     for i in e:
    #         print(i.text)
    #     e[0].click()
    def login(self,name,pas,zt_name):
        self.get_by_local.get_element('login_button_one').click()
        self.get_by_local.get_element('username').send_keys(name)
        self.get_by_local.get_element('password').send_keys(pas)
        self.get_by_local.get_element('login_button').click()

        zhangtao=self.driver.find_elements_by_id("com.kingdee.jdy:id/tv_fdb_company_name")

        for zt in zhangtao:
            print(zt.text)
            if zt.text==zt_name:
                zt.click()
            else:
                print("不是%s这个账套" %(zt_name))

        self.get_by_local.driver.find_element_by_id("com.kingdee.jdy:id/tv_fdb_enter").click()

        # 应用
        t=self.driver.find_elements_by_id("com.kingdee.jdy:id/footer_menu_item_icon")
        t[1].click()
        time.sleep(3)

    def login_fn(self,usernamem,password,zhangtao_name):
        #点击同意
        self.get_by_local.get_element("agree").click()
        try:
            self.get_by_local.get_element("Get_permission").click()
            self.get_by_local.get_element("Get_permission").click()
        except:
            print("跳过获取权限")
        #滑动
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        self.swipe_right()

        #登录并选择账套
        self.login(name=usernamem,pas=password,zt_name=zhangtao_name)