#coding=utf-8
from selenium import webdriver
import os

def openUrl(driver,url):
    driver.get(url)

def insert_img(driver,file_name):
    base_dir = str(os.path.dirname(os.path.dirname(__file__))).replace("\\",'/')
    base = base_dir.split('/test_case')[0]
    file_path = base + "/report/image/" + file_name
    print file_path
    driver.get_screenshot_as_file(file_path)

if __name__=='__main__':
    driver = webdriver.Chrome()
    openUrl(driver,'http://127.0.0.1/zentao/')
    insert_img(driver,"zentao_login.jpg")
    driver.close()
    driver.quit()






