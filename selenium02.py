import time
from selenium import webdriver

driver = webdriver.Chrome()

def site_login():
    driver.get('http://www.superdatascience.com/login')
    driver.find_element_by_id('cookiescript_reject').click()
    driver.find_element_by_name('email').send_keys('myusername') # for some reason these by_name css selectors fail??
    driver.find_element_by_name('password').send_keys('mypassword')
    driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div[1]/div/div/form/button').click()



site_login()
time.sleep(20) # in seconds
driver.quit()

