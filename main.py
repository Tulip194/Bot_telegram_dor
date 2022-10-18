from aiogram import Bot, types, asyncio, Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, Message
from aiogram.utils.markdown import hlink
import logging
import config
import keyboard
import sqlite3 as sql
from states import *
import func
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
storage=MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
admin=951378262
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@dp.message_handler(commands=['start'], state = None)
async def start(message):
    info = func.user(message.chat.id)
    if info is None:
        con = sql.connect("users.db")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, login TEXT, Nick TEXT, stat INT, message TEXT)")
            cur.execute(f"INSERT OR IGNORE INTO `users` VALUES (?, ?, ?, ?, ?)",(message.chat.id, message.from_user.username, message.from_user.first_name, 0, 0))
            con.commit()

    elif (str(info[0]) == str(config.admin)):
            await message.answer(f"Добро пожаловать {message.from_user.first_name}",reply_markup=keyboard.sotr)
    else:
        await message.answer(f"Добро жопаловать {message.from_user.first_name}",reply_markup=keyboard.startuser9)


@dp.message_handler(content_types=['text'])
async def get_message(message, state: FSMContext):
    info = func.user(message.chat.id)
    if info is not None:
        if message.text =='Создать очередь':
            if (str(info[0]) == str(config.admin)):
                await change.Q1.set()
                await message.answer('Введите предмет, номер лабы , также дату(всё через "-")', reply_markup = keyboard.otm, parse_mode='Markdown')
            else:
                await message.answer('Куда лезем')
        elif message.text =='Запись в очередь':
            pass

@dp.callback_query_handler(text_contains='otm',state='*')
async def otm(call: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'OK')


@dp.message_handler(state=change.Q1)
async def c(message, state: FSMContext):
    if 'Отменить' == message.text:
        await state.finish()
        await message.answer('Главная', reply_markup=keyboard.foradmin,  parse_mode='Markdown')
        return
    async with state.proxy() as data:
        data['Q1'] = message.text
    async with state.proxy() as data:
        Q1 = data.get("Q1")
        func.safemessage(config.admin,Q1)
        await message.answer('Изменение сохранено', reply_markup=keyboard.sotr)
        await state.finish()

@dp.callback_query_handler(text_contains='cancle')
async def cancle(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard.sotr, parse_mode='Markdown')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
executor.start_polling(dp, skip_updates=(True))
