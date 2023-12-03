from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def start_list_categories(message: types.Message):
    """Инлайн кнопки с категориями товаров прикрепляются к сообщению"""
    buttons = [

        [
            types.InlineKeyboardButton(text='🎂 Торты', callback_data='cakes')
        ],
        [
            types.InlineKeyboardButton(text='🦄 Маршмеллоу', callback_data='marshmallow')
        ],
        [
            types.InlineKeyboardButton(text='🌷 Зефирные цветы', callback_data='flowers')
        ],
        [
            types.InlineKeyboardButton(text='🥮 Тарталетки', callback_data='tartlets')
        ],
        [
            types.InlineKeyboardButton(text='🍬 Конфеты', callback_data='sweets')
        ]

    ]

    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    await message.answer("Выбери продукт:", reply_markup=reply_markup)

# """Простые кнопки которые крепятся снизу"""
# async def start_list_categories(message: types.Message):
#     buttons = ['🎂 Торты', '🦄 Маршмеллоу', '🌷 Зефирные цветы', '🥮 Тарталетки', '🍬 Конфеты']
#     builder = ReplyKeyboardBuilder()
#     for button in buttons:
#         builder.add(types.KeyboardButton(text=str(button)))
#     builder.adjust(4)
#     await message.answer("Выбери продукт:", reply_markup=builder.as_markup(resize_keyboard=True))
