import asyncio
from database.database import db_start
from handlers.standard_handlers import start, help
from keyboards import category_cakes, category_marshmallow, category_flowers, category_tartlets, category_sweets, \
    list_categories
from loader import dp, bot


async def main():
    """Запуск процесса поллинга новых апдейтов"""
    await db_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    dp.include_routers(start.router, help.router)
    dp.include_routers(list_categories.start_routers)
    dp.include_routers(category_cakes.router_cakes)
    dp.include_routers(category_marshmallow.router_marshmallow)
    dp.include_routers(category_flowers.router_flowers)
    dp.include_routers(category_tartlets.router_tartlets)
    dp.include_routers(category_sweets.router_sweets)

    asyncio.run(main())
