from orbit import Orbit
from latency import round_trip_latency

orbits = [
    Orbit("LEO", 550),
    Orbit("MEO", 20200),
    Orbit("GEO", 35786)
]

print("Satellite Communication Latency (RTT):\n")

for orbit in orbits:
    rtt = round_trip_latency(orbit.distance_from_earth_center())
    print(f"{orbit.name}: {rtt:.4f} seconds")
