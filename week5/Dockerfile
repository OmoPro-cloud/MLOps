# syntax=docker/dockerfile:1
FROM python:3.10-slim AS base

# system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Prevent TF from writing huge logs
ENV TF_CPP_MIN_LOG_LEVEL=2 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .

# Install Python deps (no cache to keep layer smallish)
RUN pip install --no-cache-dir -r requirements.txt

#Pre-download Keras weight into the image layer (so first run is fast/offline)
RUN python - <<'PY'
from tensorflow.keras.applications import MobileNetV2
MobileNetV2(weights='imagenet')
print("Keras weights cached")
PY

# Copy app
COPY app.py ./

# Create a non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose some ports and set entrypoint (Gunicorn)
EXPOSE 8080
CMD ["gunicorn", "-w", "2", "-k", "gthread", "-b", "0.0.0.0:8080", "app:app"]