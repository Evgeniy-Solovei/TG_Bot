import requests
from loader import api_weather
from datetime import datetime

city = input('Введите город: ')


def get_weather(city, api_weather):
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
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_weather}&units=metric&lang=ru'
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
        print(f'Погода в городе: {city}\n'
              f'Температура: {current_weather} С° {wd}\n'
              f'Влажность: {humidity}%\n'
              f'Скорость ветра: {wind_speed} м/с\n'
              f'Давление: {atmosphere_pressure} мм.рт.ст.\n'
              f'Восход солнца: {sunrise}\n'
              f'Заход солнца: {sunset}\n'
              f'Продолжительность дня: {length_of_day}')
    else:
        print('Введите правильно город')


get_weather(city, api_weather)
