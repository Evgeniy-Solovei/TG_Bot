import asyncio
from database.database import db_start
from handlers.custom_handlers import handlers_cakes, handlers_flowers, handlers_marshmallow, handlers_sweets, \
    handlers_tartlets, handlers_menu
from handlers.standard_handlers import start, help
from loader import dp, bot


async def main():
    """Запуск процесса поллинга новых апдейтов"""
    await db_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    dp.include_routers(start.router, help.router)
    dp.include_routers(handlers_cakes.router_cakes)
    dp.include_routers(handlers_flowers.router_flowers)
    dp.include_routers(handlers_marshmallow.router_marshmallow)
    dp.include_routers(handlers_sweets.router_sweets)
    dp.include_routers(handlers_tartlets.router_tartlets)
    dp.include_routers(handlers_menu.router_menu)

    asyncio.run(main())
