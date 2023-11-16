''' check if ISS is within sight and it's dark enough to see it '''
import math
import time
import smtplib
import datetime as dt
import requests

MY_LAT = 51.620800
MY_LONG = -8.894160

# store latitude and longitude on dictionary
paramaters = {
    'lat': MY_LAT,
    'long': MY_LONG,
    'formatted': 0
}

def check_light_level():
    ''' check if it's dark enough to see space station'''
    response = requests.get("https://api.sunrise-sunset.org/json", params=paramaters, timeout=10)
    response.raise_for_status()
    daylight_data = response.json()
    sunrise = int(daylight_data['results']['nautical_twilight_begin'].split('T')[1].split(':')[0])
    sunset = int(daylight_data['results']['nautical_twilight_end'].split('T')[1].split(':')[0])    
    time_now = dt.datetime.now()
    list_part1 = [x for x in range(1, sunrise + 1)]
    list_part2 = [x for x in range(sunset, 25)]
    sighting_hours = list_part1 + list_part2   

    if time_now.hour in sighting_hours:        
        return True
    return False

def check_iss_position():
    ''' check if ISS is within +5 or -5 degrees of our position '''
    response = requests.get("http://api.open-notify.org/iss-now.json", timeout=10)
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    lat_range = [x for x in range(int(MY_LAT) - 5, int(MY_LAT) + 5)]
    long_range = [x for x in range(int(MY_LONG) -5, int(MY_LONG) +5)]
    # print(f"Lat range: {lat_range}")
    # print(f"Long range: {long_range}")
    if math.floor(latitude) in lat_range and math.floor(longitude) in long_range:
        # we can see the ISS
        return True
    return False

# email details
password= ""
my_email = ""
user_email = ""
host = "smtp.gmail.com"
send_to = ""
message = "Subject: ISS Overhead\n\nLook up the ISS is passing overhead soon"

while True:
    time.sleep(1800) # run once every half hour
    if check_light_level() and check_iss_position():
        # send email
        with smtplib.SMTP(host) as connection:        
            connection.starttls() # transport layer security
            connection.login(user=user_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=send_to,
                msg=message)
