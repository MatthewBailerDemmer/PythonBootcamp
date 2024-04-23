import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

URL_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfG_pbfUPVRsxio7q6T5uUg3UA6aB_irSlsdmf_bawNgEzaDw/viewform?usp=sf_link"
URL_DATA = "https://appbrewery.github.io/Zillow-Clone/"


def get_data():
    data = requests.get(URL_DATA)
    soup = BeautifulSoup(data.text, "html.parser")
    links = [item.get("href") for item in soup.find_all(name="a", class_="property-card-link")]
    prices = [item.text[:6] for item in
              soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
    addresses = [item.text.replace("\n", "").strip() for item in
                 soup.findAll(name="address", attrs={"data-test": "property-card-addr"})]
    return links, prices, addresses


def input_data(links, prices, addresses):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    for i in range(len(links)):
        driver.get(URL_FORM)
        time.sleep(5)
        address = driver.find_element(By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address.send_keys(addresses[i])
        price = driver.find_element(By.XPATH,
                                    value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price.send_keys(prices[i])
        link = driver.find_element(By.XPATH,
                                   value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link.send_keys(links[i])
        submit = driver.find_element(By.XPATH,
                                     value=' //*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit.click()

    driver.quit()


data = get_data()
input_data(data[0], data[1], data[2])
