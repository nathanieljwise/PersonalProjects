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
            api = json.loads(url.read().decode())
            city = api["name"]
            temperature = api["main"]["temp"]
            temperature = round((temperature - 273.15) * 9/5 + 32)  # Convert from K to deg F
            temperatureUnit = "°F"
            windSpeed = api["wind"]["speed"]
            windDirection = api["wind"]["deg"]
            return f'The current temperature at {lat}, {long} ({city}) is {temperature}{temperatureUnit}. ' \
                   f'The wind is {windSpeed}mph at heading {windDirection}. '

    except urllib.error.HTTPError:
        print(f"{time_string}\tFailure: Location not found.")


def main():
    # https://twython.readthedocs.io/en/latest/usage/starting_out.html
    twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
    lat, long = 39.2649, -76.5324 #Fort Holabird Park
    starttime = time.time()
    while True:
        now = datetime.datetime.now()
        time_string = f'The time is {now.strftime("%H:%M")}. '
        try:
            message = time_string + get_weather(lat, long)
            twitter.update_status(status=message)
            print(f"{time_string}\tSuccess")
            time.sleep(1800.0 - ((time.time() - starttime) % 1800.0)) # Half hour delay between posts
        except TypeError:
            print(f"{time_string}\tFailure: Type Error")
        except:
            print(f"{time_string}\tFailure: Unknown Error")

if __name__ == '__main__':
    main()
