from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddUserPage:
    def __init__(self, driver):
        self.user_roleLocator = 'oxd-select-text--active'
        self.select_UR_Locator = '//span[text()="ESS"]'
        self.statusLocator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[' \
                             '2]/div/div/div[1] '
        self.select_St_Locator = '//span[text()="Enabled"]'
        self.employee_name_Locator = '//input[contains(@placeholder,"Type for hints...")]'
        self.select_EN_Locator = '//div[@class="oxd-autocomplete-dropdown --positon-bottom"]'
        self.usernameLocator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input'
        self.passwordLocator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input'
        self.confirm_P_Locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input'
        self.saveLocator = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]"

        self.employeeName = 'Odis Adalw'
        self.user_name = "loneew"
        self.passw = "France123!"
        self.driver = driver

    def user_role(self):
        self.driver.find_element(By.CLASS_NAME, self.user_roleLocator).click()
        time.sleep(2)
        WebDriverWait(self.driver, 1.5).until(EC.presence_of_element_located((By.XPATH, self.select_UR_Locator))).click()
        time.sleep(2)

    def status(self):
        self.driver.find_element(By.XPATH, self.statusLocator).click()
        time.sleep(2)
        WebDriverWait(self.driver, 1.5).until(EC.presence_of_element_located((By.XPATH, self.select_St_Locator))).click()
        time.sleep(2)

    def employee_name(self):
        self.driver.find_element(By.XPATH, self.employee_name_Locator).send_keys(self.employeeName)
        time.sleep(2)
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, self.select_EN_Locator))).click()
        time.sleep(2)

    def username(self):
        self.driver.find_element(By.XPATH, self.usernameLocator).send_keys(self.user_name)
        time.sleep(1)

    def password(self):
        self.driver.find_element(By.XPATH, self.passwordLocator).send_keys(self.passw)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.confirm_P_Locator).send_keys(self.passw)
        time.sleep(1)

    def add_user(self):
        self.user_role()
        self.status()
        self.employee_name()
        self.username()
        self.password()
        self.driver.find_element(By.XPATH, self.saveLocator).click()
        time.sleep(8)
        return self

