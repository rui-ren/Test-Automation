from WebUI.basePage.base_page import BasePage
from selenium import webdriver
from ddt import ddt
from time import sleep
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    url = "https://github.com/login"
    login_name = (By.XPATH, '//*[@id="login_field"]')
    pwd = (By.XPATH, '//*[@id="password"]')
    click_button = (By.XPATH, '//*[@id="login"]/form/div[4]/input[9]')

    def input_username(self, user_name):
        self.locator(self.login_name).send_keys(user_name)

    def input_pwd(self, pwd):
        self.locator(self.pwd).send_keys(pwd)

    def login(self):
        self.locator(self.click_button).click()

    def check_page(self, user_name, pwd):
        self.visit(self.url)
        self.input_username(user_name)
        self.input_pwd(pwd)
        self.login()
        sleep(2)
        self.quit_browser()


if __name__ == "__main__":
    driver = webdriver
    username = '123'
    pwd = 332
    lp = LoginPage(driver)
    lp.check_page(username, pwd)

