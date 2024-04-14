from bs4 import BeautifulSoup
import lxml
import requests
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)
# all_anchor_tags = soup.find_all(name="a")
#
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText)
#
# company_url = soup.select_one(selector="p a") #selector="#name", selector=".heading"
# print(company_url)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(class_="athing", name="tr")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.select_one(".titleline a").getText())
    article_links.append(article.select_one(".titleline a").get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
article_upvotes.append(0)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])