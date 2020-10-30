#coding=utf-8
import os
from v7jxc_auto.util.logger import Log
class DosCmd:
    def excute_cmd_result(self,command):
        lg= Log()
        result_list = []
        result = os.popen(command).readlines()
        lg.info(result)
        lg.info("=======================================================================================================================================")

        for i in result:
                if i =='\n':
                    continue
                result_list.append(i.strip('\n'))
        return result_list

    def excute_cmd(self,command):
        # os.putenv("Path","D:\\tool\\sdk\\tools")
        os.system(command)

if __name__ == '__main__':
    dos = DosCmd()

    # os.system('chcp 65001')

    dos.excute_cmd_result("adb devices")
    dos.excute_cmd('appium -p 4700 -bp 4701 -U NAB0220629016963')
