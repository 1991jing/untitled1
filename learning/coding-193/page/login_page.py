#coding=utf-8
from util.get_by_local import GetByLocal
import time
from base.base_driver import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
	# 获取登录页面所有的页面元素信息
	def __init__(self,i):
		base_driver = BaseDriver()
		self.driver = base_driver.android_driver(i)
		self.get_by_local = GetByLocal(self.driver)

	def get_username_element(self):
		'''
		获取用户名元素信息
		'''	
		return self.get_by_local.get_element('username')

	def get_password_element(self):
		'''
		获取密码元素信息
		'''	
		return self.get_by_local.get_element('password')

	def get_login_button_element(self):
		'''
		获取登陆按钮元素信息
		'''
		return self.get_by_local.get_element('login_button')

	def get_forget_password_element(self):
		'''
		忘记密码元素
		'''
		return self.get_by_local.get_element('forget_password')

	def get_register_element(self):
		'''
		注册元素
		'''
		return self.get_by_local.get_element('register')

	def get_tost_element(self,message):
		'''
		获取tostelement
		'''
		time.sleep(2)
		tost_element = ("xpath","//*[contains(@text,"+message+")]")
		return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(tost_element))

