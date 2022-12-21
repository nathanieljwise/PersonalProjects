from credentials import TRAIN_TRACKER_KEY
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


stations = [{'name':'18th', 'id':'40830'},            
               {'name':'35th-Bronzeville-IIT', 'id':'41120'},
               {'name':'35th/Archer', 'id':'40120'},
               {'name':'43rd', 'id':'41270'},
               {'name':'47th (Green Line)', 'id':'41080'},
               {'name':'47th (Red Line)', 'id':'41230'},
               {'name':'51st', 'id':'40130'},
               {'name':'54th/Cermak', 'id':'40580'},
               {'name':'63rd', 'id':'40910'},
               {'name':'69th', 'id':'40990'},
               {'name':'79th', 'id':'40240'},
               {'name':'87th', 'id':'41430'},
               {'name':'95th', 'id':'40450'},
               {'name':'Adams/Wabash', 'id':'40680'},
               {'name':'Addison (Blue Line)', 'id':'41240'},
               {'name':'Addison (Brown Line)', 'id':'41440'},
               {'name':'Addison (Red Line)', 'id':'41420'},
               {'name':'Argyle', 'id':'41200'},
               {'name':'Armitage', 'id':'40660'},
               {'name':'Ashland/63rd', 'id':'40290'},
               {'name':'Ashland (Green, Pink Lines)', 'id':'40170'},
               {'name':'Ashland (Orange Line)', 'id':'41060'},
               {'name':'Austin (Blue Line)', 'id':'40010'},
               {'name':'Austin (Green Line)', 'id':'41260'},
               {'name':'Belmont (Red, Brown, Purple Lines)', 'id':'41320'},
               {'name':'Belmont (Blue Line)', 'id':'40060'},
               {'name':'Berwyn', 'id':'40340'},
               {'name':'Bryn Mawr', 'id':'41380'},
               {'name':'California (Pink Line)', 'id':'40440'},
               {'name':'California (Green Line)', 'id':'41360'},
               {'name':"California (Blue Line-O'Hare Branch)", 'id':'40570'},
               {'name':'Central Park', 'id':'40780'},
               {'name':'Central (Green Line)', 'id':'40280'},
               {'name':'Central (Purple Line)', 'id':'41250'},
               {'name':'Cermak-Chinatown', 'id':'41000'},
               {'name':'Cermak-McCormick Place', 'id':'41690'},
               {'name':'Chicago (Blue Line)', 'id':'41410'},
               {'name':'Chicago (Brown Line)', 'id':'40710'},
               {'name':'Chicago (Red Line)', 'id':'41450'},
               {'name':'Cicero (Pink Line)', 'id':'40420'},
               {'name':'Cicero (Blue Line-Forest Park Branch)', 'id':'40970'},
               {'name':'Cicero (Green Line)', 'id':'40480'},
               {'name':'Clark/Division', 'id':'40630'},
               {'name':'Clark/Lake', 'id':'40380'},
               {'name':'Clinton (Blue Line)', 'id':'40430'},
               {'name':'Clinton (Green Line)', 'id':'41160'},
               {'name':'Conservatory', 'id':'41670'},
               {'name':'Cumberland', 'id':'40230'},
               {'name':'Damen (Brown Line)', 'id':'40090'},
               {'name':'Damen (Pink Line)', 'id':'40210'},
               {'name':"Damen (Blue Line-O'Hare Branch)", 'id':'40590'},
               {'name':'Davis', 'id':'40050'},
               {'name':'Dempster', 'id':'40690'},
               {'name':'Dempster-Skokie', 'id':'40140'},
               {'name':'Diversey', 'id':'40530'},
               {'name':'Division', 'id':'40320'},
               {'name':'Cottage Grove', 'id':'40720'},
               {'name':'Forest Park', 'id':'40390'},
               {'name':'Foster', 'id':'40520'},
               {'name':'Francisco', 'id':'40870'},
               {'name':'Fullerton', 'id':'41220'},
               {'name':'Garfield (Green Line)', 'id':'40510'},
               {'name':'Garfield (Red Line)', 'id':'41170'},
               {'name':'Grand (Blue Line)', 'id':'40490'},
               {'name':'Grand (Red Line)', 'id':'40330'},
               {'name':'Granville', 'id':'40760'},
               {'name':'Halsted (Green Line)', 'id':'40940'},
               {'name':'Halsted (Orange Line)', 'id':'41130'},
               {'name':'Harlem (Blue Line-Forest Park Branch)', 'id':'40980'},
               {'name':'Harlem (Green Line)', 'id':'40020'},
               {'name':"Harlem (Blue Line-O'Hare Branch)", 'id':'40750'},
               {'name':'Harold Washington Library-State/Van Buren', 'id':'40850'},
               {'name':'Harrison', 'id':'41490'},
               {'name':'Howard', 'id':'40900'},
               {'name':'Illinois Medical District', 'id':'40810'},
               {'name':'Indiana', 'id':'40300'},
               {'name':'Irving Park (Blue Line)', 'id':'40550'},
               {'name':'Irving Park (Brown Line)', 'id':'41460'},
               {'name':'Jackson (Blue Line)', 'id':'40070'},
               {'name':'Jackson (Red Line)', 'id':'40560'},
               {'name':'Jarvis', 'id':'41190'},
               {'name':'Jefferson Park', 'id':'41280'},
               {'name':'Kedzie (Brown Line)', 'id':'41180'},
               {'name':'Kedzie (Pink Line)', 'id':'41040'},
               {'name':'Kedzie (Green Line)', 'id':'41070'},
               {'name':'Kedzie-Homan (Blue Line)', 'id':'40250'},
               {'name':'Kedzie (Orange Line)', 'id':'41150'},
               {'name':'Kimball', 'id':'41290'},
               {'name':'King Drive', 'id':'41140'},
               {'name':'Kostner', 'id':'40600'},
               {'name':'Lake', 'id':'41660'},
               {'name':'Laramie', 'id':'40700'},
               {'name':'LaSalle', 'id':'41340'},
               {'name':'LaSalle/Van Buren', 'id':'40160'},
               {'name':'Lawrence', 'id':'40770'},
               {'name':'Linden', 'id':'41050'},
               {'name':'Logan Square', 'id':'41020'},
               {'name':'Loyola', 'id':'41300'},
               {'name':'Main', 'id':'40270'},
               {'name':'Midway', 'id':'40930'},
               {'name':'Monroe (Blue Line)', 'id':'40790'},
               {'name':'Monroe (Red Line)', 'id':'41090'},
               {'name':'Montrose (Blue Line)', 'id':'41330'},
               {'name':'Montrose (Brown Line)', 'id':'41500'},
               {'name':'Morgan', 'id':'41510'},
               {'name':'Morse', 'id':'40100'},
               {'name':'North/Clybourn', 'id':'40650'},
               {'name':'Noyes', 'id':'40400'},
               {'name':'Oak Park (Blue Line)', 'id':'40180'},
               {'name':'Oak Park (Green Line)', 'id':'41350'},
               {'name':'Oakton-Skokie', 'id':'41680'},
               {'name':"O'Hare", 'id':'40890'},
               {'name':'Paulina', 'id':'41310'},
               {'name':'Polk', 'id':'41030'},
               {'name':'Pulaski (Pink Line)', 'id':'40150'},
               {'name':'Pulaski (Blue Line-Forest Park Branch)', 'id':'40920'},
               {'name':'Pulaski (Green Line)', 'id':'40030'},
               {'name':'Pulaski (Orange Line)', 'id':'40960'},
               {'name':'Quincy/Wells', 'id':'40040'},
               {'name':'Racine', 'id':'40470'},
               {'name':'Ridgeland', 'id':'40610'},
               {'name':'Rockwell', 'id':'41010'},
               {'name':'Roosevelt', 'id':'41400'},
               {'name':'Rosemont', 'id':'40820'},
               {'name':'Sedgwick', 'id':'40800'},
               {'name':'Sheridan', 'id':'40080'},
               {'name':'South Boulevard', 'id':'40840'},
               {'name':'Southport', 'id':'40360'},
               {'name':'Sox-35th', 'id':'40190'},
               {'name':'State/Lake', 'id':'40260'},
               {'name':'Thorndale', 'id':'40880'},
               {'name':'UIC-Halsted', 'id':'40350'},
               {'name':'Washington/Wabash', 'id':'41700'},
               {'name':'Washington/Wells', 'id':'40730'},
               {'name':'Washington (Blue Line)', 'id':'40370'},
               {'name':'Wellington', 'id':'41210'},
               {'name':'Western (Brown Line)', 'id':'41480'},
               {'name':'Western (Pink Line)', 'id':'40740'},
               {'name':'Western (Blue Line-Forest Park Branch)', 'id':'40220'},
               {'name':"Western (Blue Line-O'Hare Branch)", 'id':'40670'},
               {'name':'Western (Orange Line)', 'id':'40310'},
               {'name':'Wilson', 'id':'40540'}]