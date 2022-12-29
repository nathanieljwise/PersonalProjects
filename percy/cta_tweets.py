"""
http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=c88f71976c9d4874a05eaf932f80a331&mapid=40380&outputType=JSON
https://www.transitchicago.com/station/wils/

https://docs.mapbox.com/api/maps/static-images/
"""

from twython import Twython
from credentials import google_key, consumer_key, consumer_secret, access_token, access_token_secret
from cta_parse import getData
import requests
import time
import datetime


while True:
    current_time = time.localtime()
    if not (current_time.tm_min % 5):
        chosen_station = 12
        data = getData(chosen_station)
        dest_station = data[0]["staNm"]

        base_url = "https://maps.googleapis.com/maps/api/staticmap"
        zoom = 16
        size = "700x700"
        maptype = "roadmap"
        counter = 0
        train_markers = {}

        on_time_trains = delayed_trains = unknown_trains = approaching_trains = 0
        num_trains = len(data)
        for i in data:
            #print(i["rt"],i["rn"], end=" ")
            if i["lat"]:
                if int(i["isDly"]):
                    delayed_trains += 1
                else:
                    on_time_trains += 1
                #print(f' is at {i["lat"]}, {i["lon"]} ')

                lat = float(i["lat"])
                lon = float(i["lon"])
                """
                marker_label = f'{i["rn"]}'
                #&markers=color:blue|label:S|40.702147,-74.015794
                marker = f"color:green|{lat},{lon}" # label parameter causes error
                marker = f"{lat},{lon}"
                query_string = f"center={lat},{lon}&zoom={zoom}&size={size}&maptype={type}&markers={marker}&key={google_key}"
                response = requests.get(base_url + "?" + query_string)
                with open(f"map{0+counter}.png", "wb") as f:
                    f.write(response.content)
                """

                train_markers[f'{counter}'] = {}
                train_markers[f'{counter}']["lat"] = float(i["lat"])
                train_markers[f'{counter}']["lon"] = float(i["lon"])
                train_markers[f'{counter}']["marker"] = f"{lat},{lon}" #|label:{marker_label}

                counter += 1
            else:
                unknown_trains += 1
                #print(" is at an unknown location.")
            if int(i["isApp"]):
                approaching_trains += 1
                on_time_trains -= 1

                #print("is approaching the station.")

        markers_query = ""
        for i in range(len(train_markers)):
            markers_query += f'&markers={train_markers[str(i)]["marker"]}'

        zoom = 11
        size = "400x1000"
        lat, lon = 41.848904, -87.633004
        query_string = f"center={lat},{lon}&zoom={zoom}&size={size}&maptype={maptype}{markers_query}&key={google_key}"

        response = requests.get(base_url + "?" + query_string)

        with open(f"map.png", "wb") as f:
            f.write(response.content)

        message = f'{num_trains} trains headed to {dest_station}. {approaching_trains} on approach. {on_time_trains} on time. {delayed_trains} delayed. {unknown_trains} not reporting location.'

        try:
            twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
            photo = open('map.png', 'rb')
            response = twitter.upload_media(media=photo)
            twitter.update_status(status=message, media_ids=[response['media_id']])
        except Exception as e:
            print(e)
    time.sleep(60)
