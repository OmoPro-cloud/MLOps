from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram
import random
import time

app = FastAPI()

#gather metrics
request_counter = Counter("api_requests_total", "Total API requests", ["endpoint"])
prediction_counter = Counter("model_predictions_total", "Total number of predictions", ["model_version", "prediction_class"])
request_latency_histogram = Histogram("api_latency_seconds", "Request Latency In Seconds", ["endpoint"])
confidence_histogram = Histogram("model_confidence_score", "Confidence score of predictions", buckets=[0.5, 0.7, 0.9, 1.0])

#instrumentator automatically tracks request count, latency, error rate and /metrics endpoint
instrumentation = Instrumentator().instrument(app).expose(app)

#setup /predict endpoint and model
@app.get("/predict")
def predict(model_version: str = "v1"):
    start_time = time.time() #records when the requests start

    #simulate prediction
    classes = ["cat", "dog", "mouse"]
    prediction = random.choice(classes)
    confidence = random.uniform(0.5, 1.0)

    #increment metrics
    request_counter.labels(endpoint="/predict").inc()
    prediction_counter.labels(model_version=model_version, prediction_class=prediction).inc()
    confidence_histogram.observe(confidence)

    #record latency
    elapsed = time.time() - start_time
    request_latency_histogram.labels(endpoint="/predict").observe(elapsed)

    #return prediction

    return {
        "result": prediction,
        "confidence": confidence,
        "latency_seconds": elapsed
    }