#!/usr/bin/python
#======================================================================
# TC_001 - Search for a product in site - Positive case
#
# (c) 2018 <company-name>. All rights reserved.
#
# Tabstop: 4
#
#======================================================================

try:

    import unittest
    from selenium import webdriver

except:

    print "IMPORT ERROR"
    raise

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class Amazon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def search(self):
        self.driver.get('https://www.amazon.com')
	self.driver.implicitly_wait(30)
	self.driver.maximize_window()
        search_input = self.driver.find_element_by_css_selector(
		'#content input[type="text"]')
	search_input.send_keys('iphone 6s')
	search_submit = self.driver.find_element_by_css_selector(
		'#content input[type="submit"]')
	search_submit.click()

	# Using both find_element_by_css_selector and find_element_by_id just to show that elements can be located in multiple ways.
	self.assertTrue(self.driver.find_element_by_id("twotabsearchtextbox")
	# We can also use XPATH here

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

if __name__ == '__main__':
    unittest.main()
