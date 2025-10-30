from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .ai_infer import router as ai_router

app = FastAPI(title="Agrobot V2 Cloud Simulator", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_router)

@app.get("/")
def root():
    return {"message": "Agrobot V2 Cloud Simulator API - Fleet Ready"}
