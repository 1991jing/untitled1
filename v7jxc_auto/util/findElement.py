from v7jxc_auto.util.read_ini import ReadIni

class FindElement(object):

    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key,meg=None):

        read_int = ReadIni(node=meg)
        data = read_int.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        if by == 'id':
            return self.driver.find_element_by_id(value)
        elif by == 'name':
            return self.driver.find_element_by_name(value)
        elif by == 'className':
            return self.driver.find_element_by_class_name(value)
        else:
            return self.driver.find_element_by_xpath(value)

'''
    def get_element_cg(self, key):
        read_int = ReadIni(node='caigou_element')
        data = read_int.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]

        if by == 'id':
            return self.driver.find_element_by_id(value)
        elif by == 'name':
            return self.driver.find_element_by_name(value)
        elif by == 'className':
            return self.driver.find_element_by_class_name(value)
        else:
            return self.driver.find_element_by_xpath(value)

    def get_element_xs(self, key):
        read_int = ReadIni(node='xiaoshou_element')
        data = read_int.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]

        if by == 'id':
            return self.driver.find_element_by_id(value)
        elif by == 'name':
            return self.driver.find_element_by_name(value)
        elif by == 'className':
            return self.driver.find_element_by_class_name(value)
        else:
            return self.driver.find_element_by_xpath(value)
'''