from datetime import datetime

import requests
from aiogram import types, Router, F
from aiogram.types import ReplyKeyboardRemove, Message

from loader import api_weather

start_routers = Router()


async def start_list_categories(message: types.Message):
    """Инлайн кнопки с категориями товаров прикрепляются к сообщению"""
    buttons = [

        [
            types.InlineKeyboardButton(text='🎂 Торты', callback_data='cakes')
        ],
        [
            types.InlineKeyboardButton(text='🦄 Маршмеллоу', callback_data='marshmallow')
        ],
        [
            types.InlineKeyboardButton(text='🌷 Зефирные цветы', callback_data='flowers')
        ],
        [
            types.InlineKeyboardButton(text='🥮 Тарталетки', callback_data='tartlets')
        ],
        [
            types.InlineKeyboardButton(text='🍬 Конфеты', callback_data='sweets')
        ]

    ]

    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    await message.answer("Выбери продукт:", reply_markup=reply_markup)


async def buttons_below(message: types.Message):
    buttons = [
        [
            types.KeyboardButton(text='Нажми, чтобы узнать погоду...')
        ],
        [
            types.KeyboardButton(text='Instagram ')
        ],

    ]
    reply_markup = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True)
    await message.answer(
        text=f'Добро пожаловать, <b>{message.from_user.first_name}</b>', parse_mode='HTML',
        reply_markup=reply_markup
    )


@start_routers.message(F.text == 'Нажми, чтобы узнать погоду...')
async def weather(message: Message):
    await message.answer(
        text='Введите интересующий вас город:'
    )


@start_routers.message()
async def get_weather(message: Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    api_data = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={api_weather}&units=metric&lang=ru'
    )
    data = api_data.json()
    if data['cod'] == 200:
        city = data['name']
        current_weather = data['main']['temp']
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        atmosphere_pressure = data['main']['grnd_level']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(data['sys']['sunrise'])
        await message.reply(f'Погода в городе: {city}\n'
                            f'Температура: {current_weather} С° {wd}\n'
                            f'Влажность: {humidity}%\n'
                            f'Скорость ветра: {wind_speed} м/с\n'
                            f'Давление: {atmosphere_pressure} мм.рт.ст.\n'
                            f'Восход солнца: {sunrise}\n'
                            f'Заход солнца: {sunset}\n'
                            f'Продолжительность дня: {length_of_day}')
    else:
        await message.reply('Введите правильно город')

# """Простые кнопки которые крепятся снизу"""
# async def start_list_categories(message: types.Message):
#     buttons = ['🎂 Торты', '🦄 Маршмеллоу', '🌷 Зефирные цветы', '🥮 Тарталетки', '🍬 Конфеты']
#     builder = ReplyKeyboardBuilder()
#     for button in buttons:
#         builder.add(types.KeyboardButton(text=str(button)))
#     builder.adjust(4)
#     await message.answer("Выбери продукт:", reply_markup=builder.as_markup(resize_keyboard=True))
