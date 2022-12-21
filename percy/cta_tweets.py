"""
http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=c88f71976c9d4874a05eaf932f80a331&mapid=40380&outputType=JSON
https://www.transitchicago.com/station/wils/

https://docs.mapbox.com/api/maps/static-images/
"""

from credentials import TRAIN_TRACKER_KEY, google_key
from cta_parse import CTAStation, Prediction, getData, printArrivals, stations
import requests
import json

st_95th = CTAStation(12)
data_95th = getData(12)


base_url = "https://maps.googleapis.com/maps/api/staticmap"
zoom = 16
size = "700x700"
type = "roadmap"
counter = 0
train_markers = {}

for i in data_95th:
    #print(i["rt"],i["rn"], end=" ")
    if int(i["isApp"]):
        pass
        #print("is approaching the station.")
    elif i["lat"]:
        #print(f' is at {i["lat"]}, {i["lon"]} ')

        lat = float(i["lat"])
        lon = float(i["lon"])
        marker_label = f'{i["rn"]}'
        #marker = f"{lat},{lon}|label:{marker_label}" # label parameter causes error
        marker = f"{lat},{lon}"

        query_string = f"center={lat},{lon}&zoom={zoom}&size={size}&maptype={type}&markers={marker}&key={google_key}"

        response = requests.get(base_url + "?" + query_string)

        with open(f"map{0+counter}.png", "wb") as f:
            f.write(response.content)

        
        train_markers[f'{counter}'] = {}
        train_markers[f'{counter}']["lat"] = float(i["lat"])
        train_markers[f'{counter}']["lon"] = float(i["lon"])
        #train_markers[f'{counter}']["marker_label"] = f'{i["rn"]}'
        train_markers[f'{counter}']["marker"] = f"{lat},{lon}" #|label:{marker_label}

        counter += 1
    else:
        pass
        #print(" is at an unknown location.")

markers_query = ""
for i in range(len(train_markers)):
    markers_query += f'&markers={train_markers[str(i)]["marker"]}'

zoom = 11
size = "300x1500"
query_string = f"center={41.823815},{-87.630285}&zoom={zoom}&size={size}&maptype={type}{markers_query}&key={google_key}"

response = requests.get(base_url + "?" + query_string)

with open(f"map.png", "wb") as f:
    f.write(response.content)