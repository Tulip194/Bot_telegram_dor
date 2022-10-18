from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
foradmin = types.ReplyKeyboardMarkup(resize_keyboard=True)
create = types.KeyboardButton('Создать очередь')
view = types.KeyboardButton('Запись в очередь')
help = types.KeyboardButton('Технические проблемы')
foradmin.add(create, view, help)
#####################################################
sotr = types.ReplyKeyboardMarkup(resize_keyboard=True)
queue = types.KeyboardButton('Запись в очередь')
alert = types.KeyboardButton('Помощь')
sotr.add(queue, alert)
#####################################################
newlabqueue = InlineKeyboardMarkup()
newlabqueue.add(InlineKeyboardButton('Встать в начало очереди', callback_data='front'))
newlabqueue.add(InlineKeyboardButton('Встать в конец очереди', callback_data='end'))
#####################################################
sotr = types.ReplyKeyboardMarkup(resize_keyboard=True)
help = types.KeyboardButton('Технические проблемы')
admin = types.KeyboardButton('Проблемы с новой лабой')
sotr.add(help, admin)
#####################################################
otm = InlineKeyboardMarkup()
otm.add(InlineKeyboardButton('Отмена', callback_data='otm'))
