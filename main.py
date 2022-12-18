from selenium import webdriver
import time
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.AddUserPage import AddUserPage
from Pages.UserManagementPage import UserManagementPage


class Test:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.login = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.add_user_page = AddUserPage(self.driver)
        self.user_management_page = UserManagementPage(self.driver)

    def run_test(self):
        self.login.login()
        time.sleep(2)
        self.home_page.admin_management()
        self.add_user_page.add_user()
        self.user_management_page.delete_user()


def main():
    test1 = Test()
    test1.run_test()


if __name__ == "__main__":
    main()
