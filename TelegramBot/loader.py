from aiogram import Bot, Dispatcher
from data import config
from baza.postgresql import Database



ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS


bot = Bot(token=TOKEN, parse_mode="HTML")

# Initializing dispatcher
dp = Dispatcher(bot=bot)
db = Database()
dp = Dispatcher()