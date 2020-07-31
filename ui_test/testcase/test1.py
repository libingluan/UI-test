import unittest

from selenium import webdriver

driver = webdriver.Chrome()
#driver.maximize_window() # 浏览器最大化

driver.implicitly_wait(3)  # 等待3秒

driver.get("http://user-dev4.tangees.com")

driver.find_element_by_xpath(type="text").send_keys("18578731109")
driver.find_element_by_xpath(type="password").send_keys("Aaa111")

driver.implicitly_wait(1)
driver.find_element_by_xpath(type="button").click()


import common
# class Testlogin(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(3)
#         self.base_url = 'https://user-dev4.tangees.com'
#         #self.testCaseInfo = TestCaseInfo()
#
#     def test_login(self):
#         # 打开网页
#         self.driver.get(self.base_url)
#
#     def tearDown(self):
#         # self.driver.close()
#         pass


if  __name__  ==  '__main__':
    unittest.main()
