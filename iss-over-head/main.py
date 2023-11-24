import requests
from datetime import datetime
import smtplib

MY_EMAIL = "mail@gmail.com"
MY_PASSWORD = "password"
MY_PROVIDER = "smtp.gmail.com"


def send_email():
    with smtplib.SMTP(MY_PROVIDER) as server:
        server.starttls()
        server.login(user=MY_EMAIL, password=MY_PASSWORD)
        server.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:LOOK UP\n\nISS IS OVER HEAD!!!")


MY_LAT = 51.507351
MY_LONG = -0.127758

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(iss_latitude)
print(iss_longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunset)
print(sunrise)
time_now = datetime.now()
hour = time_now.hour

if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
    if sunset < hour or hour < sunrise:
        send_email()
