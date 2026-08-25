"""
Telegram-бот для игры "Кошка-девочка и мини-дракончик"
Платформа: aiogram 3.x
"""

import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Токен бота (рекомендуется передавать через переменную окружения)
BOT_TOKEN = os.getenv("BOT_TOKEN", "kkk")

# URL вашего WebApp (GitHub Pages, Vercel и т.д.)
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://hor4ik.github.io/miu/")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start. Выводит приветствие и кнопку для запуска TWA.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🐾 Играть в Тамагочи 🐉",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ],
            [
                InlineKeyboardButton(
                    text="📜 Инструкция и Описание",
                    callback_data="help_info"
                )
            ]
        ]
    )
    
    welcome_text = (
        "<b>Приветствую в уютном домике!</b> 🐾🐉

"
        "Здесь живут маленькая Кошка-девочка и шустрый Мини-дракончик.
"
        "Заботьтесь о них, справляйтесь с бытовым хаосом и наблюдайте за их дружбой!

"
        "<i>Нажмите кнопку ниже, чтобы открыть игру прямо в Telegram.</i>"
    )
    
    await message.answer(welcome_text, reply_markup=keyboard, parse_mode="HTML")

@dp.callback_query(lambda c: c.data == "help_info")
async def process_help(callback: types.CallbackQuery):
    help_text = (
        "<b>Как играть:</b>
"
        "• Следите за показателями: Голод, Настроение, Усталость, Дружба, Чистота, Тепло.
"
        "• Нажимайте на подсвеченные объекты в комнате для взаимодействия.
"
        "• Справляйтесь со случайными событиями (выключение света, рассыпанный корм, потухшая свеча).
"
        "• Прогресс сохраняется автоматически!"
    )
    await callback.answer()
    await callback.message.answer(help_text, parse_mode="HTML")

async def main():
    print("Бот запущен! Ожидание сообщений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("ВНИМАНИЕ: Не забудьте указать реальный BOT_TOKEN!")
    asyncio.run(main())