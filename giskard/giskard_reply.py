import credentials as cred
consumer_key, consumer_secret, open_weather_app_id = cred.consumer_key, cred.consumer_secret, cred.open_weather_app_id
access_token, access_token_secret = cred.giskard_access_token, cred.giskard_access_token_secret

from twython import Twython
import time
import datetime


def get_weather(latitude, longitude):
    """
    :param latitude: Decimal latitude
    :param longitude: Decimal longitude
    :return: String message.
    """
    import json
    import urllib.request
    valid_coordinates = False
    while not valid_coordinates:
        try:
            #lat, long = input("[LAT], [LONG]: ").split(", ")
            #lat, long = 39.2649, -76.5324
            lat, long = latitude, longitude
            valid_coordinates = True
        except ValueError:
            print("Enter coordinates as comma-delimited decimal latitude and longitude.")

    #api_url = f"https://api.weather.gov/points/{lat},{long}"
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={open_weather_app_id}"
    try:
        with urllib.request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
            city = data["name"]
            temperature = data["main"]["temp"]
            temperature = round((temperature - 273.15) * 9/5 + 32)  # Convert from K to deg F
            temperatureUnit = "°F"
            windSpeed = data["wind"]["speed"]
            windDirection = data["wind"]["deg"]
            return f'The current temperature at {lat}, {long} ({city}) is {temperature}{temperatureUnit}. ' \
                   f'The wind is {windSpeed}mph at heading {windDirection}. '

    except urllib.error.HTTPError:
        print("Location not found.")


def is_new_mention(this_id, old_id):
    if this_id == old_id:
        return False
    else:
        return True


starttime = time.time()
previous_id = 0

while True:
    now = datetime.datetime.now()
    # https://twython.readthedocs.io/en/latest/usage/starting_out.html
    twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
    mentions = [twitter.get_mentions_timeline()]

    latest_mention_id = mentions[0][0]["id_str"]

    if is_new_mention(latest_mention_id, previous_id):
        last_mention_url = f"https://twitter.com/BotGiskard/status/{latest_mention_id}"
        coords = mentions[0][0]["text"][12:].split(", ")
        lat, long = coords[0], coords[1]
        now = datetime.datetime.now()
        time_string = f'The time is {now.strftime("%H:%M")}. '
        message = time_string + get_weather(lat, long) + last_mention_url
        print(message)
        twitter.update_status(status=message)
    else:
        print(f'{now.strftime("%H:%M")} No new mentions.')
    previous_id = latest_mention_id

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

