from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Initialize chrome debbuger: go on the cmd to where the chrome.exe is and run this script
#chrome.exe -remote-debugging-port=9222 -user-data-dir=E:\chromeData

#Create object of ChromeOptions Class
chrome_options = webdriver.ChromeOptions()

#pass the debuggerAddress and pass the port along with host. Since I am running test on local so using localhost
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222 ")
# set the driver path- You can also use WebDriverManager for drivers
chrome_options.binary_location = "E:\\MukeshData\\chromedriver.exe"

#pass ChromeOptions object to ChromeDriver constructor
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/app/recs")
time.sleep(10)
try:
    prop = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div[1]/div[4]/button[2]')
    prop.click()
except:
    print("Excecione")
while True:
    try:
        button = driver.find_element(By.CSS_SELECTOR, value='#o515699397 > div > div.App__body.H'+
                                                        '\(100\%\).Pos\(r\).Z\(0\) > div > main >'+
                                                        ' div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)'+
                                                        '--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw'+
                                                        '\(--recs-card-width\)--ml > div.recsCardboard__cards'+
                                                        'Container.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\)'+
                                                        '.B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > '+
                                                        'div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs'+
                                                        '\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > '+
                                                        '   button')
        button.click()
    except:
        try:
            pop = driver.find_element(By.XPATH, value='// *[ @ id = "o-1212681679"] / main / div / div[2] / button[2]')
            print("Deu ruim mais voltei")
        except:
            print("Deu RUim")
            break
    time.sleep(5)
