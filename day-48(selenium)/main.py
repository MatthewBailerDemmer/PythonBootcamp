from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep the Chrome brower open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="green").text
# print(f"The price is {price_dollar}")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
#
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

events_time_selenium = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div')
event_string = events_time_selenium[0].text
event_list = event_string.split("\n")
del event_list[0]
event_list.remove("More")
event_dic = {}
for i in range(0, len(event_list) - 1, 2):
    event_dic[f"{int(i/2)}"] = {
        "time": event_list[i],
        "name": event_list[i + 1]
    }
print(event_dic)
#driver.close() # closes the particular tab
driver.quit() # closes the entire browser
