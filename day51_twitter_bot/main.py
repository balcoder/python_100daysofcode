''' Tweet your internet provider when your internet speed is below promised'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PROMISED_DOWN = 28
PROMISED_UP = 1.9
CHROME_DRIVER_PATH = ''
TWITTER_EMAIL = "des.barrett.sub@gamil.com"
TWITTER_PASSWORD = "xyz"



class InternetSpeedTwitterBot:
    def __init__(self, up, down):
        self.up = up
        self.down = down
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)



    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(3)
        self.consent_btn = self.driver.find_element(
            By.CSS_SELECTOR, 'button#onetrust-accept-btn-handler')
        self.consent_btn.click()
        time.sleep(4)
        self.go_btn = self.driver.find_element(
            By.CSS_SELECTOR, 'div.start-button a')
        self.go_btn.click()
        time.sleep(45)
        self.down_result = self.driver.find_element(By.CSS_SELECTOR,
                            '.result-container-data span.result-data-large.number.result-data-value.download-speed').text
        self.up_result = self.driver.find_element(
            By.CSS_SELECTOR, '.result-container-data span.result-data-large.number.result-data-value.upload-speed').text
        print(self.down_result)
        print(self.up_result)

    def tweet_result(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(4)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a/div')
        log_in.click()        
        time.sleep(5)
        email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(TWITTER_EMAIL)
        time.sleep(1)

internet_speed_twitter_bot = InternetSpeedTwitterBot(
    PROMISED_UP, PROMISED_DOWN)
# internet_speed_twitter_bot.get_internet_speed()
internet_speed_twitter_bot.tweet_result()
