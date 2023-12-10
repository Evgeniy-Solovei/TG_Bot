from aiogram import types


"""Кнопки показывающие названия тортов"""
buttons = [
    [types.InlineKeyboardButton(text='🍰 Эстерхази', callback_data='esterhazy')],
    [types.InlineKeyboardButton(text='🍰 Чёрный лес', callback_data='black_forest')],
    [types.InlineKeyboardButton(text='🍰 Наполеон', callback_data='napoleon')],
]
categories_cakes = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
