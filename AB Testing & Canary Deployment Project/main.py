from fastapi import FastAPI
from router import recommend_router

app = FastAPI(title="Recommendation Service")

# include router
app.include_router(recommend_router)