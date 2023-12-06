from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
import logging
from config_data.config import BOT_TOKEN, API_TOKEN

"""Включаем логирование - это запись информации о событиях, происходящих во время работы программы."""
logging.basicConfig(level=logging.DEBUG)

"""Создание экземпляра бота, он обеспечивает через API работу с серверами TG"""
bot = Bot(token=BOT_TOKEN)

"""Диспетчер, предназначен для обработки обновлений от пользователя. Определяет, как бот должен на них отреагировать."""
dp = Dispatcher(storage=MemoryStorage())

"""Создаём экземпляр API, для дальнейших запросов пользователя."""
api_weather = API_TOKEN
