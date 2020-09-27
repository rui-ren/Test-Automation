import unittest
import requests
import json
from ddt import ddt, file_data, data
import pytest
import yaml
from Interface_Test.logger import logger

# read the yaml file here
def read_yaml():
    with open(r'C:\Users\ruire\Documents\GitHub\automated-testing\Interface_Test\config\data.yaml', 'r') as f:
        cfg = yaml.load(f.read())
        return cfg

data = read_yaml()
url = data['api_url']
print(data['api_url'])

class HttpClient():
    """
    encapusule the request and post
    """
    # def get(self):
    #
    #
    # def post(self):
    #
    # def send_request(self):
    #     if :
    #         self.get()
    #
    #     if :
    #         self.post()

@ddt
class TestCase(unittest.TestCase):

    def test_demo(self):
        url = 'http://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0'
        data = {"limit": '1'}
        data = json.dumps(data)
        headers = {
            "Content-Type": "application/json"
        }

        res = requests.get(url=url, params=data, headers= headers)  # send the request there
        logger.info(res.json())
        # print("The first API", res.text, res.status_code)

    # The second one here

    def test_login(self):
        url = 'http://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0'
        data = {
                "product": "astro",
                "init": "2020092612",
                "dataseries": [{
                    "timepoint": 3,
                    "hollyshit": 9
                }]
            }
        data = json.dumps(data)
        headers = {
            "Content-Type": "application/json"
        }

        res = requests.post(url=url, data=data, headers=headers)  # send the request there
        # print('The second API', res.text, res.status_code)
        logger.info(res.json())

    # @file_date('test.yaml')
    # def test_1(self, **user):



if __name__ == '__main__':
    unittest.main()
    # pytest.main(['-s', 'test.py', '--html=ruiren.html'])