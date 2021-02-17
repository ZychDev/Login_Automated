from selenium import webdriver
from time import sleep

mail = '...'
passw = '.....'
#path to chromedriver
web_driver = webdriver.Chrome('/usr/bin/chromedriver')

#open github
web_driver.get("https://github.com/")

#Sign in
for element in web_driver.find_elements_by_tag_name("a"):
    if "/login" in element.get_attribute('href'):
        element.click()

time.sleep(1)

user_field = web_driver.find_element_by_id('login_field')
user_field.send_keys(mail)
time.sleep(1)

password_field = web_driver.find_element_by_id('password')
password_field.send_keys(passw)
time.sleep(1)

driver.find_element_by_xpath('//*[@class="btn btn-primary btn-block"]').click()