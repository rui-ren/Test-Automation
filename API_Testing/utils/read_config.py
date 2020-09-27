"""
read the file in config  -- yaml file here
"""

import configparser
import os
from API_Testing.utils.project_path import config_path

class WriteConfig(object):
    config = configparser.ConfigParser()
    config['MODE'] = {
        'login_data': 'all',
        'recharge_date': [1, 3]
    }
    with open('../config/http.config', 'w') as configfile:
        config.write(configfile)

class ReadConfig(object):

    @staticmethod
    def get_config(config_path, section, option):
        config = configparser.ConfigParser()
        config.read(config_path, encoding='utf-8')
        return config[section][option]


if __name__ == "__main__":
    if not os.walk('../config'):
        WriteConfig()
    cf = ReadConfig.get_config(config_path, 'MODE', 'login_data')
    print(cf)

