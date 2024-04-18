from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3883460961&eBP"
    "=CwEAAAGO8nQYbpGGZQwfqGbEMDDbv4XY5zXNowVW9VYhgAVigYsLwKh28LMFqq9VGfxRt0p4hU6qg9N8AlM"
    "aFobRkgGmlIMvWybagv8sk2SwWrWd4clthZuQp14r-GjyDrfbf1_N3Vd8i6qkqIircKrYFQH42NRmeMQuSdD1"
    "HU9pywEa27LVlLW0dC2kyAev7pMo9GEUhYy-spvVIsS8dSOoyh4E6SQX373vOjL8HV7Oj-570IiofJd_ukNlzfP"
    "JoJqLG8Z0aTWstmStx1IdDej9NoGKTEshBCuH8gegChozCrinZZZymiEps0wVypU7IE3jsrhqpZdVh0otXAOIqb9"
    "hzx5-fSzrD46W0aOcjv1EogatOT6K9_hN&refId=7fqCbHa1OkN2mMiJ4Kc9%2Fw%3D%3D&trackingId=Ee2TETh8"
    "qv0VSWQniXCqEg%3D%3D")
time.sleep(10)
login = driver.find_element(By.ID, value="username")
login.send_keys("matheusbailerdemmer@gmail.com")
password = driver.find_element(By.ID, value="password")
password.send_keys("matheusbd1999")
button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
button.click()
time.sleep(20)
button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
button.click()
time.sleep(20)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()
time.sleep(20)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="#ember306")
submit_button.click()
time.sleep(20)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="#ember313")
submit_button.click()
# they are all changing
