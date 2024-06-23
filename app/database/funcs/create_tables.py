import aiosqlite as sq
from loader import db_path

async def create_tables() -> None:
    async with sq.connect(db_path) as db:
        cur = await db.cursor()
        await cur.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL UNIQUE,
                quizzesIds TEXT
            )
        ''')
        await db.commit()
