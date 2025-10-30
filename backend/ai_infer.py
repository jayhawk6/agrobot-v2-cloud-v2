from pydantic import BaseModel
from fastapi import APIRouter
import joblib
import numpy as np
import os

router = APIRouter(prefix="/ai", tags=["AI"])

MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "demo_model.joblib")

class AIRequest(BaseModel):
    soil_moisture: float
    temperature: float

model = None

@router.on_event("startup")
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
    else:
        print(f"⚠️ Model not found at {MODEL_PATH}, using mock predictions.")
        model = None

@router.post("/infer")
def ai_infer(data: AIRequest):
    if model:
        X = np.array([[data.soil_moisture, data.temperature]])
        pred = model.predict(X)[0]
        return {"prediction": pred}
    else:
        # fallback mock inference
        if data.soil_moisture < 30:
            return {"prediction": "Water the plant"}
        elif data.temperature > 35:
            return {"prediction": "High temperature alert"}
        else:
            return {"prediction": "All conditions normal"}
