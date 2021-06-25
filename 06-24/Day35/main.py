import requests
import os
from twilio.rest import Client

# Open Weather
API_KEY = os.environ.get("OWM_API_KEY")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
LAT = "<LATITUDE>"
LON = "<LONGITUDE>"

# Twilio
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

#------------WEATHER------------
weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:13]

will_rain = False

for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 600:
        will_rain = True
        
if will_rain:
    #------------SMS Using Twilio------------
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Bring an umbrella with you ☔️",
            from_='<Twilio Number>',
            to='<Your Phone Number>'
            )
    print(message.status)
