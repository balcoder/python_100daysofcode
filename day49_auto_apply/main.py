''' App to save fullstack job from linkedin to a txt file'''
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


# keep chrome open after selenium finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

# Get the full url by doing a search on Linkedin for a specific job title and copying url
# For other types of jobs just change the keyword below like 'backend%20end%20developer'
base_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3743477069&f_WT=2%2C1%2C3&'
# URL search parameters
geo_location = 'geoId=103667222&'
job_keywords = '&keywords=full%20stack%20developer'
location = '&location=County%20Cork%2C%20Ireland'
end_url = '&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true' 

# login to linked in
driver.get(f'{base_url}{geo_location}{job_keywords}{location}{end_url}')
consent_btn = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-global-alert-action')
time.sleep(2)
consent_btn.click()
time.sleep(2)

# get list of available jobs
jobs_list = driver.find_elements(By.CSS_SELECTOR, 'ul.jobs-search__results-list>li>div>a')

# Dictionary comprehension Syntax:{key: value for (key, value) in iterable if condition}
job_dict = {url.text: url.get_attribute('href') for url in jobs_list}
print(job_dict)

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
with open(f'{dir_path}\jobs.txt', 'w', encoding='utf-8') as f:
    for key, value in job_dict.items():
        f.write(key +'\n')
        f.write(value + '\n')
