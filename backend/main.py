from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import random
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 15 Agrobots
robots = [
    {
        "robot_id": f"AG-{i+1:02d}",
        "x": random.randint(50, 750),
        "y": random.randint(50, 350),
        "battery": random.randint(50, 100),
        "task": "Idle",
    }
    for i in range(15)
]

# Charging stations
stations = [(50, 50), (700, 50), (50, 350), (700, 350)]

# Obstacles
obstacles = [{"x":200, "y":150}, {"x":400, "y":300}, {"x":600, "y":200}]

# Tasks
tasks = ["Fertilize", "Water", "Soil Check"]

# Weather states: sun, clouds, rain
weather_state = "sun"

async def simulate_robots():
    global weather_state
    while True:
        # Randomly change weather every 60 ticks (~30s)
        if random.randint(0, 59) == 0:
            weather_state = random.choice(["sun", "clouds", "rain"])

        for robot in robots:
            # Battery drain
            robot["battery"] -= random.randint(0, 3)
            if robot["battery"] <= 0:
                robot["battery"] = 0
                robot["task"] = "Inactive"

            # Low battery → go to nearest station
            if robot["battery"] < 20 and robot["task"] != "Inactive":
                robot["task"] = "Charging"
                sx, sy = min(stations, key=lambda s: (s[0]-robot["x"])**2 + (s[1]-robot["y"])**2)
                dx, dy = sx - robot["x"], sy - robot["y"]
                step = 10
                distance = (dx**2 + dy**2)**0.5
                if distance > step:
                    robot["x"] += dx / distance * step
                    robot["y"] += dy / distance * step
                else:
                    robot["x"], robot["y"] = sx, sy
            else:
                # Random patrol
                robot["x"] += random.randint(-5, 5)
                robot["y"] += random.randint(-5, 5)

                # Assign task if idle
                if robot["task"] == "Idle":
                    robot["task"] = random.choice(tasks)

            # Obstacle avoidance
            for obs in obstacles:
                if abs(robot["x"] - obs["x"]) < 30 and abs(robot["y"] - obs["y"]) < 30:
                    robot["x"] += random.choice([-15, 15])
                    robot["y"] += random.choice([-15, 15])

            # Keep robots inside farm boundaries
            robot["x"] = max(0, min(760, robot["x"]))
            robot["y"] = max(0, min(360, robot["y"]))

        await asyncio.sleep(0.5)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(simulate_robots())

@app.websocket("/ws/telemetry")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        await ws.send_json({
            "robots": robots,
            "obstacles": obstacles,
            "stations": stations,
            "weather": weather_state
        })
        await asyncio.sleep(0.5)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
