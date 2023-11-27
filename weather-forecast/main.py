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
will_rain = False
for timestamp in weather_data["list"][0]["weather"]:
    if timestamp["id"] < 700:
        will_rain = True
if will_rain:
    print("It's going to rain. Take an umbrella with you!")
else:
    print("No need to worry about getting wet")
