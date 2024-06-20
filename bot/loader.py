import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties



dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'app', 'utils', '.env'))
load_dotenv(dotenv_path)

db_path = os.getenv('db_path')

bot = Bot(token = os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode='html'))
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)
