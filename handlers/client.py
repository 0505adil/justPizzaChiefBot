from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного Аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Напишите боту в ЛС \nhttps://t.me/just_pizza_chief_bot')


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_time(message: types.Message):
    await bot.send_message(message.from_user.id, 'Когда хотим тогда и работаем')


# @dp.message_handler(commands=['Location'])
async def pizza_location(message: types.Message):
    await bot.send_message(message.from_user.id, 'Там где счастье', reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_time, commands=['work_time'])
    dp.register_message_handler(pizza_location, commands=['location'])
