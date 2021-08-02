import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
USERNAME = ''
PASSWORD = ''
URL_LOGIN = 'https://www.udemy.com/join/login-popup/'
#URL = 'https://www.udemy.com/home/my-courses/learning/'
URL_COURSES = 'https://www.udemy.com/home/my-courses/learning/?p='
BEGIN_PAGE_NUMBER = 1
END_PAGE_NUMBER = 1 #354


def site_login(url):

    driver.get(url)
    time.sleep(5)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    # xpath = //*[@id="onetrust-accept-btn-handler"]
    driver.find_element_by_name('email').send_keys(USERNAME)
    # xpath = //*[@id="email--1"]
    driver.find_element_by_name('password').send_keys(PASSWORD)
    # xpath = //*[@id="id_password"]
    driver.find_element_by_xpath('//*[@id="submit-id-submit"]').click()

def get_page_course_details(url, page_number):

    url = 'https://www.amazon.com/Best-Sellers/zgbs'
    # common user agent list from https://www.networkinghowtos.com/howto/common-user-agent-list/
    headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    print(r.status_code)
    product_total_review = [i.text for i in soup.findAll('a', {'class': 'a-size-small a-link-normal'})]
    df = pd.DataFrame(product_total_review)
    print(df)
    # add timer
    time.sleep(60)

    #https://www.udemy.com/home/my-courses/learning/?p=1
    driver.get(url + page_number)
    time.sleep(5)
    course_numbers = [i.text for i in soup.findAll('href', {'class': 'card--learning__details'})]
    course_names = [i.text for i in soup.findAll('strong', {'class': 'details__name'})]
    return course_numbers, course_names

# driver = webdriver.Chrome()
# site_login(URL_LOGIN)

for num in range(BEGIN_PAGE_NUMBER, END_PAGE_NUMBER):
    courses = pd.DataFrame(get_page_course_details(URL_COURSES, num))

print(courses)

time.sleep(20) # in seconds
driver.quit()