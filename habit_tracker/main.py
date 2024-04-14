import requests
from datetime import datetime
USER_NAME = "matheusbdemm"
TOKEN = "tu34t0ujjcwhwce9-"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

#today = str(datetime.date.today()).replace("-","")
#today = datetime(year=2024, month=3,day=27).strftime("%Y%m%d")
today = datetime.now().strftime("%Y%m%d")
pixel_config = {
    "date": today,
    "quantity": "8.00",
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixel_endpoint}/{today}"
pixeL_update_data = {
    "quantity": "15.00"
}

# response = requests.put(url=pixel_update_endpoint, json=pixeL_update_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = pixel_update_endpoint
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
