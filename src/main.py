import argparse
from orbit import Orbit
from latency import round_trip_latency

ORBIT_CONFIGS = {
    "LEO": 550,
    "MEO": 20200,
    "GEO": 35786
}

def run_single_orbit(name):
    altitude = ORBIT_CONFIGS[name]
    orbit = Orbit(name, altitude)
    rtt = round_trip_latency(orbit.distance_from_earth_center())
    print(f"{name} Orbit RTT: {rtt:.4f} seconds")

def run_all_orbits():
    print("Satellite Communication Latency (RTT):\n")
    for name, altitude in ORBIT_CONFIGS.items():
        orbit = Orbit(name, altitude)
        rtt = round_trip_latency(orbit.distance_from_earth_center())
        print(f"{name}: {rtt:.4f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Satellite Communication Latency Simulator"
    )
    parser.add_argument(
        "--orbit",
        choices=ORBIT_CONFIGS.keys(),
        help="Simulate a specific orbit (LEO, MEO, GEO)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Simulate all supported orbits"
    )

    args = parser.parse_args()

    if args.orbit:
        run_single_orbit(args.orbit)
    else:
        run_all_orbits()
