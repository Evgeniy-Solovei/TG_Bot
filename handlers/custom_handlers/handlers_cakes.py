from aiogram import Router, F, types
from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from keyboards.category_cakes import categories_cakes
from lexicon.lexicon_ru import cakes_info

router_cakes = Router()


@router_cakes.callback_query(F.data == 'cakes')
async def cakes(callback: types.CallbackQuery):
    await callback.message.answer('Выберите продукт: ', reply_markup=categories_cakes)


@router_cakes.callback_query(F.data.in_({'esterhazy', 'black_forest', 'napoleon'}))
async def instance_cake(callback: types.CallbackQuery):
    cake = cakes_info[callback.data]['info']  # берём название из апгрейда ('esterhazy', 'black_forest', 'napoleon')
    photos = cakes_info[callback.data]['photos']
    album_builder = MediaGroupBuilder(caption=cake)
    for photo in photos:
        album_builder.add(type="photo", media=FSInputFile(photo))
    await callback.message.answer_media_group(media=album_builder.build())
