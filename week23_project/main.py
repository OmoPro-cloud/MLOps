from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram
import random
import time

app = FastAPI()

#metrics
prediction_counter = Counter('model_predictions_total', 'Total number of predictions', ['model_version', 'prediction_class'])
request_counter = Counter('api_requests_total', 'Total API requests', ['endpoint'])

latency_histogram = Histogram('api_latency_seconds', 'Request latency in seconds', ['endpoint'], buckets=[0.1, 0.2, 0.5, 1.0, 2.0])
confidence_histogram = Histogram('model_confidence_score', 'Confidence score of predictions', buckets=[0.5, 0.7, 0.9, 1.0])

#Instrumentation
Instrumentator().instrument(app).expose(app)

@app.get("/predict")
def predict(request: Request, model_version: str = "v1"):
    start_time = time.time()

    classes = ['cat', 'dog', 'mouse']
    prediction = random.choice(classes)
    confidence = random.uniform(0.5, 1.0)

    #prediction metric
    prediction_counter.labels(model_version=model_version, prediction_class=prediction).inc()

    #confidence metric
    confidence_histogram.observe(confidence)

    #request_count
    request_counter.label(endpoint="/predict").inc()

    #latency tracking
    latency = time.time() - start_time
    latency_histogram.labels(endpoint="/predict").observe(latency)

    return {
        "result": prediction,
        "confidence": confidence,
        "latency": latency
    }