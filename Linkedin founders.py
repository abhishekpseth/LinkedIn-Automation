import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Set up Chrome driver
driver = webdriver.Chrome('D:/CSE/chromedriver_win32/chromedriver.exe')


# Log in to LinkedIn
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
username = driver.find_element_by_id('username')
username.send_keys('')
password = driver.find_element_by_id('password')
password.send_keys('')
log_in_button = driver.find_element_by_class_name('btn__primary--large')
log_in_button.click()


# Search for founders on LinkedIn
driver.get('https://www.google.com/')
search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "founder"')
search_query.send_keys(Keys.RETURN)


# Extract LinkedIn URLs
linkedin_urls = []
n=5
while len(linkedin_urls) < n:
    linkedin_urls_elements = driver.find_elements_by_xpath('//cite[@class="iUh30"]')
    for url_element in linkedin_urls_elements:
        if len(linkedin_urls) < n:
            linkedin_urls.append(url_element.text)
        else:
            break
    if len(linkedin_urls) < n:
        next_page_link = driver.find_element_by_xpath('//a[@id="pnnext"]')
        next_page_link.click()
        time.sleep(2)
    else:
        break


# Save LinkedIn URLs to Excel sheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = 'LinkedIn URLs'
for row, url in enumerate(linkedin_urls, start=1):
    worksheet.cell(row=row, column=1, value=url)
workbook.save('founders_on_linkedin.xlsx')


# Quit Chrome driver
driver.quit()