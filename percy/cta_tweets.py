"""
http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=c88f71976c9d4874a05eaf932f80a331&mapid=40380&outputType=JSON
https://www.transitchicago.com/station/wils/
"""

from credentials import TRAIN_TRACKER_KEY
from cta import  CTAStation, Prediction, getData, printArrivals, stations
import requests
import json

st_95th = CTAStation(12)
data_95th = getData(12)
for i in data_95th:
    print(i["rt"], end=" ")
    print(i["rn"], end=" ")
    if int(i["isApp"]):
        print("is approaching the station.")
    else:
        print()
