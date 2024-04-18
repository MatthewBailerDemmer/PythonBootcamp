from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME, value="fName")
name.send_keys("Matheus")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Bailer Demmer")
email = driver.find_element(By.NAME, value="email")
email.send_keys("matheusbailerdemmer@gmail.com")
button = driver.find_element(By.XPATH, value="/html/body/form/button")
button.click()


