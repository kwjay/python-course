import requests

params = {
    "lat": 52.406376,
    "lon": 16.925167,
    "appid": "",
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params)
print(response.status_code)
response.raise_for_status()
print(response.json())
