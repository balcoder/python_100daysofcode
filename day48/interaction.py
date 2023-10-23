''' Some simple examples of automating website actions using Selenium'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# keep chrome open after selenium finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


# Automating the cookie cliker game to score points over 5 mins
driver.get('https://orteil.dashnet.org/cookieclicker/')
consent_button = driver.find_element(By.CLASS_NAME, 'fc-cta-consent')
consent_button.click()
time.sleep(3)
lang_select = driver.find_element(By.CSS_SELECTOR, '#langSelect-EN')
lang_select.click()
time.sleep(5)

# get our selections
button = driver.find_element(By.ID, 'bigCookie')

OUTER_TIMEOUT = 300 # 5 mins
outer_start_time = time.time()

# start automation for 5 mins
while time.time() < outer_start_time + OUTER_TIMEOUT:
    TIMEOUT = 20   # [seconds]
    start_time = time.time()
    # every timeout click the highest price upgrade item
    while time.time() < start_time + TIMEOUT:
        button.click()
    cookies = driver.find_element(By.ID, 'cookies').text
    # print(cookies.split()[0])
    store_items = driver.find_elements(By.CSS_SELECTOR, '#products .product.unlocked.enabled ')
    # if we have enough cookies to buy an upgrade
    if len(store_items) > 0:
        most_expensive = store_items[len(store_items) -1]
        most_expensive.click()
cookies_per_second = driver.find_element(By.ID, 'cookiesPerSecond').text
print(cookies_per_second)

#---------------------------------------------------------------------#
# Wikipedia
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# stats = driver.find_element(By.CSS_SELECTOR, '#articlecount > a')
# view_history = driver.find_element(By.LINK_TEXT, 'View history')
# view_history.click()
# print(stats.text)

# search = driver.find_element(By.NAME, 'search')
# search.send_keys('Putin')
# search.send_keys(Keys.ENTER)
#---------------------------------------------------------------------#

#---------------------------------------------------------------------#
#App Brewery lab page testing site
# driver.get('http://secure-retreat-92358.herokuapp.com/')
# first_name = driver.find_element(By.NAME, 'fName')
# first_name.send_keys('Richard')
# last_name = driver.find_element(By.NAME, 'lName')
# last_name.send_keys('Daukins')
# email = driver.find_element(By.NAME, 'email')
# email.send_keys('Richard@gmail.com')
# submit = driver.find_element(By.CSS_SELECTOR, '.btn[type=submit]')
# submit.click()
#---------------------------------------------------------------------#

#---------------------------------------------------------------------#
