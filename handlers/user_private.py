from aiogram import types, Router
from aiogram.filters import CommandStart, Command


user_private_router = Router()

DESCRIPTION = 'Я виртуальный помощник, бот для учебного проекта'


# Реагирует на комманду /start
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer('Привет, я виртуальный помощник')


# Меню
@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message) -> None:
    await message.answer('Вот меню:')


# Описание
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message) -> None:
    await message.answer(f'Описание: {DESCRIPTION}')
