import unittest
import ddt
from ddt import ddt, data, unpack
from WebUI.pageObject.search_page import SearchPage
from selenium import webdriver
from time import sleep

@ddt
class TestCases(unittest.TestCase):

    # condition
    def setUp(self) -> None:
        self.sp = SearchPage(webdriver, 'kw', 'su')

    # back condition
    def tearDown(self) -> None:
        self.sp.quit_browser()

    @data(['http://www.baidu.com', 'pure storage'], ['http://www.baidu.com', 'pure storage'])
    @unpack
    def test_1(self, url, input_text):
        self.sp.check(url, input_text)
        sleep(2)
        # self.assertEqual(self.sp.get_title(), "百度一下，你就知道", msg="Error")


if __name__ == "__main__":
    unittest.main()


