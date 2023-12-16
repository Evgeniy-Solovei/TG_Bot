from aiogram import types, Router
from aiogram.filters import Command
from database.database import cmd_start_db
from keyboards.list_categories import list_categories
from keyboards.menu import menu_keyboard

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    """Запуск бота"""
    await cmd_start_db(message.from_user.id, message.from_user.full_name)
    await message.answer(f'Добро пожаловать, <b>{message.from_user.first_name}.</b>',
                         reply_markup=menu_keyboard)
    await message.answer('Выберите продукт: ', reply_markup=list_categories)
