__author__ = 'Javier'

import unittest
from selenium import webdriver
import os

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.environ["PATH"] += os.pathsep + "C:\code\workspaces\Python\_miscelanea\Selenium"

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_whater_in_Stockholm(self):
        self.driver.get("http://www.yr.no/")

        search_field = self.driver.find_element_by_id("sted")
        search_field.clear()
        search_field.send_keys("Stockholm")
        search_field.submit()

        topLinkXPathExpression = "//div[@id='directories']/table/tbody/tr/td[2]/a"
        topSearchResult = self.driver.find_element_by_xpath(topLinkXPathExpression)
        topSearchResult.click()

        weather_entry = self.driver.find_element_by_css_selector("li")
        weather_entry.click()

        expected = "Stockholm";
        actualHeadLine = self.driver.find_element_by_css_selector("h1")
        actual = actualHeadLine.text

        self.assertIn(expected, actual)


if __name__ == '__main__':
    unittest.main()
