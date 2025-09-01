# syntax=docker/dockerfile:1
FROM python:3.10-slim AS base

#system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates && \
    rm -rf /var/lib//apt/lists/*

#prevent tf from writing long logs
ENV TF_CPP_MIN_LOG_LEVEL=2 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .

#install python deps (no cache to keep layer smallish)
RUN pip install --no-cache-dir -r requirements.txt

#predownload keras weight into the image layer
RUN python - <<"PY"
from tenserflow.keras.applications import MobileNetV2
MobileNetV2(weights="imagenet")
print("Keras weight cached")

#copy app
COPY app.py ./

#create a non root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

#expose some ports and use gunicorn to set entry point
CMD ["gunicorn", "-w", "2", "-k", "gthread", "-b", "0.0.0.0:9000", "app:app"]