from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram
import random
import time

app = FastAPI()

#gather metrics 
REQUEST_COUNTER = Counter("api_requests_total", "Total API requests", ["endpoint"])
PREDICTION_COUNTER = Counter("model_predictions_total", "Total number of predictions", ["model_version", "prediction_class"])
REQUEST_LATENCY_HISTOGRAM = Histogram("api_latency_seconds", "Request latency in seconds", ["endpoint"])
CONFIDENCE_HISTOGRAM = Histogram("model_confidence_score", "Confidence score of predictions", buckets=[0.5, 0.7, 0.9, 1.0])

#instrumentator automatically tracks request count, latency, error rate and /metrics endpoint
instrumentation = Instrumentator().instrument(app).expose(app)

#setup /predict endpoint and model
@app.get("/predict")
def predict(model_version: str = "v1"):
    start_time = time.time()  # Record request start

    #Simulate prediction
    classes = ["cat", "dog", "mouse"]
    prediction = random.choice(classes)
    confidence = random.uniform(0.5, 1.0)

    #Increment metrics
    REQUEST_COUNTER.labels(endpoint="/predict").inc()
    PREDICTION_COUNTER.labels(model_version=model_version, prediction_class=prediction).inc()
    CONFIDENCE_HISTOGRAM.observe(confidence)

    # Record latency
    elapsed = time.time() - start_time
    REQUEST_LATENCY_HISTOGRAM.labels(endpoint="/predict").observe(elapsed)

    #Return prediction

    return {
        "result": prediction,
        "confidence": confidence,
        "latency_seconds": elapsed
    }



















''' from fastapi import FastAPI, Request
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
    request_counter.labels(endpoint="/predict").inc()

    #latency tracking
    latency = time.time() - start_time
    latency_histogram.labels(endpoint="/predict").observe(latency)

    return {
        "result": prediction,
        "confidence": confidence,
        "latency": latency
    }
    '''