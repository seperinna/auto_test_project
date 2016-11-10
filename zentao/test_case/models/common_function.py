#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait

#设置等待时间
def get_ele_times(driver, times, func):
    return WebDriverWait(driver, times).until(func)

def find_element(driver,*args):
    return driver.find_element(*args)


