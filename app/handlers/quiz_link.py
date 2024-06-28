from aiogram import html, types, F, Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup,  InputFile, FSInputFile
from aiogram.filters import Command, CommandObject,CommandStart
from app.database.funcs import add_navigation_quiz, add_user, check_register
from aiogram.utils.deep_linking import decode_payload
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()



@router.message(Command('start'))
async def send_welcome(message: types.Message, command: CommandObject):
    userId = message.from_user.id
    nachat_file_path = 'assets/images/nachat.png'
    isRegister = await check_register.checkRegister(userId)
    args = command.args
    if isRegister:
        if args:
            builder = InlineKeyboardMarkup(
                    inline_keyboard=[[InlineKeyboardButton(text="Запустить QuizBro🔥!", url=f"https://t.me/testquizebro_bot/base")]]
            )
            await message.reply_photo(
            photo=FSInputFile(nachat_file_path),
            caption='''Тест у меня! 
Лови ссылку и проходи его!''',
                    reply_markup=builder
            )
            await add_navigation_quiz.addQuizId(userId, args)  
        else:
            start_file_path = 'assets/images/bolshe.png'
            builder = InlineKeyboardMarkup(
                    inline_keyboard=[[InlineKeyboardButton(text="Запустить QuizBro🔥!", url=f"https://t.me/testquizebro_bot/base")]]
                )
            await message.reply_photo(
                    photo=FSInputFile(start_file_path),
                    caption='''Я вижу ты хочешь проходить тесты!
Тогда вот твоя персональная ссылка и скорее погружайся в этот удивительный мир!''',
                    reply_markup=builder,
                    parse_mode="HTML"
                )
    else:
        if args:
            args = command.args
            builder = InlineKeyboardMarkup(
                    inline_keyboard=[[InlineKeyboardButton(text="Запустить QuizBro🔥!", url=f"https://t.me/testquizebro_bot/base")]]
            )
            await message.reply_photo(
            photo=FSInputFile(nachat_file_path),
            caption='''Тест у меня! 
Лови ссылку и проходи его!''',
                    reply_markup=builder
            )
            await add_user.register(userId)
            await add_navigation_quiz.addQuizId(userId, args)  
        else:
            start_file_path = 'assets/images/bolshe.png'
            builder = InlineKeyboardMarkup(
                    inline_keyboard=[[InlineKeyboardButton(text="Запустить QuizBro🔥!", url=f"https://t.me/testquizebro_bot/base")]]
                )
            await message.reply_photo(
                    photo=FSInputFile(start_file_path),
                    caption='''Привет! Всеми нами любимые тесты теперь доступны в телеграм!
Начинай скорее проходить  и обязательно напиши, понравилось ли тебе. 
Нам будет очень приятно услышать твое мнение. 
Попробуй прямо сейчас и убедись сам!
<tg-spoiler> Наш блог с разработкой - @testbroblog </tg-spoiler>
    ''',
                    reply_markup=builder,
                    parse_mode="HTML"
                )
            await add_user.register(userId)



