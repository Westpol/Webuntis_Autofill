from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://nessa.webuntis.com/WebUntis/?school=ges-scharnhorst#/basic/login")
time.sleep(2)
uname = driver.find_element(By.CLASS_NAME, "un-input-group__input")
pw = driver.find_element(By.CLASS_NAME, "un-input-group__input")
time.sleep(5)
driver.close()
