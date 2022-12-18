from selenium.webdriver.common.by import By
import time


class HomePage:
    def __init__(self, driver):
        self.admin_buttonLocator = 'oxd-main-menu-item'
        self.managementLocator = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
        self.usersLocator = 'oxd-topbar-body-nav-tab-link'
        self.addLocator = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
        self.driver = driver

    def admin_management(self):
        self.driver.find_element(By.CLASS_NAME, self.admin_buttonLocator).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.managementLocator).click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, self.usersLocator).click()
        time.sleep(1.5)
        self.driver.find_element(By.XPATH, self.addLocator).click()
        time.sleep(1.5)
        return self
