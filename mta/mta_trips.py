class Trip():
    def __init__(self, tripDict):
        self.route_id = tripDict['route_id']
        self.service_id = tripDict['service_id']
        self.trip_id = tripDict['trip_id']
        self.trip_headsign = tripDict['trip_headsign']
        self.trip_short_name = tripDict['trip_short_name']
        self.direction_id = tripDict['direction_id']
        self.block_id = tripDict['block_id']
        self.shape_id = tripDict['shape_id']
        self.wheelchair_accessible = tripDict['wheelchair_accessible']
        self.bikes_allowed = tripDict['bikes_allowed']

    def __str__(self):
        s = f"{self.trip_headsign}"
        return s


class Stop():
    def __init__(self, stopDict):
        self.stop_id = stopDict['stop_id']
        self.stop_code = stopDict['stop_code']
        self.stop_name = stopDict['stop_name']
        self.stop_desc = stopDict['stop_desc']
        self.stop_lat = stopDict['stop_lat']
        self.stop_lon = stopDict['stop_lon']
        self.zone_id = stopDict['zone_id']
        self.stop_url = stopDict['stop_url']
        self.location_type = stopDict['location_type']
        self.parent_station = stopDict['parent_station']
        self.stop_timezone = stopDict['stop_timezone']
        self.wheelchair_boarding = stopDict['wheelchair_boarding']

    def __str__(self):
        s = f"{self.stop_name}"
        return s


def loadTrips(filename):
    with open(filename, "r") as filestream:
        next(filestream)
        tripsDict = {}
        count = 1
        for line in filestream:
            thisTrip = {}
            currentline = line.split(",")
            thisTrip['route_id'] = currentline[0]
            thisTrip['service_id'] = currentline[1]
            thisTrip['trip_id'] = currentline[2]
            thisTrip['trip_headsign'] = currentline[3]
            thisTrip['trip_short_name'] = currentline[4]
            thisTrip['direction_id'] = currentline[5]
            thisTrip['block_id'] = currentline[6]
            thisTrip['shape_id'] = currentline[7]
            thisTrip['wheelchair_accessible'] = currentline[8]
            thisTrip['bikes_allowed'] = currentline[9].strip() # Chop the trailing newline
            tripsDict[thisTrip['trip_id']] = Trip(thisTrip) # Add to dictionary with ID as key and Trip object as value
            count +=1
        return tripsDict


def loadStops(filename):
    with open(filename, "r") as filestream:
        next(filestream)
        stopsDict = {}
        count = 1
        for line in filestream:
            thisStop = {}
            currentline = line.split(",")
            thisStop['stop_id'] = currentline[0]
            thisStop['stop_code'] = currentline[1]
            thisStop['stop_name'] = currentline[2]
            thisStop['stop_desc'] = currentline[3]
            thisStop['stop_lat'] = currentline[4]
            thisStop['stop_lon'] = currentline[5]
            thisStop['zone_id'] = currentline[6]
            thisStop['stop_url'] = currentline[7]
            thisStop['location_type'] = currentline[8]
            thisStop['parent_station'] = currentline[9]
            thisStop['stop_timezone'] = currentline[10]
            thisStop['wheelchair_boarding'] = currentline[11].strip() # Chop the trailing newline
            stopsDict[thisStop['stop_id']] = Stop(thisStop) # Add to dictionary with ID as key and Stop object as value
            count +=1
        return stopsDict