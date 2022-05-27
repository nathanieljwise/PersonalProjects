import json
import urllib.request
import datetime


class LocationDataPoints:
    def __init__(self, lat, long, open_weather_app_id, city):
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={open_weather_app_id}"
        with urllib.request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
            now = datetime.datetime.now()
            self.city_name = city
            self.time_var = f"{now.strftime('%H%M%S')}"
            self.date_var = f"{now.strftime('%Y%m%d')}"
            self.temperature = data["main"]["temp"]
            self.temperature = (self.temperature - 273.15) * 9 / 5 + 32  # Convert from K to deg F
            self.temperature = (f"{self.temperature:.2f}")
            self.pressure = data["main"]["pressure"]  # millibars
            self.humidity = data["main"]["humidity"]
            self.windSpeed = data["wind"]["speed"]
            self.windDirection = data["wind"]["deg"]
            self.file_name = f"{city}_weather.txt"
            self.final_output = f'{self.date_var}\t{self.time_var}\t{self.temperature}\t{self.windSpeed}\t' \
                                f'{self.windDirection}\t{self.pressure}\t{self.humidity}'
