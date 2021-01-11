from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# we mute the web page here!
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.get("www.baidu.com")

driver.title()


