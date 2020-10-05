#coding=utf-8
import configparser

class ReadIni():

    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name ='D:\\v7app_auto\\untitled1\\v7jxc_auto\\data\\localElement.ini'

        if node == None:
            self.node = "login_element"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self,key):
        data = self.cf.get(self.node, key)
        return data
# 获取value的值
if __name__ == '__main__':
    read_init = ReadIni(node='caigou_element')
    print(read_init.get_value('caigou'))


