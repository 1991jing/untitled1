import  json,os,time,xlrd
from appium import webdriver

def ErrorImage(driver):
    NowDate = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    NowTime = time.strftime("%H_%M_%S", time.localtime(time.time()))
    # UrlFrode = "D:\\AppAutomation\\AppData\\Results\\Android\\ErrorImage\\"
    UrlFrode = os.path.join(os.getcwd(), "../AppData/Results/Android/ErrorImage/")
    FoldURL = UrlFrode + NowDate
    FileURL = UrlFrode + NowDate + "\\" + NowTime
    if not os.path.isdir(FoldURL) and not os.path.exists(FoldURL):
        os.mkdir(FoldURL)
    else:
        print("The fold is exist on list")
    ImageURL = FileURL + "Error_png.png"
    driver.get_screenshot_as_file(ImageURL)

#判断元素是否在当前页面
def objDisplay(driver,object):
    if object.is_displayed() == True:
        print("ok")
    else:
        print("not OK")
        ErrorImage(driver)
    return object






