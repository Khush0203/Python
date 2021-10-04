#simple python program that logins into your commonapp account and goes to common app section
#create a new python file to store username and password
#here it is commonappdatabase 
#i have not uploaded it for privacy reasons 
#create one and store encrypted passwords 
#encrypting with a unique algorithm and decrypting before using it will make your automation smooth


from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
import time
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
import commonappdatabase 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


web = webdriver.Safari()
web.get("https://apply.commonapp.org/login")

username = web.find_element_by_xpath('//*[@id="loginEmailControl"]')
username.send_keys(commonappdatabase.username)#username

password = web.find_element_by_xpath('//*[@id="loginPasswordControl"]')
password.send_keys(commonappdatabase.decrypted)#decrypted password

time.sleep(8)

submit = web.find_element_by_xpath('//*[@id="loginSubmit"]')
submit.click()

time.sleep(10)
try:
    element = WebDriverWait(web , 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="top-common"]'))
    )
    element.click()
except:
    print("error")

#A KHUSH MUNSHI PRODUCTION
