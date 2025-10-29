#!/bin/bash

# Start FastAPI backend in the background
uvicorn main:app --reload &

# Wait a bit for backend to start
sleep 2

# Serve frontend via Python HTTP server
cd frontend
python3 -m http.server 8080
