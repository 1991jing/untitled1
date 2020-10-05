# -*- coding:utf-8 -*-

#保存成功页面

def sale_finish(driver):
    #保存成功
    driver.tv_sale_finish = driver.find_element_by_id("com.kingdee.jdy:id/tv_sale_finish")
    #打印
    driver.tv_sale_finish_bluetooth = driver.find_element_by_id("com.kingdee.jdy:id/tv_sale_finish_bluetooth")
    #查看/分享单据
    driver.tv_sale_finish_share = driver.find_element_by_id("com.kingdee.jdy:id/tv_sale_finish_share")
    #历史单据
    driver.tv_sale_finish_history = driver.find_element_by_id("com.kingdee.jdy:id/tv_sale_finish_history")
    #查看开单
    driver.tv_sale_finish_continue = driver.find_element_by_id("com.kingdee.jdy:id/tv_sale_finish_continue")


