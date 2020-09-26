
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# generate a chromedriver
driver = webdriver.Chrome()
# use the get method to access the url
driver.get("http://www.baidu.com")
# input the pure storage
driver.find_element_by_id('kw').send_keys("pure storage")
# click baidu button
driver.find_element_by_id('su').click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, '6')))
# click pure storage
driver.find_element_by_xpath('//*[@id="6"]/h3/a').click()

