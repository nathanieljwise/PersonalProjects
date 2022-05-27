import time
import os
from location_weather import LocationDataPoints  # My class
from credentials import OPEN_WEATHER_APP_ID

locations = {"dundalk": {"lat": 39.2649, "long": -76.5324},
             "towanda": {"lat": 41.7125, "long": -76.4688},
             "santa_maria": {"lat": 34.9454, "long": -120.448358},
             "lewisburg": {"lat": 40.9639, "long": -76.8904},
             "hixson": {"lat": 35.2007, "long": -85.191588},
             "greenville": {"lat": 34.8895, "long": -82.3325},
             "new_market": {"lat": 34.9004, "long": -86.4473},
             "columbia": {"lat": 39.185245, "long": -76.8438}
             }


starttime = time.time()
while True:
    dundalk = LocationDataPoints(locations["dundalk"]["lat"], locations["dundalk"]["long"], OPEN_WEATHER_APP_ID, city="dundalk")
    towanda = LocationDataPoints(locations["towanda"]["lat"], locations["towanda"]["long"], OPEN_WEATHER_APP_ID, city="towanda")
    santa_maria = LocationDataPoints(locations["santa_maria"]["lat"], locations["santa_maria"]["long"], OPEN_WEATHER_APP_ID, city="santa_maria")
    lewisburg = LocationDataPoints(locations["lewisburg"]["lat"], locations["lewisburg"]["long"], OPEN_WEATHER_APP_ID, city="lewisburg")
    hixson = LocationDataPoints(locations["hixson"]["lat"], locations["hixson"]["long"], OPEN_WEATHER_APP_ID, city="hixson")
    greenville = LocationDataPoints(locations["greenville"]["lat"], locations["greenville"]["long"], OPEN_WEATHER_APP_ID, city="greenville")
    new_market = LocationDataPoints(locations["new_market"]["lat"], locations["new_market"]["long"], OPEN_WEATHER_APP_ID, city="new_market")
    columbia = LocationDataPoints(locations["columbia"]["lat"], locations["columbia"]["long"], OPEN_WEATHER_APP_ID, city="columbia")

    locations_list = [dundalk, towanda, santa_maria, lewisburg, hixson, greenville, new_market, columbia]

    for location in locations_list:
        log_point = f"{location.final_output}\n"
        file_name = f"{location.file_name}"
        with open(file_name, "a") as log:
            log.write(f"{log_point}")
            log.close()
    time.sleep(600.0 - ((time.time() - starttime) % 600.0))
