import os
"""
Generate the path file here!
"""

project_path = os.path.split(os.path.dirname(os.path.realpath("__file__")))[0]

# make the directory of the path
if not os.path.exists(project_path + r'\data'):
    os.mkdir(project_path + r'\data')
test_case_path = os.path.join(project_path, 'data', 'data_http.xlsx')

# report file path
if not os.path.exists(project_path + r'\report'):
    os.mkdir(project_path + r'\report')

# use the time to rename the report
report_path = os.path.join(project_path, 'report', 'report.html')

# get the file path
if not os.path.exists(project_path + r'\config'):
    os.mkdir(project_path + r'\config')

config_path = os.path.join(project_path, 'config', 'http.config')

