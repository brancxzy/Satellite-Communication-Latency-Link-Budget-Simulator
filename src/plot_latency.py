import matplotlib.pyplot as plt
from orbit import Orbit
from latency import round_trip_latency

orbits = [
    Orbit("LEO", 550),
    Orbit("MEO", 20200),
    Orbit("GEO", 35786)
]

names = []
latencies = []

for orbit in orbits:
    names.append(orbit.name)
    latencies.append(round_trip_latency(orbit.distance_from_earth_center()))

plt.figure()
plt.bar(names, latencies)
plt.xlabel("Orbit Type")
plt.ylabel("Round-Trip Latency (seconds)")
plt.title("Satellite Communication Latency Comparison")

plt.tight_layout()
plt.savefig("latency_comparison.png")
