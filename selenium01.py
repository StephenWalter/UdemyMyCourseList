import time
from selenium import webdriver

driver = webdriver.Chrome()

# initial test
#driver.get('http://www.google.com')
#time.sleep(5)

# new test site
driver.get('http://sdsclub.com')
# use simple xpath to click login button
driver.find_element_by_xpath('/html/body/header/div/div/div[2]/a').click()
# can also use find by id and others. Plus here we fill in the field
driver.find_element_by_id('username').send_keys('cheese' + Keys.RETURN)






time.sleep(5) # in seconds
driver.quit()

