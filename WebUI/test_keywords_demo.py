from selenium import webdriver
from time import sleep
class TestKeyWords(object):
    # import the browser
    __test__ = False

    def __init__(self, browser_type, url):
        self.driver = self.open_browser(browser_type)
        sleep(2)
        self.driver.get(url)

    def open_browser(self, browser_type):
        if browser_type == "Chrome":
            return webdriver.Chrome()
        elif browser_type == "Firefox":
            return webdriver.Firefox()
        else:
            print("type error")

    # get the element
    def locator(self, locator_type, value):

        if locator_type == "xpath":
            el = self.driver.find_element_by_xpath(value)
            return el
        elif locator_type == "id":
            el = self.driver.find_element_by_id(value)
            return el
        elif locator_type == "name":
            el = self.driver.find_element_by_name(value)
            return el

    # input
    def input_text(self, locator_type, value, text):
        # get element by id
        self.locator(locator_type, value).send_keys(text)

    # click element
    def click_element(self, locator_type, value):
        self.locator(locator_type, value).click()

    # close the browser
    def quit_browser(self):
        self.driver.quit()


if __name__ == "__main__":
    tk = TestKeyWords("Chrome", "http://www.jd.com")
    tk.input_text('id', 'kw', 'pure storage')
    tk.click_element('id', 'su', )
    tk.quit_browser()
