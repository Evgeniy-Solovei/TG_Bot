from aiogram import Router, F, types
from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from lexicon.lexicon_ru import marshmallow_info

router_marshmallow = Router()


@router_marshmallow.callback_query(F.data == 'marshmallow')
async def info_marshmallow(callback: types.CallbackQuery):
    """Вывод информации о marshmallow"""
    marshmallow = marshmallow_info['info']
    photos = marshmallow_info['photos']
    album_builder = MediaGroupBuilder(caption=marshmallow)
    for photo in photos:
        album_builder.add(type="photo", media=FSInputFile(photo))
    await callback.message.answer_media_group(media=album_builder.build())
