from config import dp
from aiogram import types


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    print(message.text)
    await message.answer('Hello! To use the bot type "/image" and your search result to generate google images link')


@dp.message_handler(commands='image')
async def input_image(message: types.Message):
    msg = message.text.split()
    image = 'https://www.google.co.in/search?q=' + msg[1] +'&source=lnms&tbm=isch'
    await message.answer(image)
