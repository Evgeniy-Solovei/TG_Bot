from aiogram import Router, F, types
from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from keyboards.category_sweets import categories_sweets
from lexicon.lexicon_ru import sweets_info

router_sweets = Router()


@router_sweets.callback_query(F.data == 'sweets')
async def sweet(callback: types.CallbackQuery):
    """Вывод кнопок категории sweets"""
    await callback.message.answer('Выберите продукт: ', reply_markup=categories_sweets)


@router_sweets.callback_query(F.data.in_({'irish', 'truffle'}))
async def instance_sweets(callback: types.CallbackQuery):
    """Вывод информации от sweets"""
    sweets = sweets_info[callback.data]['info']
    photos = sweets_info[callback.data]['photos']
    album_builder = MediaGroupBuilder(caption=sweets)
    for photo in photos:
        album_builder.add(type="photo", media=FSInputFile(photo))
    await callback.message.answer_media_group(media=album_builder.build())
