import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from app.database.funcs.create_tables import create_tables
from loader import dp, bot
from app.handlers import info, quiz_link

async def main() -> None:
    try:
        await create_tables()
        dp.include_routers(info.router, quiz_link.router)
        await dp.start_polling(bot)
    except Exception as ex:
        logging.error(ex)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
