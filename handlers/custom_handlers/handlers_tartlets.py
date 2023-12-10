from aiogram import Router, F, types
from aiogram.types import FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from lexicon.lexicon_ru import tartlets_info

router_tartlets = Router()


@router_tartlets.callback_query(F.data == 'tartlets')
async def info_tartlets(callback: types.CallbackQuery):
    tartlets = tartlets_info['info']
    photos = tartlets_info['photos']
    album_builder = MediaGroupBuilder(caption=tartlets)
    for photo in photos:
        album_builder.add(type="photo", media=FSInputFile(photo))
    await callback.message.answer_media_group(media=album_builder.build())
