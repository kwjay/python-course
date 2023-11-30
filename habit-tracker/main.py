import requests

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
# print(response.text)

# CREATING GRAPH
GRAPH_ENDPOINT = PIXELA_URL + f"/users/{USERNAME}/graphs"
GRAPH_CONFIG = {
    "id": "graph1",
    "name": "Workout Graph",
    "unit": "sessions",
    "type": "int",
    "color": "kuro",
}

HEADERS = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)
# print(response.text)

