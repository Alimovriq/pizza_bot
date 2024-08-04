from aiogram import F, Router, types
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter, IsAdmin
from kbds.reply import get_keyboard


admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private'], IsAdmin()))


ADMIN_KB = get_keyboard(
    'Добавить товар',
    'Изменить товар',
    'Удалить товар',
    'Я так, просто посмотреть зашел',
    placeholder='Выбрать действие',
    sizes=(2, 1, 1,)
)


@admin_router.message(Command('admin'))
async def add_product(message: types.Message):
    await message.answer('Что Вы хотите сделать?', reply_markup=ADMIN_KB)


@admin_router.message(F.text == 'Я так, просто посмотреть зашел')
async def starring_at_product(message: types.Message):
    await message.answer('ОК, вот список товаров')


@admin_router.message(F.text == 'Изменить товар')
async def change_product(message: types.Message):
    await message.answer('ОК, вот список товаров для изменений')


@admin_router.message(F.text == 'Удалить товар')
async def delete_product(message: types.Message):
    await message.answer('Выберите товар(ы) для удаления')
