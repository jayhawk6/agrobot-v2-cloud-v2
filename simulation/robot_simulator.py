# simulation/robot_simulator.py
import time
import random
import json
from pathlib import Path

OUT_FILE = Path(__file__).resolve().parents[1] / "backend" / "data" / "sensor_data.json"
FARM_FILE = Path(__file__).resolve().parents[1] / "backend" / "data" / "farm_zones.json"

ROBOT_ID = "AGB-01"

def pick_random_zone(zones):
    return random.choice(list(zones.keys()))

def generate_sensor_payload(zone_id, zones):
    zone = zones[zone_id]
    payload = {
        "robot_id": ROBOT_ID,
        "zone_id": zone_id,
        "gps": [zone["x"], zone["y"]],
        "soil_moisture": zone["soil_moisture"] + random.uniform(-1,1),
        "temperature": zone["temperature"] + random.uniform(-0.3,0.3),
        "humidity": zone["humidity"] + random.uniform(-1,1),
        "battery_level": round(random.uniform(60, 100), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return payload

def run_simulator(interval=5):
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    while True:
        # read farm zones
        try:
            with open(FARM_FILE) as f:
                farm = json.load(f)
                zones = farm.get("zones", {})
        except Exception:
            zones = {"A1": {"x": 0, "y": 0, "soil_moisture": 50, "temperature": 25, "humidity": 60}}
        zone_id = pick_random_zone(zones)
        payload = generate_sensor_payload(zone_id, zones)
        with open(OUT_FILE, "w") as f:
            json.dump(payload, f, indent=2)
        print("Telemetry written:", payload)
        time.sleep(interval)

if __name__ == "__main__":
    run_simulator()
