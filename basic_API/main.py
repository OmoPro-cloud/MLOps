#this is the main entry point of the API
from fastapi import FastAPI
from routers import v1, v2

app = FastAPI(
    title="Recommendation API",
    description="API with Authentication and Versioning",
    version="2.0"
)

app.include_router(v1.router)
app.include_router(v2.router)