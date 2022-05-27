class StopTime():
    def __init__(self):
        self.trip_id = ""
        self.arrival_time = ""
        self.departure_time = ""
        self.stop_id = ""
        self.stop_sequence = ""
        self.stop_headsign = ""
        self.pickup_type = ""
        self.drop_off_type = ""
        self.shape_dist_traveled = ""


class Trip():
    def __init__(self):
        self.route_id = ""
        self.service_id = ""
        self.trip_id = ""
        self.trip_headsign = ""
        self.trip_short_name = ""
        self.direction_id = ""
        self.block_id = ""
        self.shape_id = ""
        self.wheelchair_accessible = ""
        self.bikes_allowed = ""

class Route():
    def __init__(self, routeObj):
        self.route_id = routeObj["id"]
        #self.agency_id = routeObj["agency_id"]
        self.route_short_name = routeObj["shortName"]
        self.route_long_name = routeObj["longName"]
        self.route_desc = routeObj["name"]
        self.route_type = routeObj["type"]
        #self.route_url = routeObj["route_url"]
        self.route_color = routeObj["color"]
        self.route_text_color = routeObj["textColor"]
        #self.network_id = routeObj["network_id"]
        #self.as_route = routeObj["as_route"]

    def __str__(self):
        s = f"{self.route_desc}"
        return s



class Stop():
    def __init__(self):
        # https://developers.google.com/transit/gtfs/reference#stopstxt
        self.stop_id = ""  #Identifies a stop, station, or station entrance.
        self.stop_code = ""  # Short text or a number that identifies the location for riders. 
        self.stop_name = ""  # Name of the location
        self.stop_desc = ""  # Description of the location that provides useful, quality information.
        self.stop_lat = ""  # Latitude of the location
        self.stop_lon = ""  # Longitude of the location
        self.zone_id = ""  # Identifies the fare zone for a stop
        self.stop_url = ""  # URL of a web page about the location
        self.location_type = ""  # Type of the location: 0/empty=Stop or platform, 1=Station, 2=Entrance/Exit, 3=Generic node, 4=Boarding area
        self.parent_station = ""  # Defines hierarchy between the different locations defined in stops.txt
        self.stop_timezone = ""  # Timezone of the location
        self.wheelchair_boarding = ""  # Indicates whether wheelchair boardings are possible from the location: 0=No info, 1=Some accesible boarding, 2=No wheelchair accessible path
