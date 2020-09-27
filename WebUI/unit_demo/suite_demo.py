import unittest
from WebUI.unit_demo.test_for_key import TestForKey
from ddt import ddt, data, file_data, unpack
# constructor the suite
suite = unittest.TestSuite()

# add the test case

suite.addTest(TestForKey('id','http://www.meituan.com'))
# suite.addTest(TestKeyWords("Chrome", "http://www.baidu.com"))
# suite.addTest(TestKeyWords("Chrome", "http://www.google.com"))

# use the Runner to run the unittest suite
runner = unittest.TextTestRunner()
runner.run(suite)
