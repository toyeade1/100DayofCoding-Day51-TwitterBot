from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import time

# Fixed Variables
PROMISED_DOWN = 200
PROMISED_UP = 30
PATH = os.environ['path']
TWITTER_USER = os.environ['username']
TWITTER_PASS = os.environ['password']


class InternetSpeedTwitterBot:

    def __init__(self):
        opt = Options()
        opt.add_experimental_option('detach', True)
        ser = Service(PATH)
        self.driver = webdriver.Chrome(service=ser, options=opt)
        self.down = ''
        self.up = ''
        self.urls = ['https://www.speedtest.net/', 'https://twitter.com']

    def get_internet_speed(self, url):
        self.driver.get(url)
        time.sleep(4)
        self.driver.find_element('xpath', '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(45)
        self.down = self.driver.find_element('xpath', '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element('xpath', '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f'Download Speed: {self.down} Mbps\nUpload Speed: {self.up} Mbps')

    def tweet_at_provider(self, url):
        self.driver.get(url)
        time.sleep(3)
        self.driver.find_element('xpath', '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span').click()
        time.sleep(2)
        name = self.driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        name.send_keys(TWITTER_USER)
        time.sleep(2)
        self.driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span').click()
        time.sleep(2)
        password = self.driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASS)
        time.sleep(2)
        self.driver.find_element('xpath', '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        time.sleep(7)
        self.driver.find_element('xpath', '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        time.sleep(2)
        draft = self.driver.find_element('class name', 'public-DraftStyleDefault-block')
        draft.send_keys(f'Hey Xfinity, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up?')
        time.sleep(5)
        self.driver.quit()


internet = InternetSpeedTwitterBot()
internet.get_internet_speed('https://www.speedtest.net/')
download_speed = float(internet.down)
upload_speed = float(internet.up)

if download_speed < PROMISED_DOWN or upload_speed < PROMISED_UP:
    internet.tweet_at_provider('https://twitter.com')
