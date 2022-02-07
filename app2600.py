import selenium
import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import os

username = input("Please enter your ninernet username: ")                                          # Please enter your username here
password = getpass.getpass('Please enter your password:')                                            # Please enter your password here

duoPin = input("Please enter your duo push code: ")

driver = webdriver.Firefox(executable_path='C:/Users/Michael/Documents/Personal/PY_code/Selenium_Drivers/geckodriver.exe') #replace path with your own geckodriver.exe Path
driver.get("https://my.charlotte.edu")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="shib_login_url"]/a').click()

driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)

driver.find_element_by_xpath('//*[@id="shibboleth-login-button"]').click() #clicks login

time.sleep(2.5)
iframe = driver.find_element_by_xpath('//*[@id="duo_iframe"]')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath('//*[@id="passcode"]').click()
driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[2]/div/input').send_keys(duoPin)
driver.find_element_by_xpath('//*[@id="passcode"]').click()
driver.switch_to.default_content()

time.sleep(4)
WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,'//*[@id="views-bootstrap-grid-1"]/div/div[3]/div[2]/span/a')))#wait for page load
driver.find_element_by_xpath('//*[@id="views-bootstrap-grid-1"]/div/div[3]/div[2]/span/a').click()

time.sleep(.5)
driver.switch_to.window(driver.window_handles[1])
# Gets you into banner self service
# Changes to that active tab

time.sleep(1)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/span/map/p/table/tbody/tr[1]/td/table/tbody/tr/td[7]/a').click()
# Clicks employee tab

driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td[2]/a').click()
# clicks timesheet

driver.find_element_by_xpath('//*[@id="djobs_6_id"]').click()
# clicks position

driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr/td/input').click()

##################################################### WEEK 1 #################################################################   
############################                          Sunday                             #####################################
# driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[7]/p/a').click()
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys(" ")              #Enter start time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("in")
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys(" ")              #Enter end time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("out")
# driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()                    

############################                          Monday                             #####################################
# driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[8]/p/a').click()
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys("1200")              #Enter start time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("in")
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys("0330")              #Enter end time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("out")
# driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Tuesday                             #####################################
driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[9]/p/a').click()
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys("0400")              #Enter start time
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("Class")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys("0500")               #Enter end time
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("Class")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[3]/input').send_keys("0700")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[4]/select').send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[6]/textarea').send_keys("Grading")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[9]/input').send_keys("0830")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[10]/select').send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[12]/textarea').send_keys("Grading")
driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Wednesday                             #####################################
#driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[10]/p/a').click()
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys("0200")              #Enter start time
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("Office Hours")
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys("0500")               #Enter end time
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("Office Hours")
#driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Thursday                             #####################################
driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[11]/p/a').click()
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys("0400")              #Enter start time
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("Class")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys("0500")               #Enter end time
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("Class")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[3]/input').send_keys("0700")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[4]/select').send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[6]/textarea').send_keys("Grading")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[9]/input').send_keys("0830")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[10]/select').send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[12]/textarea').send_keys("Grading")
driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Friday                             #####################################
# driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[12]/p/a').click()
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys("0100")              #Enter start time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("in")
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys("0500")               #Enter end time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("out")
# driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Saturday                             #####################################
# driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[13]/p/a').click()
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys(" ")              #Enter start time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("in")
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys(" ")              #Enter end time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("out")
# driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/p/table/tbody/tr/td[6]/input').click()

#################################################### WEEK 2 ##################################################################
############################                          Sunday                             #####################################
# driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[7]/p/a').click()
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys(" ")              #Enter start time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("in")
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys(" ")              #Enter end time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("out")
# driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Monday                             #####################################
#driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[8]/p/a').click()
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys("1130")              #Enter start time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("in")
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys("0330")               #Enter end time
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("out")
#driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Tuesday                             #####################################
driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[9]/p/a').click()
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys("0400")              #Enter start time
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("Class")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys("0500")               #Enter end time
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("Class")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[3]/input').send_keys("0700")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[4]/select').send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[6]/textarea').send_keys("Grading")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[9]/input').send_keys("0830")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[10]/select').send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[12]/textarea').send_keys("Grading")
driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Wednesday                             #####################################
#driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[10]/p/a').click()
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys("0200")              #Enter start time
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("Office Hours")
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys("0500")               #Enter end time
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
#driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("Office Hours")
#driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Thursday                             #####################################
driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[11]/p/a').click()
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys("0400")              #Enter start time
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("Class")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys("0500")               #Enter end time
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("Class")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[3]/input').send_keys("0700")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[4]/select').send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[6]/textarea').send_keys("Grading")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[9]/input').send_keys("0830")
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[10]/select').send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[4]/td[12]/textarea').send_keys("Grading")
driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Friday                             #####################################
# driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[12]/p/a').click()
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys("0100")               #Enter start time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN)  #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("in")
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys("0500")               #Enter end time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("out")
# driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()

############################                          Saturday                             #####################################
# driver.find_element_by_xpath('/html/body/div[3]/table[1]/tbody/tr[5]/td/form/table/tbody/tr[2]/td[13]/p/a').click()
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[3]/input').send_keys(" ")              #Enter start time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[4]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[6]/textarea').send_keys("in")
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[9]/input').send_keys(" ")              #Enter end time
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[10]/select').send_keys(Keys.ARROW_DOWN) #DOWN for PM or comment out for AM
# driver.find_element_by_xpath('/html/body/div[3]/form/table[2]/tbody/tr[3]/td[12]/textarea').send_keys("out")
# driver.find_element_by_xpath('/html/body/div[3]/form/p/table/tbody/tr[1]/td/input[1]').click()