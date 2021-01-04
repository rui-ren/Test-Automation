"""
Generate the HTML file report
"""

import unittest
from HtmlTestRunner import HTMLTestRunner
from .test_cases.test_http_request import TestHttpRequest
from API_Testing.utils.project_path import *

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

file_name = report_path
with open(file_name, 'w', encoding='utf-8') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        output='./report',
        report_name="test_api report",
        add_timestamp=False,
        open_in_browser=True
    )
    runner.run(suite)

