import aiosqlite as sq
from loader import db_path


async def checkRegister(userId: str) -> bool:
    try:
        async with sq.connect(db_path) as db:
            cur = await db.cursor()
            await cur.execute("SELECT user_id FROM Users WHERE user_id = ?", (userId,))
            user_id = await cur.fetchone()
            if user_id:
                return True
            else:
                return False
    except sq.Error as e:
        print(f'Error: {e}')