from fastapi import APIRouter, Depends
from aiosqlite import Connection
from typing import List, Optional

from models import reviews as review_models
from services import reviews as review_service
from crud import reviews as review_crud
from database import get_db

router = APIRouter()

@router.post("/reviews", response_model=review_models.Review)
async def create_review_handler(
    review_create: review_models.ReviewCreate,
    db: Connection = Depends(get_db)
):
    try:
        review = review_service.create_review(review_create)
        return await review_crud.create_review(review, db)
    except Exception as e:
        await db.rollback()
    finally:
        await db.commit()

@router.get("/reviews", response_model=List[review_models.Review])
async def get_review_handler(
    db: Connection = Depends(get_db),
    sentiment: Optional[review_models.Sentiment] = None
):
    return await review_crud.get_reviews(db, sentiment)