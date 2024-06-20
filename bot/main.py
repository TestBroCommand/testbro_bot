import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from app.database.funcs.create_tables import create_tables
from loader import dp, bot
from app.handlers.quiz_link import router

async def main() -> None:
    try:
        await create_tables()
        dp.include_router(router)
        await dp.start_polling(bot)
    except Exception as ex:
        logging.error(ex)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
