from aiogram import html, types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject,CommandStart
from app.database.funcs import add_navigation_quiz, add_user
from aiogram.utils.deep_linking import decode_payload

router = Router()


@router.message(Command('start'))
async def send_welcome(message: types.Message, command: CommandObject):
    args = command.args
    if args:
        await message.reply(f'''Привет! Ты зашел в наш проект TestBro!
Твоя персональная ссылка на тест: https://t.me/testquizebro_bot/base?startapp={args}.
Приятного прохождения!''')
        await add_navigation_quiz.addQuizId(message.from_user.id, args)
    else:
        await message.reply("Hello! You started me without any argument.")
        await add_user.register(message.from_user.id)


