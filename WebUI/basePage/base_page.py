from selenium import webdriver
# This is the base class

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver.Chrome()
    # locator here
    def locator(self, locator):
        return self.driver.find_element(*locator)
    # quit
    def quit_browser(self):
        self.driver.quit()

    # visit the URL
    def visit(self, url):
        self.driver.get(url)
