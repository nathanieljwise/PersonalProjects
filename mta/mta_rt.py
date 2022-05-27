import json
import http.client
from vehicle_classes import LocalBus, Metro, MARC, CommuterBus
import mta_trips
from credentials import mtaSwiftlyKey as apiKey
#https://api.goswift.ly/info/{agencyKey}/routes

def getData(agencyKey, endpoint):
    conn = http.client.HTTPSConnection("api.goswift.ly")
    headers = {
        'Content-Type': "application/json",
        'Authorization': apiKey
        }
    conn.request("GET", f"/real-time/{agencyKey}/{endpoint}?format=json", headers=headers)
    res = conn.getresponse()
    data = json.loads(res.read())
    return data


def showBusesRT(busData):
    busTrips = mta_trips.loadTrips("resources/localbus_trips.txt")
    busStops = mta_trips.loadStops("resources/localbus_stops.txt")
    count = 1
    print()
    print("Local Buses:")
    if 'entity' in busData:
        for i in busData['entity']:
            try:
                thisBus = LocalBus(i)
                thisTripId = thisBus.tripId
                thisTripName = busTrips[f'{thisTripId}']
                print(thisTripName)
                thisStopId = thisBus.stopId
                thisStopName = busStops[f'{thisStopId}']
                print(f"\t{count}. {thisBus} {thisBus.currentStatus} {thisStopName}")
                count += 1
            except:
                pass


def showMetroRT(metroData):
    metroTrips = mta_trips.loadTrips("resources/metro_trips.txt")
    metroStops = mta_trips.loadStops("resources/metro_stops.txt")
    count = 1
    print()
    print("Metro:")
    if 'entity' in metroData:
        for i in metroData['entity']:
            try:
                thisMetro = Metro(i)
                thisTripId = thisMetro.tripId
                thisTripName = metroTrips[f'{thisTripId}']
                print(thisTripName)
                thisStopId = thisMetro.stopId
                thisStopName = metroStops[f'{thisStopId}']
                print(f"\t{count}. {thisMetro} {thisMetro.currentStatus} {thisStopName}")
                count += 1
            except:
                pass


def showMARCRT(marcData):
    marcTrips = mta_trips.loadTrips("resources/marc_trips.txt")
    marcStops = mta_trips.loadStops("resources/marc_stops.txt")
    count = 1
    print()
    print("MARC:")
    if 'entity' in marcData:
        for i in marcData['entity']:
            try:
                thisMARC = MARC(i)
                thisTripId = thisMARC.tripId
                print(thisTripId)
                thisTripName = marcTrips[f'{thisTripId}'].trip_headsign
                print(thisTripName)
                print(f"\t{count}. {thisMARC} {thisMARC.currentStatus}")
                count += 1
            except:
                pass
            

def showCommuterRT(commuterData):
    commuterTrips = mta_trips.loadTrips("resources/commuter_trips.txt")
    commuterStops = mta_trips.loadStops("resources/commuter_stops.txt")
    count = 1
    print()
    print("Commuter Buses:")
    if 'entity' in commuterData:
        for i in commuterData['entity']:
            try:
                thisCommuter = CommuterBus(i)
                thisTripId = thisCommuter.tripId
                thisTripName = commuterTrips[f'{thisTripId}']
                print(thisTripName)
                thisStopId = thisCommuter.stopId
                thisStopName = commuterStops[f'{thisStopId}']
                print(f"\t{count}. {thisCommuter} {thisCommuter.currentStatus} {thisStopName}")
                count += 1
            except:
                pass


if __name__ == "__main__":
    agencyKeys = {"bus": "mta-maryland", "commuterBus": "mta-maryland-commuter-bus", "metro": "mta-maryland-metro", "marc": "mta-maryland-marc"}
    endpoints = {"rt-trip-updates":"gtfs-rt-trip-updates", "rt-vehicle-positions":"gtfs-rt-vehicle-positions"}

    buses = getData(agencyKeys["bus"], endpoints["rt-vehicle-positions"])
    metro = getData(agencyKeys["metro"], endpoints["rt-vehicle-positions"])    
    marc = getData(agencyKeys["marc"], endpoints["rt-vehicle-positions"])
    commuter = getData(agencyKeys["commuterBus"], endpoints["rt-vehicle-positions"])

    #showBusesRT(buses)
    #showMetroRT(metro)
    showMARCRT(marc)
    #showCommuterRT(commuter)
