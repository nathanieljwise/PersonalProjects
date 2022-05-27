"""
http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=c88f71976c9d4874a05eaf932f80a331&mapid=40380&outputType=JSON
https://www.transitchicago.com/station/wils/
"""

from credentials import TRAIN_TRACKER_KEY
from cta_stations import stations
import requests
import json


class CTAStation():
    def __init__(self, stationNumber):
        self.mapID = stations[stationNumber]["id"]
        self.stationName = stations[stationNumber]["name"]


class Prediction():
    def __init__(self, jsonObj):
        # Documentation: https://www.transitchicago.com/developers/ttdocs/
        self.stationID = jsonObj["staId"] #Numeric GTFS parent station ID which this prediction is for (five digits in 4xxxx range) (matches "mapid" specified by requestor in query)
        self.stopID = jsonObj["stpId"] #Numeric GTFS unique stop ID within station which this prediction is for (five digits in 3xxxx range)
        self.stationName = jsonObj["staNm"] #Textual proper name of parent station
        self.stopDescription = jsonObj["stpDe"] #Textual description of platform for which this prediction applies
        self.run = jsonObj["rn"] #Run number of train being predicted for
        self.route = jsonObj["rt"] #Textual, abbreviated route name of train being predicted for (matches GTFS routes)
        self.destinationStation = jsonObj["destSt"] #GTFS unique stop ID where this train is expected to ultimately end its service run (experimental and supplemental only)
        self.destinationFriendlyName = jsonObj["destNm"] #Friendly destination description
        self.routeDirection = jsonObj["trDr"] #Numeric train route direction code
        self.predictionTime = jsonObj["prdt"] #Date-time format stamp for when the prediction was generated: yyyyMMdd HH:mm:ss (24-hour format, time local to Chicago)
        self.arrivalTime = jsonObj["arrT"] #Date-time format stamp for when a train is expected to arrive/depart: yyyyMMdd HH:mm:ss (24-hour format, time local to Chicago)
        self.isApproaching = jsonObj["isApp"] #Indicates that Train Tracker is now declaring "Approaching or "Due" on site for this train
        self.isScheduled = jsonObj["isSch"] #Boolean flag to indicate whether this is a live prediction or based on schedule in lieu of live data
        self.isFault = jsonObj["isFlt"] #Boolean flag to indicate whether a potential fault has been detected (see note below)
        self.isDelayed = jsonObj["isDly"] #Boolean flag to indicate whether a train is considered "delayed" in Train Tracker
        self.flags = jsonObj["flags"] #Train flags (not presently in use)
        self.latitude = jsonObj["lat"] #Latitude position of the train in decimal degrees
        self.longitude = jsonObj["lon"] #Longitude position of the train in decimal degrees
        self.heading = jsonObj["heading"] #Heading, expressed in standard bearing degrees (0 = North, 90 = East, 180 = South, and 270 = West; range is 0 to 359, progressing clockwise)

    def __str__(self):
        s = f"{self.route} #{self.run}; arrival time {self.arrivalTime[-8:-3]} (as of {self.predictionTime[-8:-3]})"
        return s


def displayStations():
    """
    Description: Prints a numbered list of all CTA train stations.
    """
    count = 0
    for j in range(0,int(len(stations))//3+1):
        for i in range(0, 3):
            if count < len(stations):
                strCount = str(count+1) + "."
                #print(f" {stations[count-1]['name']:<42} |{stations[i]['id']}|",end="")
                print(f"{strCount:<4} {stations[count]['name']:43}",end="")
                count+=1
        print()


def getData(thisStop):
    """
    :param thisStop: Integer; converted to a stop with ID and name
    Description: Takes an integer, converts to a station from the list of
    stations, and gets data from CTA for that station.
    :return: JSON object from CTA API
    """
    currentStation = CTAStation(thisStop) # Grabs ID and name from dictionary of stops
    mapID = currentStation.mapID
    apiPage = f"http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={TRAIN_TRACKER_KEY}&mapid={mapID}&outputType=JSON"
    apidata = requests.get(apiPage) # Load page from CTA
    data = json.loads(apidata.text) # JSON object with prediction info for all incoming trains

    timestamp = data['ctatt']['tmst'][-8:-3] # Date and time for when the data was obtained
    currentName = currentStation.stationName

    try:
        incomingTrains = data['ctatt']['eta']
        print(f"{timestamp} Number of train(s) expected at {currentName} Station: {len(incomingTrains)}")
        return incomingTrains
    except KeyError:
        print("No incoming trains.")
        return -1


def printArrivals(trainList):
    """
    :param trainList: JSON object of incoming trains
    Description: Prints all arrivals for a chosen station
    """
    trains = trainList
    for i in range(0,len(trains)):
        trainPrediction = Prediction(trains[i])
        print(f"{i+1}: {trainPrediction}.")
    print()


def main():
    displayStations()
    userStation = int(input("\nChoose a station (-1 to quit): "))
    print()

    while userStation > -1:
        if userStation == 0:  # Hidden command
            displayStations()
        elif userStation > 142:  # 142 stations in CTA system
            print("Please enter a valid station number.")
        else:
            theseTrains = getData(userStation-1)
            printArrivals(theseTrains)
        userStation = int(input("\nChoose a station (-1 to quit): "))
        print()


main()