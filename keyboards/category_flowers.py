from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import dp


async def info_flowers(callback: types.CallbackQuery):
    flowers = [
        types.InlineKeyboardButton(text='ℹ️ Информация о продукте', callback_data='info'),
        types.InlineKeyboardButton(text='📆 Выбрать дату доставки', callback_data='data')
    ]
    builder = InlineKeyboardBuilder()
    for flower in flowers:
        builder.row(flower)
    await callback.message.answer("Выбери пункт:", reply_markup=builder.as_markup(resize_keyboard=True))


@dp.callback_query(F.data == 'info')
async def instance_info(callback: types.CallbackQuery):
    await callback.message.answer('Информация о продукте для заполнения')


@dp.callback_query(F.data == 'data')
async def instance_info(callback: types.CallbackQuery):
    await callback.message.answer('Тут должен быть апи Календаря')
