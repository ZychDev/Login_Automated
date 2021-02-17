from selenium import webdriver
from time import sleep

mail = '...'
passw = '.....'
#path to chromedriver
web_driver = webdriver.Chrome('/usr/bin/chromedriver')

#open github
web_driver.get("https://stackoverflow.com")
#Sign in
for element in web_driver.find_elements_by_tag_name("a"):
    if "/login" in element.get_attribute('href'):
        element.click()
        

        sleep(1)

        username = web_driver.find_element_by_id('email')
        username.send_keys("name")

        password_field = web_driver.find_element_by_id('password')
        password_field.send_keys("password")

        web_driver.find_element_by_xpath('//*[@id="submit-button"]').click()    