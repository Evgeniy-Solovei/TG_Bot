from aiogram import types, F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import dp

router_sweets = Router()
@router_sweets.callback_query(F.data == 'sweets')
async def list_sweets(callback: types.CallbackQuery):
    """Кнопки показывающие названия конфет"""
    sweets = [
        types.InlineKeyboardButton(text='🍬 Ириски', callback_data='irish'),
        types.InlineKeyboardButton(text='🍬 Трюфель', callback_data='truffle'),
    ]
    builder = InlineKeyboardBuilder()
    for sweet in sweets:
        builder.row(sweet)
    await callback.message.answer("Выбери продукт:", reply_markup=builder.as_markup(resize_keyboard=True))


sweets_info = {
    'irish': {
        'info': 'ℹ️ Информация о продукте',
        'data': '📆 Выбрать дату доставки',
    },
    'Truffle': {
        'info': 'ℹ️ Информация о продукте',
        'data': '📆 Выбрать дату доставки',
    },
}


@dp.callback_query(F.data.in_({'irish', 'Truffle'}))
async def instance_cake(callback: types.CallbackQuery):
    sweet = sweets_info[callback.data]
    buttons = [
        types.InlineKeyboardButton(text=v, callback_data=k)
        for k, v in sweet.items()
    ]
    builder = InlineKeyboardBuilder()
    for button in buttons:
        builder.row(button)
    await callback.message.answer('Выбери пункт', reply_markup=builder.as_markup(resize_keyboard=True))

    @dp.callback_query(F.data == 'info')
    async def instance_info(callback: types.CallbackQuery):
        await callback.message.answer('Информация о продукте для заполнения')

    @dp.callback_query(F.data == 'data')
    async def instance_info(callback: types.CallbackQuery):
        await callback.message.answer('Тут должен быть апи Календаря')
