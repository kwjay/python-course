import requests

PIXELA_URL = "https://pixe.la/v1/users"

USER_PARAMS = {
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# FIRST TIME ACCOUNT CREATION
# response = requests.post(url=PIXELA_URL, json=USER_PARAMS)
