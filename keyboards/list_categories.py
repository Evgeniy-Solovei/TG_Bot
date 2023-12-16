from aiogram import types


"""Инлайн кнопки с категориями товаров прикрепляются к сообщению"""
buttons = [
    [types.InlineKeyboardButton(text='🎂 Торты', callback_data='cakes')],
    [types.InlineKeyboardButton(text='🦄 Маршмеллоу', callback_data='marshmallow')],
    [types.InlineKeyboardButton(text='🌷 Зефирные цветы', callback_data='flowers')],
    [types.InlineKeyboardButton(text='🥮 Тарталетки', callback_data='tartlets')],
    [types.InlineKeyboardButton(text='🍬 Конфеты', callback_data='sweets')]
]

list_categories = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
