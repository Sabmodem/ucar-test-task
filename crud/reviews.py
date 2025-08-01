from aiosqlite import Connection
from typing import Optional
from models.reviews import Review, Sentiment

async def create_review(
    review: Review,
    db: Connection
):
    cursor = await db.execute(
        "INSERT INTO reviews (text, sentiment, created_at) VALUES (?,?,?) RETURNING *",
        [review.text, review.sentiment.value, review.created_at],
    )

    result = await cursor.fetchone()
    return Review(**result)

async def get_reviews(
    db: Connection,
    sentiment: Optional[Sentiment] = None
):
    query = "SELECT * FROM REVIEWS"

    if sentiment:
        query += f" WHERE sentiment = ?"
  
    cursor = await db.execute(query, [sentiment.value] if sentiment else [])
    rows = await cursor.fetchall()
    return [Review(**row) for row in rows]