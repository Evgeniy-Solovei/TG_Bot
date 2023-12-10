import aiosqlite


# После команды старт создаётся БД, если не была создана раньше. Эту функцию мы запускам в функции main в файле bot.py
async def db_start():
    async with aiosqlite.connect('sqlite3.db') as db:
        async with db.cursor() as cur:
            await cur.execute("CREATE TABLE IF NOT EXISTS order_user("
                              "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                              "id_user INTEGER,"
                              "name_user TEXT,"
                              "start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

        await db.commit()


# После команды старт, id и fullname пользователя добавляется в БД, если его там нет. Эту функцию мы запускаем в
# функции cmd_start, что бы при запуске мы сразу добавляли пользователя в БД.
async def cmd_start_db(user_id: int, full_name: str):
    async with aiosqlite.connect('sqlite3.db') as db:
        async with db.cursor() as cur:
            await cur.execute(f"SELECT * FROM order_user WHERE id_user == {user_id}")
            user = await cur.fetchone()
            if not user:
                await cur.execute(f"INSERT INTO order_user (id_user, name_user) VALUES ({user_id}, '{full_name}')")
        await db.commit()
#  Пользователь может добавить дату заказа, просмотреть свои даты заказов и удалить свои заказы
