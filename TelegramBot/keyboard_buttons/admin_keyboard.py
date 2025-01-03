from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кол-во пользователей"),
            KeyboardButton(text="Отправить рекламу"),
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Меню админа"
)