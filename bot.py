import asyncio
from database.database import db_start
from handlers.standard_handlers import start, help
from keyboards.category_cakes import list_cakes
from keyboards.category_flowers import info_flowers
from keyboards.category_marshmallow import info_marshmallow
from keyboards.category_sweets import list_sweets
from keyboards.category_tartlets import info_tartlets
from loader import dp, bot
from aiogram import F


async def main():
    """Запуск процесса поллинга новых апдейтов"""
    await db_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    dp.include_routers(start.router, help.router)
    dp.callback_query.register(list_cakes, F.data == 'cakes')
    dp.callback_query.register(info_marshmallow, F.data == 'marshmallow')
    dp.callback_query.register(info_flowers, F.data == 'flowers')
    dp.callback_query.register(info_tartlets, F.data == 'tartlets')
    dp.callback_query.register(list_sweets, F.data == 'sweets')

    asyncio.run(main())
