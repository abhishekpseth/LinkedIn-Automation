import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:/CSE/chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.


driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')


# locate email form by_class_name
username = driver.find_element_by_id('username')


# send_keys() to simulate key strokes
username.send_keys('abhishekpseth@gmail.com')
# locate password form by_class_name
password = driver.find_element_by_id('password')

# send_keys() to simulate key strokes
password.send_keys('Iamkalam#2001')

log_in_button = driver.find_element_by_class_name('btn__primary--large')
# .click() to mimic button click
log_in_button.click()


driver.get('https://www.google.com/')

# locate search form by_name
search_query = driver.find_element_by_name('q')

# send_keys() to simulate the search text key strokes
search_query.send_keys('site:linkedin.com/in/ AND "founder"')

search_query.send_keys(Keys.RETURN)

# locate URL by_class_name
linkedin_urls = driver.find_elements_by_class_name('iUh30')

# variable linkedin_url is equal to the list comprehension 
linkedin_urls = [url.text for url in linkedin_urls]

print(linkedin_urls[0])

