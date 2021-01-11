
# Hover pattern here

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https:\\www.google.com")
action = ActionChains(driver)
# check the hover method here
memu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()

childMenu = driver.find_element_by_link_text("Top")
action.move_to_element(childMenu).click().perform()

# check the double check!
action.get("w....w")
action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert()
assert alert.text == "Are you kidding me "
alert.accept()

action.context_click(driver.find_element_by_id("double-click")).perform()

driver.close()
