from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# set the driver path- You can also use WebDriverManager for drivers
#system.setProperty("webdriver.chrome.driver","E:\\MukeshData\\chromedriver.exe");

#Create object of ChromeOptions Class
chrome_options = webdriver.ChromeOptions()


#pass the debuggerAddress and pass the port along with host. Since I am running test on local so using localhost
chrome_options.add_experimental_option("debuggerAddress","localhost:9222 ")
chrome_options.binary_location = "E:\\MukeshData\\chromedriver.exe"


#pass ChromeOptions object to ChromeDriver constructor
driver = webdriver.Chrome(options=chrome_options)

#now you can use now existing Browser
driver.get("https://www.instagram.com/nasa/followers")
time.sleep(10)
followers = driver.find_elements(By.CSS_SELECTOR, value='button._acan._acap._acas._aj1-._ap30')
for follower in range(4):
    followers[follower].click()
    print('following')