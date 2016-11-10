#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from zentao.test_case.models.browser_driver import openBrowser
from zentao.test_case.models.public_function import openUrl



class Login:
    def __init__(self):
        self.url = 'http://127.0.0.1/zentao/'
        self.zentao_login_user_loc = (By.NAME, "account")
        self.zentao_login_password_loc = (By.NAME, "password")
        self.zentao_login_button_loc = (By.ID, 'submit')

    def login_username(self,username):
        self.driver.find_element(self.zentao_login_user_loc).send_keys(username)

    def login_password(self,password):
        self.driver.find_element(self.zentao_login_password_loc).send_keys(password)

    def login_button(self):
        self.driver.find_element(self.zentao_login_button_loc).click()

    def login(self,username='admin',password='123456'):
        driver = openBrowser()
        openUrl(driver,self.url)
        driver.find_element(*self.zentao_login_user_loc).send_keys(username)
        driver.find_element(*self.zentao_login_password_loc).send_keys(password)
        driver.find_element(*self.zentao_login_button_loc).click()
        # self.login_username(username)
        # self.login_password(password)
        # self.login_button()
        sleep(1)
        driver.quit()

if __name__=="__main__":
    l = Login()
    l.login()






