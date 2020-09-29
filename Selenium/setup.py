from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt, data, unpack, file_data
import unittest
from time import sleep
import yaml

@ddt()
class GoogleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    @data(['http://www.google.com', 'pure storage'], ['http://www.google.com', 'blade array'])
    @unpack
    def test_1(self, url, input_text):
        self.driver.get(url)
        elem = self.driver.find_element_by_name('q')
        elem.send_keys(input_text)
        elem.send_keys(Keys.ENTER)
        assert 'Google' in self.driver.title
        sleep(3)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


