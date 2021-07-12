import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# could add options if needed
#options = webdriver.ChromeOptions()
#options.add_argument('--incognito')

driver = webdriver.Chrome()
driver.get('http://www.sdsclub.com')
time.sleep(2)

# click learning paths
button_one = driver.find_element_by_xpath('//*[@id="menu-item-456"]/a').click()
time.sleep(3)

button_two = driver.find_element_by_xpath('//*[@id="category-career"]/div/div[2]/div[4]/div/figure/a').click()
time.sleep(10) # need longer timeout to allow popup too appear

popup_close = driver.find_element_by_class_name('close-icon').click()

# start scraping
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

# get data
scrape_one = [i.text for i in soup.findAll('span', {'class': 'desc'})] 
scrape_two = [i.text for i in soup.findAll('div', {'class': 'single-path-article-content'})] 
scrape_three = [i.text for i in soup.findAll('p', {'p': 'name'})] 

# assign data to dataframe
df1 = pd.DataFrame(scrape_one)
df2 = pd.DataFrame(scrape_two)
df3 = pd.DataFrame(scrape_three)

print(df1, df2, df3)

time.sleep(10) # in seconds
driver.quit() 

df1_clean = df1.replace('\n', '',)
df2_clean = df2.replace('\n', '',)
df3_clean = df3.replace('\n', '',)
clean_stack = pd.concat([df1_clean, df2_clean, df3_clean], axis=1)

print(clean_stack)



