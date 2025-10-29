from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Agrobot V2 Cloud Simulation API - Fleet Ready")

# Path to the frontend directory
frontend_dir = os.path.join(os.path.dirname(__file__), "../frontend")

# Serve frontend files
app.mount("/frontend", StaticFiles(directory=frontend_dir), name="frontend")

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h2>🌾 Agrobot V2 Cloud Simulation API - Fleet Ready</h2>"

@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard():
    dashboard_path = os.path.join(frontend_dir, "dashboard.html")
    with open(dashboard_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)
