from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
PROVIDER = "Comcast"
TWITTER_USERNAME = "matheusbailerdemmer@gmail.com"
TWITTER_PASSWORD = "XXXXXXXXXXXX"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def tweet_at_provider(self, up, down):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10)
        user_name = self.driver.find_element(By.XPATH,
                                             value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/'
                                                   'div[2]/div/div/div[2]/div[2]/div/div/div/div[5]'
                                                   '/label/div/div[2]/div/input')
        user_name.send_keys(TWITTER_USERNAME)
        time.sleep(10)
        button = self.driver.find_element(By.XPATH,
                                          value='//*[@id="layers"]/div/div/div/div/'
                                                'div/div/div[2]/div[2]/div/div/div[2]/'
                                                'div[2]/div/div/div/div[6]')
        button.click()
        time.sleep(10)
        password = self.driver.find_element(By.XPATH,
                                            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]'
                                                  '/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div'
                                                  '[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(20)
        inputs = self.driver.find_element(By.XPATH,
                                          value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div'
                                                '/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/'
                                                'div/div/div/div/div/div/div/div/div/div/label/div[1]/div/'
                                                'div/div/div/div/div[2]/div')
        inputs.send_keys(
            f"@{PROVIDER}, why is my internet speed {down}down/{up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up in Halmstad")
        button = self.driver.find_element(By.XPATH,
                                          value='//*[@id="react-root"]/div/div/div[2]/main/div/div'
                                                '/div/div/div/div[3]/div/div[2]/div[1]/div/div/div'
                                                '/div[2]/div[2]/div[2]/div/div/div/div[3]')
        button.click()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        button = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
        button.click()
        time.sleep(10)
        button = self.driver.find_element(By.XPATH,
                                          value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        button.click()
        time.sleep(60)
        down_speed = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]'
                                                              '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up_speed = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                            'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        return down_speed, up_speed


interface = InternetSpeedTwitterBot()
speeds = interface.get_internet_speed()
interface.tweet_at_provider(speeds[0], speeds[1])
