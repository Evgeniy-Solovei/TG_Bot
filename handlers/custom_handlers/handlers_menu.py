from datetime import datetime
import requests
from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.list_categories import list_categories
from loader import api_weather
from states.weather_state import ControlWeather

router_menu = Router()


# @router_menu.message(~F.text == 'Хотите узнать погоду ?')
# async def fallback_handler(message: Message):
#     await message.answer("Я не знаю, что ответить на это сообщение.")


@router_menu.message(F.text == 'Instagram')
async def weather(message: Message):
    """Ссылка на страницу в Instagram"""
    await message.answer(
        text='https://instagram.com/solovey_desert'
    )


@router_menu.message(StateFilter(None), F.text == 'Хотите узнать погоду ?')
async def input_city(message: Message, state: FSMContext):
    """Ввод города пользователем для API"""
    await message.answer(text='Введите интересующий вас город:')
    await state.set_state(ControlWeather.api_weather)


@router_menu.message(ControlWeather.api_weather, F.text)
async def weather(message: Message, state: FSMContext):
    """Вывод информации о погоде через API"""
    try:
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
            await state.clear()
        else:
            await message.reply('Мне кажется, вы ввели не правильно город, попробуйте ещё раз')
            await input_city(message, state)
    except Exception as e:
        print(f"An error occurred: {e}")
        await message.answer(
            'Произошла ошибка при получении данных о погоде. Попробуйте позже или введите другой город.')


@router_menu.message(F.text == 'Главное меню')
async def menu(message: Message):
    """Вывод клавиатуры главного меню, при нажатии на кнопку"""
    await message.answer(text='Выберите продукт: ', reply_markup=list_categories)


@router_menu.message()
async def answer_all(message: Message):
    """Вывод клавиатуры главного меню на все сообщения от пользователя, которые не зарегистрированы"""
    await message.answer(text='Выберите продукт: ', reply_markup=list_categories)
