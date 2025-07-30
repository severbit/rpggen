from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import random
import asyncio
import os
    
# Загрузка переменных окружения из .env файла
load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


names = ["Гримдор", "Эллиан", "Рагнар", "Мортиус", "Люциус", "Ария", "Торион"]
races = ["Человек", "Эльф", "Орк", "Гном", "Тролль", "Демон"]
classes = ["Воин", "Маг", "Паладин", "Разбойник", "Лучник", "Жрец"]

def generate_stats():
    return {
        "⚔️ Сила": random.randint(5, 20),
        "🏃‍♂️ Ловкость": random.randint(5, 20),
        "🧠 Интеллект": random.randint(5, 20),
        "❤️ Здоровье": random.randint(20, 50),
    }


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "Привет! Я бот для создания персонажей в RPG. "
        "Используй команду /create для создания нового персонажа."
    )


@dp.message(Command("create"))
async def create_character(message: Message):
    name = random.choice(names)
    race = random.choice(races) 
    cls = random.choice(classes)
    stats = generate_stats()

    text = f"""<b>Персонаж создан!</b>
<b>Имя:</b> {name}
<b>Раса: {race}</b>
<b>Класс: {cls}</b>
<b>Статы: </b>
"""
    for stat, value in stats.items():
        text += f"{stat}: {value}\n"

    await message.answer(text, parse_mode=ParseMode.HTML)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())