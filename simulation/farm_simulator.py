# simulation/farm_simulator.py
import random
import json
import time
from pathlib import Path

OUT_PATH = Path(__file__).resolve().parents[1] / "backend" / "data" / "farm_zones.json"

def init_farm(width=4, height=4):
    zones = {}
    for x in range(width):
        for y in range(height):
            zone_id = f"{chr(65+x)}{y+1}"  # A1, A2...
            zones[zone_id] = {
                "id": zone_id,
                "x": x,
                "y": y,
                "crop": "tomato",
                "soil_moisture": round(random.uniform(30, 80), 2),
                "temperature": round(random.uniform(18, 30), 2),
                "humidity": round(random.uniform(40, 80), 2),
                "needs_fertilizer": False
            }
    return zones

def update_zone(zone):
    # small random walk for climate and moisture
    zone["soil_moisture"] = max(5, min(100, zone["soil_moisture"] + random.uniform(-3, 3)))
    zone["temperature"] = max(-10, min(50, zone["temperature"] + random.uniform(-0.5, 0.5)))
    zone["humidity"] = max(0, min(100, zone["humidity"] + random.uniform(-1.5, 1.5)))
    # rule-based need detection (simple)
    zone["needs_fertilizer"] = zone["soil_moisture"] < 40 and zone["temperature"] > 20
    return zone

def run_farm_loop(interval=5):
    zones = init_farm()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    while True:
        for zid in zones:
            zones[zid] = update_zone(zones[zid])
        with open(OUT_PATH, "w") as f:
            json.dump({"zones": zones, "updated": time.time()}, f, indent=2)
        print("Farm updated")
        time.sleep(interval)

if __name__ == "__main__":
    run_farm_loop()
