# backend/ai_stub.py

import random

class AgrobotAI:
    """
    Placeholder AI module simulating intelligent Agrobot decisions.
    Will later be replaced by real ML/AI models.
    """

    def __init__(self):
        self.status = "initialized"

    def analyze_environment(self, data):
        # Fake analysis logic — just random responses for now
        soil_quality = random.choice(["Good", "Moderate", "Poor"])
        plant_health = random.choice(["Healthy", "Stressed", "Diseased"])
        suggestion = random.choice([
            "Increase water supply.",
            "Add nitrogen fertilizer.",
            "Reduce pesticide use.",
            "All systems optimal."
        ])

        return {
            "soil_quality": soil_quality,
            "plant_health": plant_health,
            "recommendation": suggestion
        }


# Instance of the AI
ai_stub = AgrobotAI()
