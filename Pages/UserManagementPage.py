from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UserManagementPage:
    def __init__(self, driver):
        self.employee_name_Locator = '//input[contains(@placeholder,"Type for hints...")]'
        self.select_EN_Locator = '//div[@class="oxd-autocomplete-dropdown --positon-bottom"]'
        self.searchLocator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
        self.resetLocator = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]'
        self.username_record_Locator = '//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., ' \
                                       '"loneew")]//i[@class="oxd-icon bi-check oxd-checkbox-input-icon"] '
        self.delete_selected_Locator = '//button[contains(.,"Delete Selected")]'
        self.yes_Locator = '//button[contains(.,"Yes, Delete")]'
        self.employeeName = 'Odis Adalw'
        self.driver = driver

    def employee_name(self):
        self.driver.find_element(By.XPATH, self.employee_name_Locator).send_keys(self.employeeName)
        time.sleep(4)
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, self.select_EN_Locator))).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.searchLocator).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.resetLocator).click()
        time.sleep(5)

    def delete_user(self):
        self.employee_name()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.username_record_Locator).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.delete_selected_Locator).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.yes_Locator).click()
        time.sleep(4)
