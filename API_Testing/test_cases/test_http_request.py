import sys
import os

import unittest
from ddt import ddt, data
from API_Testing.utils.project_path import *
from API_Testing.utils import read_excel
from API_Testing.utils import read_config
from API_Testing.utils import http_request

cookie = None
test_data = read_excel.Read_the_excel.get_data(test_case_path, config_path)

@ddt()
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self, item):
        res = http_request.HttpRequest.http_request(item['url'],
        eval(item['data']),
        item['method'])

        if res.cookies:
            pass
        try:
            self.assertEqual(item['expected'], res.json()['info'])
            TestResult = 'PASS'
        except AssertionError as e:
            TestResult = 'FAILED'
            print('Run Error: {}'.format(e))
            raise e
        finally:
            print('get the result: {}'.format(res.json()))

    def tearDown(self) -> None:
        pass

if __name__ == "__main__":
    unittest.main()

