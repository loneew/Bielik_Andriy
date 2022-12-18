from selenium.webdriver.common.by import By
import time


class LoginPage:
    def __init__(self, driver):
        self.input_usernameLocator = "username"
        self.input_passwordLocator = "password"
        self.usernameLocator = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[1]'
        self.passwordLocator = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[2]'
        self.loginLocator = 'orangehrm-login-button'
        self.driver = driver

    def username(self):
        usr = self.driver.find_element(By.XPATH, self.usernameLocator)
        usr = usr.text[11:]
        return usr

    def password(self):
        pas = self.driver.find_element(By.XPATH, self.passwordLocator)
        pas = pas.text[11:]
        return pas

    def enter_username(self):
        usr = self.username()
        self.driver.find_element(By.NAME, self.input_usernameLocator).send_keys(usr)
        return self

    def enter_password(self):
        password = self.password()
        self.driver.find_element(By.NAME, self.input_passwordLocator).send_keys(password)
        return self

    def login(self):
        time.sleep(1)
        self.enter_username()
        time.sleep(1.5)
        self.enter_password()
        self.driver.find_element(By.CLASS_NAME, self.loginLocator).click()
        return self
