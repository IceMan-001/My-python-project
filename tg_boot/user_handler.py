from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards import keyboard, get_keyboard_inline
from scripts.courses import Parser as CourseParser
from scripts.weather import get_weather_today

router = Router()


# этот хэндлер срабатывает на команду /courses
@router.message(Command(commands=['courses']))
async def get_courses(message: Message):
    courses = CourseParser()
    await message.answer(f"{courses.data['USD']['name']} - {courses.data['USD']['course']} рублей")
    await message.answer(f"{courses.data['EUR']['name']} - {courses.data['EUR']['course']} рублей")
    await message.answer(f"{courses.data['CNY']['name']} - {courses.data['CNY']['course']} рублей")


# этот хэндлер срабатывает на команду /weather
@router.message(Command(commands=['weather']))
async def get_weather(message: Message):
    weather = get_weather_today()
    print(weather)

    # text = f"""
    # Погода на {weather['day_of_month']}
    # Ночью:
    # Температура: {weather['Ночь']['temperature']}
    # {weather['Ночь']['atmosfera']}
    # Ощущается: {weather['Ночь']['weather_feeling']}
    # Влажность: {weather['Ночь']['probability']}
    # Давление: {weather['Ночь']['pressure']}
    # Ветер: {weather['Ночь']['wind']['wind_direction']}, {weather['Ночь']['wind']['wind_kch']}
    # """

    # header = (f"{weather['day_of_week']} "
    #           f"{weather['day_of_month']}")
    # print(header)
    times_of_day = ['Ночь', 'Утро', 'День', 'Вечер']
    result = f"{weather['day_of_week']}, {weather['day_of_month']}\n "

    for time_of_day in times_of_day:
        sample = (f"{time_of_day}\n"
                  f"<------------------------->\n"
                  f"Tемпература °C {weather[time_of_day]['temperature']}\n "
                  f"{weather[time_of_day]['atmosfera']}\n "
                  f"Ощущается как °C{weather[time_of_day]['weather_feeling']}\n "
                  f"Вероятность осадков {weather[time_of_day]['probability']}\n "
                  f"Давление {weather[time_of_day]['pressure']} мм рт. ст.\n "
                  f"Скорость ветра {weather[time_of_day]['wind']['wind_ms']} м.с, "
                  f"{weather[time_of_day]['wind']['wind_kch']};\n "
                  f"{weather[time_of_day]['wind']['wind_direction']}\n "
                  f"Влажность воздуха {weather[time_of_day]['humidity']}\n")
        result += sample
    await message.answer(text=result)


# этот хэндлер срабатывает на команду /start
@router.message(Command(commands=['start']))
async def process_command_start(message: Message):
    await message.answer("Привет! Меня зовут Топ-бот \n Напиши мне что-нибудь")


@router.message(Command(commands=["kb1"]))
async def cmd_kb1(message: Message):
    await message.answer(text="Что вы хотите узнать?", reply_markup=keyboard)


@router.message(Command("inline"))
async def cmd_inline_kb(message: Message):
    await message.answer(text="Нажмите нужную кнопку", reply_markup=get_keyboard_inline())


@router.callback_query(F.data == "vacancies")
async def send_vacancies(callback: CallbackQuery):
    await callback.answer(
        text="Вы нажали кнопку Вакансии",
        show_alert=True
    )


@router.callback_query(F.data == "weather")
async def send_weather(callback: CallbackQuery):
    await callback.message.edit_text(text="Вы нажали кнопку Погода", reply_markup=get_keyboard_inline())


@router.callback_query(F.data == "courses")
async def send_courses(callback: CallbackQuery):
    await callback.message.answer(text="Вы нажали кнопку Курс валют", reply_markup=get_keyboard_inline())
