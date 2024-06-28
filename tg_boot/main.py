from dotenv import load_dotenv
import os

from aiogram import Bot, Dispatcher
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
    await massage.answer('Привет! меня зовут: Топ-бот \n Напиши мне что-нибудь!')


@dp.message()
async def process_command_start(massage: Message):
    await massage.answer('Привет! меня зовут: Топ-бот \n Напиши мне что-нибудь!')
    await massage.answer('Привет! меня зовут: Топ-бот \n Напиши мне что-нибудь!')
    await massage.answer('Привет! меня зовут: Топ-бот \n Напиши мне что-нибудь!')

if __name__ == "__main__":
    dp.run_polling(bot)

