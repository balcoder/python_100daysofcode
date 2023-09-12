''' Get weather data from openweathermap.org '''
import requests
import os
from twilio.rest import Client
from api_key import API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?"
weather_params = {
    "lat":"51.683",
    "lon":"-8.594",
    "exclude":"current,minutely,daily",
    "units": "metric",
    "appid":API_KEY
}

# get json data from openweathermap.org
response = requests.get(BASE_URL, params=weather_params, timeout=10)
response.raise_for_status()
data = response.json()

will_rain = False

def bring_umbrella(data):
    ''' loop through weather data and send sms if it's going to rain '''
    global will_rain
    weather_for_12 =  data['hourly'][:12]

    for hour in weather_for_12:
        weather_condition_id = hour['weather'][0]['id']
        if int(weather_condition_id < 700):
            will_rain = True
    if will_rain:
        send_sms("It's going to rain. Remember to bring an ☂️")
    else:
        print('Enjoy the sun')

def send_sms(message):
    ''' use twilio to send sms text message '''
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+15627413568',
        body=message,
        to='+353866067654'
        )
    print(message.status)

bring_umbrella(data)
