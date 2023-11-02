''' App to check internet speed and tweet your speed to ISP if you want '''
from time import sleep
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)

load_dotenv()

TWITTER_EMAIL = os.getenv('TWITTER_EMAIL') 
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
TWITTER_USER_NAME = os.getenv('TWITTER_USER_NAME')


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.down = 0
        self.up = 0

    def get_internet_Speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(4)
        accept_cookie = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_cookie.click()
        sleep(5)
        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go_button.click()
        sleep(50)
        self.down = float(self.driver.find_element(By.CLASS_NAME, value="download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, value="upload-speed").text)
        print(self.down, self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        sleep(6)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a/div')
        log_in.click()
        sleep(5)
        email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(TWITTER_EMAIL)        
        email_input.send_keys(Keys.ENTER)
        sleep(5)
        try:
            pass_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            username.send_keys(TWITTER_USER_NAME)  #Your Username here in case Twitter asks for username before asking password
            username.send_keys(Keys.ENTER)
            sleep(5)
            pass_input = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)
        sleep(5)

        # if you don't actually want to send the tweet comment out section below

        # input = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        # input.send_keys(f"My Current Internet Speed is {self.down} Download and {self.up} Upload")
        # sleep(3)
        # tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        # tweet.click()
        # time.sleep(5)
        # print("Tweet Done")
        # self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_Speed()
bot.tweet_at_provider()
