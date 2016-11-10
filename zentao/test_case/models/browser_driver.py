#coding=utf-8
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#启动浏览器驱动
def openBrowser():
    # 启动Chrome浏览器
    webdriver_handle = webdriver.Chrome()
    webdriver_handle.maximize_window()
    # 启动firefox浏览器
    # binary=FirefoxBinary(r'D:\Firefox\firefox.exe')
    # webdriver_handle = webdriver.Firefox(firefox_binary=binary)
    # 启动Ie浏览器
    # webdriver_handle = webdriver.Ie()
    return webdriver_handle


if __name__ == "__main__":
    openBrowser()