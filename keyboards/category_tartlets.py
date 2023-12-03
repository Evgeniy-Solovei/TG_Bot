from aiogram import types, F, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import dp

router_tartlets = Router()


@router_tartlets.callback_query(F.data == 'tartlets')
async def info_tartlets(callback: types.CallbackQuery):
    tartlets = [
        types.InlineKeyboardButton(text='ℹ️ Информация о продукте', callback_data='info'),
        types.InlineKeyboardButton(text='📆 Выбрать дату доставки', callback_data='data')
    ]
    builder = InlineKeyboardBuilder()
    for tartlet in tartlets:
        builder.row(tartlet)
    await callback.message.answer("Выбери пункт:", reply_markup=builder.as_markup(resize_keyboard=True))

    @dp.callback_query(F.data == 'info')
    async def instance_info(callback: types.CallbackQuery):
        await callback.message.answer('Информация о продукте для заполнения')

    @dp.callback_query(F.data == 'data')
    async def instance_info(callback: types.CallbackQuery):
        await callback.message.answer('Тут должен быть апи Календаря')
