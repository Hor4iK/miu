import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Токен берется из переменных окружения или указывается напрямую
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
WEB_APP_URL = os.getenv("WEB_APP_URL", "https://hor4ik.github.io/miu/")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="🐾 Играть в Тамагочи", 
        web_app=WebAppInfo(url=WEB_APP_URL)
    ))
    
    await message.answer(
        "👋 **Добро пожаловать в уютный хаос!**\n\n"
        "Кошка-девочка и мини-дракончик уже ждут тебя. Нажми кнопку ниже, чтобы открыть игру прямо в Telegram.",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    import asyncio
    print("Бот запущен...")
    asyncio.run(dp.start_polling(bot))