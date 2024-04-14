from bs4 import BeautifulSoup
import requests

USER = "jaa6gvsf6j8e6csx63rxdam8n"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/") #title-of-a-story
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

musics = [h3.getText().replace("\n", "").replace("\t","")
          for h3 in
          soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]
musics.insert(0, soup.find(name="h3",
                        class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
              .getText().replace("\n", "").replace("\t",""))


print(musics)


