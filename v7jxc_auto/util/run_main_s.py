


import os,sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
sys.path.append(rootPath)
sys.path.append(PathProject)


os.system("python D:/v7app_auto/untitled1/v7jxc_auto/case/test1_login_case.py")
os.system("python D:/v7app_auto/untitled1/v7jxc_auto/case/test2_caigou_case.py")

os.system("python ../print1.py")
os.system("python ../print2.py")
