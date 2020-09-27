import requests
from ddt import ddt,data, file_data, unpack

"""
Http requests here! 
We have the main 5 http method here
"""

class HttpRequest(object):
    @staticmethod
    def http_request(url, data, method, expected=None, cookie=None, verify=False):
        if method.lower() == 'get':
            res = requests.get(url, data, cookies=cookie, verify=False)
        elif method.lower() == 'post':
            res = requests.post(url, data, cookies=cookie, verify=False)
        elif method.lower() == 'delete':
            res = requests.delete(url, data, cookies=cookie, verify=False)
        elif method.lower() == 'put':
            res = requests.put(url, data, cookies=cookie, verify=False)
        return res
