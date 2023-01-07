from config import dp, bot
from aiogram import types
import random


total = 0


@dp.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    print(message)
    await message.reply(f'Hello, {message.from_user.first_name}!')
    print('Start')


@dp.message_handler(commands='candy')
async def candy_start_bot(message: types.Message):
    global total
    total = 150
    print('Candies')
    await message.reply(f'Hello, {message.from_user.first_name}! There are {total} candies. \n You can take from to 28. You win if you grab the last one')

@dp.message_handler()
async def candy_bot(message: types.Message):
    global total
    if message.text.isdigit():
        if total <= 0:
            await message.reply(f'{message.from_user.first_name}, '
                                f'There is no candies left')
        else:
            take = int(message.text)
            print(f'{message.from_user.first_name} took {take}')
            if take < 1 or take > 28 or take > total:
                await message.reply(f'{message.from_user.first_name}, dont be a cheat!')
            else:
                total -= take
                if total == 0:
                    await message.reply(f'{message.from_user.first_name}, '
                                    f'took {take} candies, there are {total} left.')

                else:
                    await message.reply(f'{message.from_user.first_name}, '
                                        f'took {take} candies, there are {total} left')
                    bot_take = 0
                    if total < 29:
                        bot_take = total
                    else:
                        bot_take = random.randint(1, 28)
                    total -= bot_take
                    if total == 0:
                        await message.answer(f'I took {bot_take} candies, there are {total} left.')
                        await message.answer('Bot wins')
                    else:
                        await message.answer(f'I took {bot_take} candies, there are {total} left.')
    else:
        await message.reply(f'{message.from_user.first_name}, please use numbers')


@dp.message_handler()
async def all_bot(message: types.Message):
    print(message)
    print('All')
    await message.reply(f'{message.from_user.first_name}, lets play candies game, please type /candy')