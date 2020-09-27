
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get rid of the blank
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_argument('headless')
# generate a chrome driver
driver = webdriver.Chrome(options=option)
# use the get method to access the url

driver.get("http://www.baidu.com")
print(driver.title)
# input the pure storage
driver.find_element_by_id('kw').send_keys("pure storage")
# click baidu button
driver.find_element_by_id('su').click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, '6')))
# click pure storage
driver.find_element_by_xpath('//*[@id="6"]/h3/a').click()
driver.quit()
