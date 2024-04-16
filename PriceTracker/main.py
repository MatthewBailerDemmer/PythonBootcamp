import requests
from bs4 import BeautifulSoup
import smtplib
my_email = "matheusbailerdemmer@gmail.com"
password = "kzugfeqnllouqpdl"

URL = "https://www.amazon.com/dp/B09836V1BD/ref=sr_1_1_sspa?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3S6R0NTWR7SFU&dib=eyJ2IjoiMSJ9.K0kyXYg60JSqAEzuGuhSmXNzGPSdYsmzlsrd0J3PanR3pRlPN7AgxdxtFW01F7efltDMy18sL4khdT--6mByltoL4ajLBJULEa3RkF_HbhX2upR7FBdQYq-IcpCJw1E8vQ0hF-Q7GtmyW-sdNRmVl3EvSM0RJ-Lgh_J_vQllEupHpbTYzmpOdbpnzXn3mpdycT7e-Z6_Y1CkVY9nCf_zefK9SUjfrKThuYFspb7k_Kg.HyXNq7FxqkCpatJ_MY1PLxKixy1F1C0hcxuNVhCu1ac&dib_tag=se&keywords=telescope&qid=1713229525&sprefix=tr%2Caps%2C1828&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"

minimum_price = 100.00

header = {
    "Accept-Language": "en,tr-TR;q=0.9,tr;q=0.8,en-US;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.82 Safari/537.36"
}

response = requests.get(url=URL, headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
item_title = soup.find(name="input", id="productTitle").get("value").replace("&amp;", "")
price_value = float(soup.find(name="input", id="priceValue").get("value"))
message = f"{item_title} ${price_value}"
if price_value < minimum_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}")

