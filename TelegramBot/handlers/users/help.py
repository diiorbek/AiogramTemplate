from aiogram.types import Message
from loader import dp
from aiogram.filters import Command


#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("Какая вам нужна помощь?")
