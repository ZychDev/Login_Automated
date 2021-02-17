from selenium import webdriver


#path to chromedriver
web_driver = webdriver.Chrome('/usr/bin/chromedriver')

#open github
web_driver.get("https://github.com/")

#Sign in
for element in web_driver.find_elements_by_tag_name("a"):
    if "/login" in element.get_attribute('href'):
        element.click()

