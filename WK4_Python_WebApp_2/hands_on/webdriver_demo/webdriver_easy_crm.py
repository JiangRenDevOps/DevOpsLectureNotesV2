from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://localhost:8090/login")


username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.clear()
username.send_keys("test@gmail.com")
password.clear()
password.send_keys("shh")
driver.find_element_by_xpath('//input[@type="submit"]').click()
