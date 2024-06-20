import aiosqlite as sq
from loader import db_path


async def register(userId: str) -> None:
    try:
        async with sq.connect(db_path) as db:
            cur = await db.cursor()
            await cur.execute("SELECT user_id FROM Users WHERE user_id = ?", (userId,))
            user_id = await cur.fetchone()
            if user_id:
                pass
            else:
                await cur.execute("INSERT INTO Users (user_id, quizzesIds) VALUES (?, ?)", (userId, ""))
                await db.commit()
    except sq.Error as e:
        print(f'Error: {e}')