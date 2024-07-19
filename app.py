import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


# Реагирует на комманду /start
@dp.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer('Это была команда /start')


# Эхо
@dp.message()
async def echo(message: types.Message) -> None:
    # text = message.text

    # if text in ['Привет', 'привет', 'hi', 'hello']:
    #     await message.answer('И тебе привет!')
    # elif text in ['Пока', 'пока', 'пакеда', 'До свидания']:
    #     await message.answer('И тебе пока!')
    # else:
    #     await message.answer(message.text)

    await message.answer(message.text)


async def main() -> None:
    await dp.start_polling(bot)

asyncio.run(main())
