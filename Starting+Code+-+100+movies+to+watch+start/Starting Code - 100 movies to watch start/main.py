import requests
from bs4 import BeautifulSoup
import io

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL).text
soup = BeautifulSoup(response, "html.parser")
movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
best_movies = movies[::-1]
text = ""
for movie in best_movies:
    text += movie + "\n"


with io.open("best_movies", "w", encoding="utf-8") as file:
    file.write(text)

