from WebUI.basePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchPage(BasePage):

    # inheritance here from parent
    def __init__(self, driver, input_id, click_id):
        super().__init__(driver)
        self.input_id = (By.ID, input_id)
        # click
        self.click_id = (By.ID, click_id)

    # Input the text words
    def input_text(self, input_text):
        self.locator(self.input_id).send_keys(input_text)

    # Click the elements
    def click_element(self):
        self.locator(self.click_id).click()

    # compile together here
    def check(self, url, input_text):
        self.visit(url)
        self.input_text(input_text)
        self.click_element()
        self.quit_browser()

if __name__ == "__main__":
    url = "http://www.baidu.com"
    driver = webdriver
    sp = SearchPage(driver, 'kw', 'su')
    sp.check(url, 'pure storage')

