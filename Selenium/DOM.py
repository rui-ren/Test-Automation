
# JSE

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("....").send_keys("hello")

print(driver.find_element_by_name("name").text)

driver.find_element_by_name("name").get_attribute()

# here we can get the attribute here!

# we can use this to find this !

# JS getElemnetsByName("name")[0].value
driver.execute_script("return document.getElementsByName("name")[0].value")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight")



