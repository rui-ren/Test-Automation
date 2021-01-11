
# check the iframe

# iframe, frameset, frame

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_mce")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")
# Traverse back --> we need to the previous default content
driver.switch_to.default_content()


# switch to alert
# switch to windows
# switch to iframe
