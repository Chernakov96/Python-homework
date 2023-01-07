from aiogram.utils import executor
from config import dp
import handlers
from random import randint
import commands
from aiogram import types


async def bot_start(_):
    print('Bot is up')

handlers.registred_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start)