from aiogram import types, Router
from aiogram.filters import Command
from database.database import cmd_start_db
from keyboards.list_categories import start_list_categories, buttons_below

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await cmd_start_db(message.from_user.id, message.from_user.full_name)
    await buttons_below(message)
    await start_list_categories(message)



    # """Вывод фото из компа"""
    # image_from_pc = FSInputFile('static/photo/1.png')
    # await message.answer_photo(
    #     image_from_pc,
    #     caption="Описание фото"
    # )

