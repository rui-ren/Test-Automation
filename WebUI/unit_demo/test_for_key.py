import unittest
from WebUI.test_keywords_demo import TestKeyWords
from time import sleep
from ddt import ddt, data, unpack

@ddt
class TestForKey(unittest.TestCase):
        # every test case will be run
        def setUp(self):
            self.tk = TestKeyWords("Chrome", "http://www.baidu.com")
            print('SetUp')

        # every test case will be run once
        def tearDown(self):
            self.tk.quit_browser()
            print('tearDown')
        # we have to have the underline
        # * use the tuple format to unpack the array.
        # ** use the dictionary format, key and value format.
        @data(['id', 'pure storage'], ['id', 'ideal'])
        @unpack
        def test_1(self, locator, input_value):
            self.tk.input_text(locator, "kw", input_value)
            self.tk.click_element(locator, "su")
            sleep(1)


if __name__ == "__main__":
    unittest.main()

