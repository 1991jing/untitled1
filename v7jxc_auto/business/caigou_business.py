from v7jxc_auto.base.base_driver import BaseDriver
from v7jxc_auto.util.findElement import FindElement
import time
from selenium.webdriver.common.keys import Keys
from  v7jxc_auto.business.public import Public_fu


class CaigouBusiness(object):
    def __init__(self,i,):

        public = Public_fu(i)

        self.driver = public.driver
        #应用页面
        public.login_fn(usernamem="kingdeetest5854",password="a1234567",zhangtao_name="AUTO_TEST")
        self.app=public.click_app
        # self.app_xsdd=public.click_app(app="销售订单")
        self.fe=public.get_by_local


    def quit_driver(self):
        self.driver.quit()
        # self.context=public.switch_to_context()

    def switch_to_context(self,s):
        #s=0 原生；s=1 H5
        time.sleep(2)  # 因为无法监控，加上web页面加载比较慢所以等待时间比较长
        # 获取页面所有的上下文
        cons = self.driver.contexts  #['NATIVE_APP', 'WEBVIEW_com.kingdee.jdy', 'WEBVIEW_com.android.launcher2']
        print("xxxxxx:" ,cons)
        # 获取当前窗口的上下文
        print("ssssss:",self.driver.current_context)
        self.driver.switch_to.context(cons[s])
        print("bbbbbbb:",self.driver.current_context)

    def get_purchase_order(self):
        time.sleep(5)
        #做采购单
        self.app(app="采购入库")

        self.switch_to_context(s=1)

        self.fe.get_element('add',meg="caigou_element").click()
        self.switch_to_context(s=1)
        # print (driver.page_source)

        self.fe.get_element('add_supplier',meg="caigou_element").send_keys(u"河源供应商")
        #select_supplier
        self.switch_to_context(s=1)

        self.fe.get_element('select_supplier',meg="caigou_element").click()

        self.switch_to_context(s=1)

        self.fe.get_element('add_goods',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('h1_warehouse',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('search_warehouse_baihuo',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('search_box',meg="caigou_element").send_keys(u"益达").send_keys(Keys.ENTER)
        self.switch_to_context(s=1)
        self.fe.get_element('select_goods',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('goods_quantity',meg="caigou_element").clear().send_keys(10)

        self.fe.get_element('confirm',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('confirm_select',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('Settlement',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('pay',meg="caigou_element").click()
        self.fe.get_element('account',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('select_account',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('pay_for',meg="caigou_element").send_keys(50)


        self.switch_to_context(s=1)
        self.fe.get_element('show_more',meg="caigou_element").click()
        time.sleep(3)

        self.fe.get_element('Place_order',meg="caigou_element").click()

        time.sleep(2)
        self.switch_to_context(s=1)
        self.fe.get_element('purinbound_list',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('select_date',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('date_today',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('purinbound_staus',meg="caigou_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('unaudited',meg="caigou_element").click()
        self.switch_to_context(s=1)
        #打印订单编号
        print(self.fe.get_element('billno',meg="caigou_element").text)

        self.fe.get_element('billno',meg="caigou_element").click()
        self.switch_to_context(s=1)
        #审核单据
        self.fe.get_element('audit_button',meg="caigou_element").click()
        self.switch_to_context(s=0)
        self.fe.get_element("close",meg="caigou_element").click()

    def get_sale_order(self):
        time.sleep(5)
        print("1")
        self.app(app="销售订单")
        print("2")
        self.switch_to_context(s=1)

        self.fe.get_element('add',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('coustmer_botton',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('search_coustmer_box',meg="saleOrder_element").send_keys(u"华为")
        time.sleep(3)
        self.fe.get_element('select_coustmer',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('salesman_button',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('select_salesman_baili',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('add_goods',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('goods_group_lingshi',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('jia',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('goods_showmore',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('select_stock',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('select_stock_baihuo',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('good_quantity',meg="saleOrder_element").clear().send_keys(5)
        self.fe.get_element('discont2',meg="saleOrder_element").click()
        self.fe.get_element('discont2_money',meg="saleOrder_element").send_keys(3)
        self.fe.get_element('confirm',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('confirm_select',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('Settlement',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('deposit_button',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('account',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('select_account',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('deposit_pay',meg="saleOrder_element").send_keys(47)
        self.fe.get_element('pay_showmore',meg="saleOrder_element").click()
        self.fe.get_element('place_saleorder',meg="saleOrder_element").click()

        #下推

        self.switch_to_context(s=1)
        self.fe.get_element('saleOrder_list',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('select_date',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('date_today',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('purinbound_staus',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        T=self.fe.get_element('unaudited',meg="saleOrder_element")
        print(T.text)
        T.click()
        # get_by_local.get_element('unaudited',meg="saleOrder_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('saleorder_billno',meg="saleOrder_element").click()

        self.switch_to_context(s=1)
        self.fe.get_element('saleorder_audit_button',meg="saleOrder_element").click()
        time.sleep(5)
        self.fe.get_element('out_warehousr',meg="saleOrder_element").click()
        #出库
        self.switch_to_context(s=1)
        self.fe.get_element('Settlement',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('collection_button',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('account',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('select_account',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('collection',meg="salOutbound_element").send_keys(47)
        self.switch_to_context(s=1)
        self.fe.get_element('place_saleorder',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('saleOrder_list',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('select_date',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('date_today',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('purinbound_staus',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('unaudited',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('saleorder_billno',meg="salOutbound_element").click()
        self.switch_to_context(s=1)
        self.fe.get_element('saleorder_audit_button',meg="salOutbound_element").click()

        print("=====订单下推成功=====")





