from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')
# driver.implicitly_wait(40)
# price_pounds = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_pence = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price {price_pounds.text}.{price_pence.text}")

events = driver.find_elements(By.CSS_SELECTOR, '.event-widget.last li>a')
time_of_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget.last time')
# for event in events:
#     print(event.text)
event_names = [event.text for event in events]
event_times = [time.text for time in time_of_events]

event_dict = dict(zip(event_times, event_names))
print(event_dict)
# driver.close()