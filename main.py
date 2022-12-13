import requests
from twilio.rest import Client


api_key = "api_key"
account_sid = "account_sid"
auth_token = "auth_token"

weather_params = {
    "lat": 40.416775,
    "lon": -3.703790,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
data = response.json()
weather_slice = data['hourly'][:12]

will_rain = False
for hour in weather_slice:
    weather_condition = hour['weather'][0]['id']
    if int(weather_condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain. Bring an umbrella",
        from_='+14095097627',
        to='+44XXXXXXXXXX'
    )

    print(message.status)
