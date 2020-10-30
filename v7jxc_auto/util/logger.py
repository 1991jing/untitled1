#coding=utf-8
import yaml
import logging.config
import os,concurrent_log



class Log(object):
    def __init__(self):
        self.setup_logging()
        self.lg=logging.getLogger("jxc_v7_app")

    def debug(self,message):
        self.lg.debug(message)

    def info(self,message):
        self.lg.info(message)


    def error(self,message):
        self.lg.error(message)


    def setup_logging(self,default_level = logging.DEBUG):

        path = "D://v7app_auto//untitled1//v7jxc_auto//data//logconfig.yaml"

        # debuglog_path ="D://v7app_auto//untitled1//v7jxc_auto//log//debug.log"
        #
        # ifolog_path = "D://v7app_auto//untitled1//v7jxc_auto//log//info.log"
        #
        # errlog_path = "D://v7app_auto//untitled1//v7jxc_auto//log//errors.log"
        # #清空log文件
        # if os.path.exists(ifolog_path):
        #     with open(ifolog_path, "w") as f:
        #         f.truncate()
        #
        # if os.path.exists(errlog_path):
        #     with open(errlog_path, "w") as f:
        #         f.truncate()
        #
        # if os.path.exists(debuglog_path):
        #     with open(debuglog_path, "w") as f:
        #         f.truncate()
         #读取log配置
        if os.path.exists(path):
            with open(path,"r") as f:
                config = yaml.load(f,Loader=yaml.FullLoader)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level = default_level)

if __name__ == "__main__":
    lg=Log()
    lg.info("1")
    lg.debug("2")
    lg.error("3")
    lg.info("4")
    # log = logging.getLogger("myname")

