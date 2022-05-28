import json
import http.client

conn = http.client.HTTPSConnection("api.goswift.ly")

headers = {
    'Content-Type': "application/json",
    'Authorization': "1ee674f78037045f5e600a63047d869b"
    }


class Vehicle():
    def __init__(self, vehicleJSON):
        self.id = vehicleJSON['id']
        #'vehicle': {'trip': {'tripId': '3017901', 'startDate': '20220522', 'routeId': '11659'}, 
        self.latitude = vehicleJSON['vehicle']['position']['latitude']
        self.longitude = vehicleJSON['vehicle']['position']['longitude']
        self.bearing = vehicleJSON['vehicle']['position']['bearing']
        self.speed = vehicleJSON['vehicle']['position']['speed']
        self.occupancyStatus = vehicleJSON['vehicle']['occupancyStatus']
    def __str__(self):
        s = f"Vehicle {self.id} is at {self.latitude}, {self.longitude} at {self.speed} MPH.\t({self.occupancyStatus})"
        return s

def rtVehiclePositions():
    conn.request("GET", "/real-time/mta-maryland/gtfs-rt-vehicle-positions?format=json", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read())
    count = 1
    for i in range(0, len(data['entity'])):
        #if i['id'] == '16085':
        #    print(f"Vehicle {i['id']} is at {i['vehicle']['position']['latitude']}, {i['vehicle']['position']['longitude']} going {i['vehicle']['position']['speed']}")
        #    print(i)
        try:
            thisVehicle = Vehicle(data['entity'][i])
            print(f"{count}. {thisVehicle}")
            count += 1
        except:
            pass

def rtTripUpdates():
    conn.request("GET", "/real-time/mta-maryland/gtfs-rt-trip-updates?format=json", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read())


    for i in range(0,len(data['entity'])):
        if data['entity'][i]['tripUpdate']['trip']['tripId'] == "3017901":
            pass
            #for stop in data['entity'][i]['tripUpdate']['stopTimeUpdate']:
            #    print(stop)
            #print(data['entity'][i]['tripUpdate']['vehicle']['id'])


rtVehiclePositions()
rtTripUpdates()

'''import requests
from credentials import mtaKey
from gtfs import Route, Stop, Trip, StopTime
true = True
mtaKey2 = "2ccb109a95f0a44525d38c336cf15db2"

agencyKeys = {"bus":"mta-maryland",
              "commuter":"mta-maryland-commuter-bus",
              "metro":"mta-maryland-metro",
              "marc":"mta-maryland-marc"}


def getRoutesData(agencyKey):
    parameters = {'apiKey': mtaKey2, 'Content-Type': 'application/json'}
    r = requests.get(f"https://api.goswift.ly/real-time/{agencyKey}/gtfs-rt-vehicle-positions", params=parameters)
    jsonObj = r.json()
    return jsonObj


def loadBus():
    busData = getRoutesData(agencyKeys["bus"])
    for i in busData["data"]["routes"]:
        thisRoute = Route(i)
        print(thisRoute)
    print()
    return busData


def loadCommuter():
    commuterData = getRoutesData(agencyKeys["commuter"])
    for i in commuterData["data"]["routes"]:
        thisRoute = Route(i)
        print(thisRoute)
    return commuterData


def loadMetro():
    metroData = getRoutesData(agencyKeys["metro"])
    for i in metroData["data"]["routes"]:
        thisRoute = Route(i)
        print(thisRoute)
    return metroData


def loadMarc():
    marcData = getRoutesData(agencyKeys["marc"])
    for i in marcData["data"]["routes"]:
        thisRoute = Route(i)
        print(thisRoute)
    print()
    return marcData


def main():
    buses = loadBus()
    commuters = loadCommuter()
    metros = loadMetro()
    marcs = loadMarc()
    


main()

"""
for key in agencyKeys:
    print(key)
    thisObj = getRoutesData(agencyKeys[key])
    for i in thisObj["data"]["routes"]:
        print(i["longName"])
    print()
#print(r.url)
"""
'''
