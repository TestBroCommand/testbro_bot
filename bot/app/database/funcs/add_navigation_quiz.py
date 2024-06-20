import aiosqlite as sq
from loader import db_path
from app.database.funcs.add_user import register

async def addQuizId(userId: str, quizId: str):
    try:
        async with sq.connect(db_path) as db:
            cur = await db.cursor()
            await cur.execute("SELECT quizzesIds FROM Users WHERE user_id = ?", (userId,))
            result = await cur.fetchone()

            if result:
                current_quizzes = result[0]
                if current_quizzes:
                    new_quizzes = f"{current_quizzes}, {quizId}"
                else:
                    new_quizzes = quizId
                await cur.execute("UPDATE Users SET quizzesIds = ? WHERE user_id = ?", (new_quizzes, userId))
            else:
                await register(userId)
                new_quizzes = quizId
                await cur.execute("UPDATE Users SET quizzesIds = ? WHERE user_id = ?", (new_quizzes, userId))
                
            await db.commit()
            
    except sq.Error as e:
        print(f'Error: {e}')
