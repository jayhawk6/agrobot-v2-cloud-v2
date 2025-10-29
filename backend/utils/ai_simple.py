import random

def analyze_telemetry(telemetry_list):
    """Analyze telemetry for multiple robots and return AI advice per robot."""
    advice_list = []

    for data in telemetry_list:
        robot_id = data.get("robot_id", "Unknown")
        soil = data.get("soil_moisture", 50)
        temp = data.get("temperature", 25)
        battery = data.get("battery_level", 90)

        # Simple rule-based logic
        if soil < 30:
            action = "Irrigate crop area immediately."
        elif soil > 80:
            action = "Stop irrigation, soil too wet."
        elif battery < 20:
            action = "Return to charging station."
        elif temp > 35:
            action = "Activate cooling or pause daytime activity."
        else:
            action = "All systems optimal."

        advice_list.append({
            "robot_id": robot_id,
            "status": "Analyzed",
            "advice": action
        })

    return {"fleet_analysis": advice_list}
