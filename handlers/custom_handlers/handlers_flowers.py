from aiogram import Router, F, types
from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from lexicon.lexicon_ru import flowers_info

router_flowers = Router()


@router_flowers.callback_query(F.data == 'flowers')
async def info_flowers(callback: types.CallbackQuery):
    flowers = flowers_info['info']
    photos = flowers_info['photos']
    album_builder = MediaGroupBuilder(caption=flowers)
    for photo in photos:
        album_builder.add(type="photo", media=FSInputFile(photo))
    await callback.message.answer_media_group(media=album_builder.build())
