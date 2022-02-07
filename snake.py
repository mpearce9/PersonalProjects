import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Firefox(executable_path='C:/Users/micha/Documents/Personal/Selenium_Drivers/geckodriver.exe')#replace path with your own geckodriver.exe Path
driver.get("http://www.menet.umn.edu/~dockt036/snake.html")

driver.find_element_by_xpath('/html/body/div/div[4]/button').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="pPeeKb"]').send_keys(Keys.ARROW_RIGHT)
time.sleep(2.3)

driver.find_element_by_xpath('//*[@id="pPeeKb"]').send_keys(Keys.ARROW_DOWN)
time.sleep(2.3)

driver.find_element_by_xpath('//*[@id="pPeeKb"]').send_keys(Keys.ARROW_LEFT)
time.sleep(2.3)

driver.find_element_by_xpath('/html/body/div/div[4]/button').send_keys(Keys.ARROW_UP)
time.sleep(2.3)

driver.find_element_by_xpath('/html/body/div/div[4]/button').send_keys(Keys.ARROW_RIGHT, Keys.ARROW_DOWN)
time.sleep(2)

driver.find_element_by_xpath('/html/body/div/div[4]/button').send_keys(Keys.ARROW_RIGHT, Keys.ARROW_UP)
time.sleep(3)

driver.find_element_by_xpath('//*[@id="pPeeKb"]').send_keys(Keys.ARROW_RIGHT)
time.sleep(3)