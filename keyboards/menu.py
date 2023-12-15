from aiogram import types


buttons = [
    [types.KeyboardButton(text='Главное меню')],
    [types.KeyboardButton(text='Хотите узнать погоду ?')],
    [types.KeyboardButton(text='Instagram')],

]
menu_keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True)
