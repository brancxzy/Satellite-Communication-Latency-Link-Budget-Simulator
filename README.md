# Satellite Communication Latency Simulator

Physics-based simulation of satellite communication latency for LEO, MEO, and GEO orbits.

## Overview
This project models satellite communication delays using signal propagation physics
to compare architectural tradeoffs between different orbital regimes.

## Latency Comparison

| Orbit | Altitude (km) | Approx. RTT (seconds) | Characteristics |
|-----|--------------|----------------------|----------------|
| LEO | 550 | ~0.04 | Low latency, high coverage complexity |
| MEO | 20,200 | ~0.18 | Moderate latency, stable coverage |
| GEO | 35,786 | ~0.48 | High latency, continuous regional coverage |

## Architectural Tradeoffs
- **LEO:** Best for real-time applications but requires many satellites
- **MEO:** Balanced latency and coverage
- **GEO:** Simplest ground architecture but highest latency

## Technologies
- Python
- Physics-based modeling
- Object-oriented design

## Visualization
The project includes a latency comparison plot illustrating the significant
differences in round-trip communication delay between LEO, MEO, and GEO orbits.
