'''App to find all the apartments listed on Zillow for the San Francisco area
 with one or more bedrooms under $3000 a month '''

from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)

FORM_URL = "https://forms.gle/mUFJaoeNZdWpybWJ9"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.97258441462942%2C%22south%22%3A37.577471590568905%2C%22east%22%3A-122.25136844042969%2C%22west%22%3A-122.61529055957031%7D%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'}

def scrape_zillow(url):
    ''' Scrape Zillow for apartments under $3000 a month  with one + bedroom'''
    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status() # raise HTTPError, if the response was an http error
    except requests.exceptions.HTTPError as e:
        raise SystemExit(e) from e
    except requests.exceptions.RequestException as e:
        raise SystemExit(e) from e
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        soup_addr = soup.select('div.property-card-data address[data-test="property-card-addr"]')
        soup_links = soup.select('div.property-card-data > a')
        soup_price = soup.select('div.property-card-data span')
        links = [link['href'] for link in soup_links]
        # add missing base url to some links
        for idx, link in enumerate(links):
            if link.startswith('/'):
                links[idx] = "https://www.zillow.com" + link

        prices = [price.getText() for price in soup_price]
        addresses =[addr.get_text() for addr in soup_addr]

        return [addresses, prices, links ]

def fill_form(url, info):
    '''fills in a google form from a list of addresses, prices and links '''
    for idx in range(len(info[0])):
        driver.get(url)
        sleep(1)
        property_address = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i1"]')
        property_price = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i5"]')
        property_link = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="i9"]')
        submit_button = driver.find_element(By.CSS_SELECTOR, 'span.NPEfkd.RveJvd.snByac')

        property_address.send_keys(info[0][idx])
        property_price.send_keys(info[1][idx])
        property_link.send_keys(info[2][idx])
        sleep(1)
        submit_button.click()
        sleep(1)

list_of_apartments = scrape_zillow(ZILLOW_URL)
fill_form(FORM_URL, list_of_apartments)
