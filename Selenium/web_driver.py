
from selenium import webdriver

# browser exposes an executable file
# through selenum , we can invoke actual brower
driver = webdriver.Chrome()
"""
The same code work for all the browsers --> might not for IE
driver = webdriver.Firefox()

"""

driver.maximize_window()
driver.get("https://www.baidu.com/") # get method to click on browser

print(driver.title)

print(driver.current_url)

driver.close()

driver.get("https://google.com/")

driver.minimize_window()

driver.back()

driver.refresh()

# close the job task manager
driver.quit()
