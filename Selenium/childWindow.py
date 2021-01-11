
# child window page

# How to handle multiple window

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()
childwindow = driver.window_handles[1]

# get the child window here!
driver.switch_to.window(childwindow)
driver.find_element_by_ta_name("h3").text

driver.close()

