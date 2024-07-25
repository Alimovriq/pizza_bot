from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

DESCRIPTION = 'Я виртуальный помощник, бот для учебного проекта'


# Реагирует на комманду /start
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer(
        'Привет, я виртуальный помощник', reply_markup=reply.start_kb)


# Меню
@user_private_router.message(or_f(Command('menu'), F.text.lower() == 'меню'))
async def menu_cmd(message: types.Message) -> None:
    await message.answer('Вот меню:')


# Описание
@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message) -> None:
    await message.answer(f'Описание: {DESCRIPTION}')


# Оплата
@user_private_router.message(F.text.lower() == 'варианты оплаты')
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message) -> None:
    await message.answer('Варианты оплаты:')


# Доставка
@user_private_router.message(
    (F.text.lower().contains(
        'доставк') | (F.text.lower() == 'варианты доставки')))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message) -> None:
    await message.answer('Варианты доставки:')
