import time
        
class mtaVehicle:
    def __init__(self, vehicleJSON):
        self.id = vehicleJSON['id']
        self.tripId                 = vehicleJSON['vehicle']['trip']['tripId']
        self.startDate              = vehicleJSON['vehicle']['trip']['startDate']
        self.routeId                = vehicleJSON['vehicle']['trip']['routeId']
        self.latitude               = vehicleJSON['vehicle']['position']['latitude']
        self.longitude              = vehicleJSON['vehicle']['position']['longitude']
        self.bearing                = vehicleJSON['vehicle']['position']['bearing']
        self.currentStopSequence    = vehicleJSON['vehicle']['currentStopSequence']
        self.currentStatus          = vehicleJSON['vehicle']['currentStatus']
        self.timestamp              = vehicleJSON['vehicle']['timestamp']
        self.stopId                 = vehicleJSON['vehicle']['stopId']
        self.vehicleId              = vehicleJSON['vehicle']['vehicle']['id']
        self.label                  = vehicleJSON['vehicle']['vehicle']['label']

class LocalBus(mtaVehicle):
    def __init__(self, busJSON):
        super(LocalBus, self).__init__(busJSON)
        self.speed = busJSON['vehicle']['position']['speed']
        self.occupancyStatus = busJSON['vehicle']['occupancyStatus']
        self.occupancyPercentage = busJSON['vehicle']['occupancyPercentage']

    def __str__(self):
        s = f"Bus #{self.id} [{self.tripId}] is at ({self.latitude}, {self.longitude})."
        return s


class Metro(mtaVehicle):
    def __init__(self, metroJSON):
        super(Metro, self).__init__(metroJSON)

    def __str__(self):
        s = f"Metro #{self.id} [{self.tripId}] is at ({self.latitude}, {self.longitude})."
        return s


class MARC(mtaVehicle):
    def __init__(self, marcJSON):
        super(MARC, self).__init__(marcJSON)

    def __str__(self):
        s = f"MARC #{self.id} [{self.tripId}] is at ({self.latitude}, {self.longitude})."
        return s


class CommuterBus(mtaVehicle):
    def __init__(self, commuterJSON):
        super(CommuterBus, self).__init__(commuterJSON)
        self.speed = commuterJSON['vehicle']['position']['speed']

    def __str__(self):
        s = f"Commuter Bus #{self.id} [{self.tripId}] is at ({self.latitude}, {self.longitude})."
        return s