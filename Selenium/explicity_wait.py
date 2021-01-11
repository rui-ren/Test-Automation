

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# Global wait
# - 1.5 second to reach next page-execution will resume in 1.5 second
# - if object do not show up at all, then max time your test waits for 5 second
driver.implicitly_wait(5)

driver.get("https://www.google.com/")

# explicity wait -> target specific element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 5)

wait.until(EC.presence_of_element_located(By.CLASS_NAME, 'promoCode'))

wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, "apan.promoInf"))


# Rule of Thumb 
# 1. If you know, where you application is slow, you can use implicity wait
# 2. If you want to test specific area, you can use explicity wait support. wait 


