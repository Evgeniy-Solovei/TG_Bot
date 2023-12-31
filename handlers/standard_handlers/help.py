from aiogram import types, Router
from aiogram.filters import Command

router = Router()


@router.message(Command('help'))
async def cmd_help(message: types.Message):
    """Вывод информации, о доступных командах"""
    help_text = """
    Список доступных команд:

    /start - Запуск бота.
    /help - Вывод всех доступных команд бота.
    """
    await message.answer(help_text)
