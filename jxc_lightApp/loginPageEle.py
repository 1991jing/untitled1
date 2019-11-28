from jxc_lightApp.util.findElement import FindElement

class LoginPageEle():
    def __init__(self,driver):
        self.fd = FindElement(driver)

    def get_username_element(self):
        return self.fd.get_element('username')



