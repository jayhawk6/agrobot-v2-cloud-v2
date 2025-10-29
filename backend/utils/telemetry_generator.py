import json, random, time
from pathlib import Path

FLEET_FILE = Path("backend/data/fleet_data.json")

def generate_fleet_data():
    fleet = []
    for i in range(1, 21):
        fleet.append({
            "robot_id": f"AGB-{i:02d}",
            "zone_id": f"Z{i%5 + 1}",
            "gps": [round(random.uniform(-1.0, 1.0), 6), round(random.uniform(34.0, 36.0), 6)],
            "soil_moisture": round(random.uniform(20, 90), 2),
            "temperature": round(random.uniform(18, 38), 2),
            "humidity": round(random.uniform(40, 90), 2),
            "battery_level": round(random.uniform(10, 100), 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

    FLEET_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(FLEET_FILE, "w") as f:
        json.dump(fleet, f, indent=2)
    return fleet
