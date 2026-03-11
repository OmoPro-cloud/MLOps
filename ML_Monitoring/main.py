from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram
import random
import time

app = FastAPI()

# Create custom metrics
PREDICTION_COUNTER = Counter('model_predictions_total', 'Total number of predictions', ['model_version', 'class'])
CONFIDENCE_HISTOGRAM = Histogram('model_confidence_score', 'Confidence score of predictions', buckets=[0.5, 0.7, 0.9, 1.0])

# Automatic instrumentation (Latency, Error rates, etc.)
instrumentation = Instrumentator().instrument(app).expose(app)

@app.get("/predict")
def predict(model_version: str = "v1"):
    # Simulate a prediction with random confidence score
    classes = ['cat', 'dog', 'mouse']
    prediction = random.choice(classes)
    confidence = random.uniform(0.5, 1.0)

    
    # Increment the prediction counter with model version and class (for simplicity, using 'positive' class)
    PREDICTION_COUNTER.labels(model_version=model_version, class_=prediction).inc()
    
    # Observe the confidence score in the histogram
    CONFIDENCE_HISTOGRAM.observe(confidence)
    
    return {"result": prediction, "confidence": confidence}