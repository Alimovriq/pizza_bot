from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter

from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

DESCRIPTION = 'Я виртуальный помощник, бот для учебного проекта'


# Реагирует на комманду /start
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer(
        'Привет, я виртуальный помощник',
        reply_markup=reply.start_kb3.as_markup(
            resize_keyboard=True,
            input_field_placeholder='Что Вас интересует?'
        ))
    # await message.answer(
    #     'Тестовая клава с локацией и телефоном',
    #     reply_markup=reply.test_kb
    # )


# Меню
@user_private_router.message(or_f(Command('menu'), F.text.lower() == 'меню'))
async def menu_cmd(message: types.Message) -> None:
    await message.answer('Вот меню:', reply_markup=reply.del_kbd)


# Описание
@user_private_router.message(F.text.lower() == 'о магазине')
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message) -> None:
    await message.answer(f'Описание: {DESCRIPTION}')


# Оплата
@user_private_router.message(F.text.lower() == 'варианты оплаты')
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message) -> None:
    text = as_marked_section(
        Bold('Варианты оплаты:'),
        'Картой в боте',
        'При получении карта/кеш',
        'В заведении',
        marker='✅ '
    )
    await message.answer(text.as_html())


# Доставка
@user_private_router.message(
    (F.text.lower().contains(
        'доставк') | (F.text.lower() == 'варианты доставки')))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message) -> None:
    text = as_list(
        as_marked_section(
            Bold('Варинты доставки/заказа:'),
            'Курьер',
            'Самовывоз (сейчас прибегу и заберу)',
            'Покушаю у Вас (сейчас прибегу)',
            marker='✅ '),
        as_marked_section(
            Bold('Нельзя:'),
            'Почта',
            'Голуби',
            marker='❌'),
        sep='\n--------------------------------------\n'
        )
    await message.answer(text.as_html())


# Телефонный номер
@user_private_router.message(F.contact)
async def get_contact(message: types.Message) -> None:
    await message.answer('Ваш номер получен')
    await message.answer(str(message.contact))


# Местоположение
@user_private_router.message(F.location)
async def get_location(message: types.Message) -> None:
    await message.answer('Ваша локация получена')
    await message.answer(str(message.location))
