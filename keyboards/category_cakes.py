from aiogram import types, F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import dp

router_cakes = Router()


@router_cakes.callback_query(F.data == 'cakes')
async def list_cakes(callback: types.CallbackQuery):
    """Кнопки показывающие названия тортов"""
    cakes = [
        types.InlineKeyboardButton(text='🍰 Эстерхази', callback_data='esterhazy'),
        types.InlineKeyboardButton(text='🍰 Чёрный лес', callback_data='black_forest'),
        types.InlineKeyboardButton(text='🍰 Наполеон', callback_data='napoleon'),
    ]
    builder = InlineKeyboardBuilder()
    for cake in cakes:
        builder.row(cake)
    await callback.message.answer("Выбери продукт:", reply_markup=builder.as_markup(resize_keyboard=True))


cakes_info = {
    'esterhazy': {
        'info': 'ℹ️ Информация о продукте',
        'data': '📆 Выбрать дату доставки',
    },
    'black_forest': {
        'info': 'ℹ️ Информация о продукте',
        'data': '📆 Выбрать дату доставки',
    },
    'napoleon': {
        'info': 'ℹ️ Информация о продукте',
        'data': '📆 Выбрать дату доставки',
    },
}


@dp.callback_query(F.data.in_({'esterhazy', 'black_forest', 'napoleon'}))
async def instance_cake(callback: types.CallbackQuery):
    cake = cakes_info[callback.data]
    buttons = [
        types.InlineKeyboardButton(text=v, callback_data=k)
        for k, v in cake.items()
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
