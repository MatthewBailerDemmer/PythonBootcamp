from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)




driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(10)
eng = driver.find_element(By.ID, value="langSelect-EN")
eng.click()
time.sleep(10)
cookie = driver.find_element(By.ID, value="bigCookie")

timez = time.time() + 5
time_final = time.time() + 1 * 60

while True:
    cookie.click()
    now = time.time()
    if now >= time_final:
        break
    if now >= timez:
        stuff = driver.find_elements(By.CSS_SELECTOR, value="#products .product.unlocked.enabled")
        prices = [int(item.text.split("\n")[1]) for item in stuff]
        try:
            stuff[prices.index(max(prices))].click()
        except:
            print("nothing available")

        timez = time.time() + 5


