import aiosqlite

async def get_db():
    async with aiosqlite.connect('reviews.db') as db:
        db.row_factory = aiosqlite.Row
        yield db