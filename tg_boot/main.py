from dotenv import load_dotenv
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from user_handler import router as user_router

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
# print(bot_token)

# Создаем объект бота и объект диспетчера
bot = Bot(token=bot_token)
dp = Dispatcher()
dp.include_router(user_router)

if __name__ == "__main__":
    dp.run_polling(bot)
    print("\N{smiling face with sunglasses}""\N{smiling face with sunglasses}""\N{smiling face with sunglasses}")
