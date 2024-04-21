from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)




driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
time.sleep(5)
button_entrar = driver.find_element(By.XPATH, value='//*[@id="o515699397"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
button_entrar.click()
time.sleep(5)
button_entrar = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button')
button_entrar.click()
time.sleep(5)
button_entrar = driver.find_element(By.XPATH, value='//*[@id="o-1212681679"]/main/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/input')
button_entrar.send_keys("0737421648")
button_entrar.send_keys(Keys.ENTER)
time.sleep(60)
button_entrar = driver.find_element(By.XPATH, value='//*[@id="o-1212681679"]/main/div[2]/div/div/div[1]/div[2]/button')
button_entrar.click()
time.sleep(10)
button_entrar = driver.find_element(By.XPATH, value='//*[@id="o-1212681679"]/main/div/div/div/div[3]/button[1]')
button_entrar.click()
time.sleep(5)
button_entrar = driver.find_element(By.XPATH, value='//*[@id="o-1212681679"]/main/div/div/div/div[3]/button[2]')
button_entrar.click()
time.sleep(15)
for i in range(5):
    time.sleep(10)
    button_entrar = driver.find_element(By.CSS_SELECTOR, value='#o515699397 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > div > main > div > div > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button')
    button_entrar.click()
#Numero de tentatias extouradas
#Mudaram a parada