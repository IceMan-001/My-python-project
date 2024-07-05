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
    text = f"""
    Погода на {weather['day_of_month']}
    Ночью:
    Температура: {weather['Ночь']['temperature']}
    {weather['Ночь']['atmosfera']}
    Ощущается: {weather['Ночь']['weather_feeling']}
    Влажность: {weather['Ночь']['probability']}
    Давление: {weather['Ночь']['pressure']}
    Ветер: {weather['Ночь']['wind']['wind_direction']}, {weather['Ночь']['wind']['wind_kch']}
    """

    await message.answer(text=text)


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
