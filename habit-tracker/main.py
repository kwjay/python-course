import requests
from datetime import datetime

PIXELA_URL = "https://pixe.la/v1"
USERNAME = ""
TOKEN = ""

USERS_ENDPOINT = PIXELA_URL + "/users"
USER_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# FIRST TIME ACCOUNT CREATION
# response = requests.post(url=USERS_ENDPOINT, json=USER_PARAMS)

# CREATING GRAPH
GRAPH_ENDPOINT = PIXELA_URL + f"/users/{USERNAME}/graphs"
GRAPH_CONFIG = {
    "id": "ctci",
    "name": "Cracking the coding interview",
    "unit": "pages",
    "type": "int",
    "color": "kuro",
}

HEADERS = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)

PIXEL_CREATION_ENDPOINT = GRAPH_ENDPOINT + "/" + GRAPH_CONFIG["id"]
today = datetime.now()
PIXEL_CREATION_CONFIG = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2",
}
# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=PIXEL_CREATION_CONFIG, headers=HEADERS)

pixel_date = datetime(year=2024, month=1, day=2).strftime("%Y%m%d")
PIXEL_UPDATE_ENDPOINT = PIXEL_CREATION_ENDPOINT + "/" + pixel_date
PIXEL_UPDATE_CONFIG = {
    "quantity": "4",
}
response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=PIXEL_UPDATE_CONFIG, headers=HEADERS)
print(response.text)
