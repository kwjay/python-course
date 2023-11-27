import requests

params = {
    "lat": 52.406376,
    "lon": 16.925167,
    "appid": "",
    "cnt": 4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
for timestamp in weather_data["list"][0]["weather"]:
    if timestamp["id"] < 700:
        print("Bring an umbrella")
    else:
        print("No need to worry about getting wet")
