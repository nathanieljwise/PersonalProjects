import requests
import json
import urllib.request


class Closure():
    def __init__(self, jsonOBJ):
        # https://opendata.maryland.gov/resource/nigh-m2sg.json
        self.county = jsonOBJ["county"]
        self.incident = jsonOBJ["incident"]
        self.direction = jsonOBJ["direction"]
        self.link = jsonOBJ["link"]
        self.lanes = "\t" + jsonOBJ["lanes"].replace(".",".\n\t")
        self.created = jsonOBJ["created"]
        self.updated = jsonOBJ["updated"]
        
        # I'm not sure how this JSON handles lat/long
        '''
        'lat': '{"x":-78.987987,"y":39.559577,"spatialReference":{"wkid":4326}}',
        'long': '{"x":-76.060086,"y":38.558139,"spatialReference":{"wkid":4326}}',
        '''
        self.coords1 = json.loads(jsonOBJ["lat"])
        self.coords2 = json.loads(jsonOBJ["long"])
        self.lat1 = self.coords1["y"]
        self.long1 = self.coords1["x"]
        self.lat2 = self.coords2["y"]
        self.long2 = self.coords2["x"]
        self.latlong1 = f"{self.lat1}, {self.long1}"
        self.latlong2 = f"{self.lat2}, {self.long2}"


        '''
        self.lat1 = jsonOBJ["lat"]["y"]
        self.lat2 = jsonOBJ["long"]["y"]
        self.long1 = jsonOBJ["lat"]["x"]
        self.long2 = jsonOBJ["long"]["y"]
        '''


    def __str__(self):
        #s = f"{self.county}\n{self.incident}\n{self.lanes}\n\t{self.latlong1}\n\t{self.latlong2}"
        s = f"{self.county} {self.updated}\n{self.incident}\n{self.lanes}{self.latlong1}\n\t{self.latlong2}"
        return s

def loadData(jsonURL):
    with urllib.request.urlopen(jsonURL) as url:
        data = json.loads(url.read().decode())
    return data

if __name__ == "__main__":
    roadClosureURL = "https://opendata.maryland.gov/resource/nigh-m2sg.json"
    data = loadData(roadClosureURL)
    for i in data:
        thisClosure = Closure(i)
        print(thisClosure)
        print()
