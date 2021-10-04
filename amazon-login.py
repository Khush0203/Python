#simple web automation program that logins to your amazon account and searches what you want
#save login details in item python file 
#i have not included that file for privacy reasons
#create one and store encrypted passwords 
#encrypting with a unique algorithm and decrypting before using it will make your automation smooth

from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
import time
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
import item
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

searchitem = input("What do you want to search in amazon:  ")
print()
print()

web = webdriver.Safari()
web.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")


email =  web.find_element_by_xpath('//*[@id="ap_email"]')
email.send_keys(item.username)

email_submit = web.find_element_by_xpath('//*[@id="continue"]')
email_submit.click()


time.sleep(3)


pasword = web.find_element_by_xpath('//*[@id="ap_password"]')
pasword.send_keys(item.decrypted)

password_submit = web.find_element_by_xpath('//*[@id="signInSubmit"]')
password_submit.click()

time.sleep(8)
search = web.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys(searchitem)

time.sleep(5)
button = web.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
button.click()

#A KHUSH MUNSHI PRODUCTION

