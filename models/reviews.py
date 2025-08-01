from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class Sentiment(Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"

class Review(BaseModel):
    id: Optional[int] = None
    text: str
    sentiment: Sentiment
    created_at: datetime = Field(default_factory=datetime.now)

class ReviewCreate(BaseModel):
    text: str