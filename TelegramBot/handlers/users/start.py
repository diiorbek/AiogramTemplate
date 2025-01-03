from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    username = message.from_user.username
    db.add_user(full_name=full_name,telegram_id=telegram_id, telegram_username=username)
    await message.answer(text="Здравствуйте, добро пожаловать!")
