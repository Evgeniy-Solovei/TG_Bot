from aiogram.fsm.state import StatesGroup, State


class ControlWeather(StatesGroup):
    """Состояние вывода информации о погоде"""
    api_weather = State()
