# coding=utf-8
from v7jxc_auto.handdle.oper_handle import LoginHandle


class LoginBusiness(object):
    def __init__(self,i):
        self.login_handle = LoginHandle(i)

    # def login_button_one_click(self):
    #     self.login_handle.click_loginone_button()
    #
    # def get_click_menu_yingyong_button(self):
    #     self.login_handle.click_menu_yingyong_button()


    def login_pass(self):

        self.login_handle.click_agree()
        try:
            self.login_handle.click_auth()
            self.login_handle.click_auth()
        except:
            print("没有点击权限")
        self.login_handle.click_loginone_button()
        self.login_handle.send_username('kingdeetestv3')
        self.login_handle.send_password('a1234567')
        self.login_handle.click_login()

    def login_user_error(self):
        # self.login_handle.click_agree()
        # try:
        #     self.login_handle.click_auth()
        #     self.login_handle.click_auth()
        # except:
        #     print("没有点击权限")
        # self.login_handle.click_loginone_button()
        self.login_handle.send_username('kingdeetestv')
        self.login_handle.send_password('a1234567')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost('登录名或密码错误')
        if user_flag:
            return True
        else:
            return False

    def login_password_error(self):
        # self.login_handle.click_agree()
        # try:
        #     self.login_handle.click_auth()
        #     self.login_handle.click_auth()
        # except:
        #     print("没有点击权限")
        # self.login_handle.click_loginone_button()
        self.login_handle.send_username('kingdeetestv3')
        self.login_handle.send_password('111112')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost('登录名或密码错误')
        if user_flag:
            return True
        else:
            return False

    # def get_size(self):
    #     size = self.driver.get_window_size()
    #     width = size['width']
    #     height = size['height']
    #     return width, height
    #
    # # 向左滑动
    #
    # def swip_left(self):
    #     get_size = self.get_size()
    #     x1 = get_size[0] / 10 * 9
    #     y1 = get_size[1] / 2
    #     x = get_size[0] / 10
    #     self.driver.swipe(x1, y1, x, y1)
    #
    # def swipe_right(self):
    #     get_size = self.get_size()
    #     x1 = get_size[0] / 10
    #     y1 = get_size[1] / 2
    #     x = get_size[0] / 10 * 9
    #     self.driver.swipe(x1, y1, x, y1)
    #
    # def swipe_on(self,direction):
    #     if direction == 'left':
    #         self.swip_left()
    #     elif direction == 'right':
    #         self.swipe_right()
