SPEED_OF_LIGHT = 3e8  # meters per second

def km_to_meters(km):
    return km * 1000

def one_way_latency(distance_km):
    return km_to_meters(distance_km) / SPEED_OF_LIGHT

def round_trip_latency(distance_km):
    return 2 * one_way_latency(distance_km)
