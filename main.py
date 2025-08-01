from routes.reviews import router as review_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(review_router)