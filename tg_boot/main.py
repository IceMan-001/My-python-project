from dotenv import load_dotenv
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
# print(bot_token)

# Создаем объект бота и объект диспетчера
bot = Bot(token=bot_token)
dp = Dispatcher()


# этот хэндлер срабатывает на команду /start
@dp.message(Command(commands=['start']))
async def process_command_start(massage: Message):
    await massage.answer(
        'Привет! Меня зовут "Bot-Advisor"! \n Для обзора возможностей бота воспользуйтесь командой \n"help"')


@dp.message(Command(commands=['help']))
async def process_command_help(massage: Message):
    await massage.answer(
        'Для вывода прогноза погоды: \n введите команду: "/weather" или воспользуйтесь пунктом меню. \n'
        'Для вывода прогноза курса валют: \n введите команду: "/courses" или воспользуйтесь пунктом меню.\n '
        'Для вывода прогноза вакансий: \n введите команду: "/vacancies" или  воспользуйтесь пунктом меню.')


@dp.message(Command(commands=['weather']))
async def process_command_weather(massage: Message):
    await massage.answer('Погода')


@dp.message(Command(commands=['courses']))
async def process_command_courses(massage: Message):
    await massage.answer('Курс валют')


@dp.message(Command(commands=['vacancies']))
async def process_command_vacancies(massage: Message):
    await massage.answer('Подбор вакансий')


@dp.message(lambda msg: 'vacancies' in msg.text.lower())
async def answer(message: types.Message):
    await message.answer('По вашему запросу будет подготовлен и выведен ответ через 1, 2, 3...')


@dp.message()
async def answer(message: types.Message):
    await message.answer('Команда не опознана! \nДля просмотра возможных команд \nвоспользуйтесь командой: "help"')


if __name__ == "__main__":
    dp.run_polling(bot)
    print("\N{smiling face with sunglasses}""\N{smiling face with sunglasses}""\N{smiling face with sunglasses}")
