#!/bin/bash

# --- API BACKEND (UVICORN) Config ---

echo "Starting Uvicorn API Backend on port 5050..."

uvicorn app.main:app --host 0.0.0.0 --port 5050 &


echo "Waiting 10 seconds for API to initialize..."
sleep 10

# --- FRONTEND (GRADIO) ---

echo "Starting Gradio Frontend..."

# This command will run in the foreground
# and keep the container/Space from exiting.
python -m app.frontend.gradio_ui

# If your Gradio is launched with launch(server_port=7860),
# this command will occupy the Terminal and keep the app running.