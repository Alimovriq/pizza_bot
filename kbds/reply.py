from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='О магазине'),
            KeyboardButton(text='Варианты доставки'),
            KeyboardButton(text='Варинты оплаты'),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?'
)
