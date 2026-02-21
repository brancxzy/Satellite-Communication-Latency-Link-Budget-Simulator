EARTH_RADIUS_KM = 6371

class Orbit:
    def __init__(self, name, altitude_km):
        self.name = name
        self.altitude_km = altitude_km

    def distance_from_earth_center(self):
        return EARTH_RADIUS_KM + self.altitude_km
