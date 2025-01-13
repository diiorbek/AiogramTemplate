from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Создатель: <a href='https://github.com/diiorbek'>Diyorbek</a>")
