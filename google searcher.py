from selenium import webdriver

s = input("What do you want to search in google?")




web = webdriver.Chrome()

web.get("https://www.google.com/?gws_rd=ssl")

searchbox = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys(s)

searchbutton = web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
searchbutton.click()
