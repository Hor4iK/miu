"""
Telegram-бот для игры «Кошка-девочка и мини-дракончик».
Платформа: aiogram 3.x
"""
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://hor4ik.github.io/miu/")

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🐾 Играть в Тамагочи 🐉",
                web_app=WebAppInfo(url=WEBAPP_URL),
            )],
            [InlineKeyboardButton(
                text="📜 Инструкция и описание",
                callback_data="help_info",
            )],
        ]
    )

    welcome_text = (
        "<b>Приветствую в уютном домике!</b> 🐾🐉\n\n"
        "Здесь живут маленькая Кошка-девочка и шустрый Мини-дракончик.\n"
        "Теперь они сами ходят по комнате, умываются, играют, "
        "подходят к миске, коробке и окну и отдыхают.\n\n"
        "<i>Нажмите кнопку ниже, чтобы открыть игру прямо в Telegram.</i>"
    )
    await message.answer(welcome_text, reply_markup=keyboard, parse_mode="HTML")


@dp.callback_query(lambda c: c.data == "help_info")
async def process_help(callback: types.CallbackQuery):
    help_text = (
        "<b>Как играть:</b>\n"
        "• Следите за показателями: Голод, Настроение, Энергия, "
        "Дружба, Чистота, Тепло.\n"
        "• Персонажи живут автономно: ходят, моргают, машут хвостом, "
        "умываются, играют и взаимодействуют с комнатой.\n"
        "• Нажимайте на кошку или дракончика для ручных действий.\n"
        "• Справляйтесь со случайными событиями.\n"
        "• Прогресс сохраняется автоматически!"
    )
    await callback.answer()
    await callback.message.answer(help_text, parse_mode="HTML")


async def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "Не задан BOT_TOKEN. Укажите токен через переменную окружения BOT_TOKEN."
        )

    bot = Bot(token=BOT_TOKEN)
    try:
        logging.info("Бот запущен! Ожидание сообщений...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())