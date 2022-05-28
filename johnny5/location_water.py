import json
import urllib.request
import datetime

class LocationDataPoints:
    def __init__(self, id, name):
        api_url = f"https://waterservices.usgs.gov/nwis/iv/?format=json&indent=on&sites={id}"
        with urllib.request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
            now = datetime.datetime.now()
            self.station_name = f'{name}'
            self.time_var = f"{now.strftime('%H%M')}"
            self.date_var = f"{now.strftime('%Y%m%d')}"
            self.stream_flow = data["value"]["timeSeries"][0]["values"][0]["value"][0]["value"]
            self.gage_height = data["value"]["timeSeries"][1]["values"][0]["value"][0]["value"]
            self.final_output = f'{self.date_var}\t{self.time_var}\t{self.stream_flow}\t{self.gage_height}'