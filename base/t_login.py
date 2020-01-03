#coding:utf-8
from CommonTools import operation_json
from selenium import webdriver
import time
# class Login:
#     def __init__(self):
#
#     def get_data(self):
#         data = operation_json()
#
driver = webdriver.Chrome()
# driver.maximize_window()

first_url = 'http://62.234.200.243:8995/users/sign_in'
print("now access %s"%(first_url))
driver.get(first_url)
driver.find_element_by_class_name("el-input__inner").send_keys('huangping')
driver.find_element_by_xpath("//div[@class='login-input password-input el-input']/input").send_keys('hp123456')
target=driver.find_element_by_id("nc_1_n1z")
js="window.scrollTo(100,450);"
driver.execute_script(js)
time.sleep(1)
driver.find_element_by_xpath("//button[@class='el-button login-btn el-button--primary is-round']/span").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='dropdown-toggle']/span[@class='user-text']").click()
driver.find_element_by_link_text('安全退出').click()
driver.find_element_by_xpath("//div[@class='modal-content']/div[@class='modal-footer']/a[@class='btn btn-primary']").click()
# driver.find_element_by_css_selector("a.btn.btn-primary").click()
driver.find_elements(self.brower,"classname","btn btn-primary").click()
time.sleep(10)
driver.quit()