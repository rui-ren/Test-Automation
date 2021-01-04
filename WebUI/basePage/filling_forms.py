from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# Filling in forms here
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
elem = driver.find_element_by_id("kw")
elem.send_keys("pure storage")
driver.find_element_by_id('su').click()
sleep(10)

select = Select(driver.find_element_by_xpath('//*[@id="s_tab"]/div/a[1]'))
select.select_by_value("视频")
driver.quit()
# select.select_by_index("index")
# select.select_by_visible_text("text")
# select.select_by_value("value")
#
# # Drag and drop
# element = driver.find_element_by_name("source")
# target = driver.find_element_by_name("target")
#
# from selenium.webdriver import ActionChains
# action_chains = ActionChains(driver)
# action_chains.drag_and_drop(element, target).perform()

# driver.switch_to_window("windowName")

