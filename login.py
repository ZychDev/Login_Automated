from selenium import webdriver


#path to chromedriver
web_driver = webdriver.Chrome('/usr/bin/chromedriver')

#open github
web_driver.get("https://github.com/")