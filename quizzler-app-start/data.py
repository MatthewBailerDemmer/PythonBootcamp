import requests

params = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

question_data = requests.get(url="https://opentdb.com/api.php?", params=params)
question_data = question_data.json()["results"]