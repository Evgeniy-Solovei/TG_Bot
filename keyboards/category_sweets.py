from aiogram import types


"""Кнопки показывающие названия конфет"""
buttons = [
    [types.InlineKeyboardButton(text='🍬 Ириски', callback_data='irish')],
    [types.InlineKeyboardButton(text='🍬 Трюфель', callback_data='truffle')],
]
categories_sweets = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)

