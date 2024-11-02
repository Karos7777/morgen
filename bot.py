import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

API_TOKEN = '7211622201:AAH6uicWDk-pyBRpXdHa1oPDjX0pu6pnLaw'
WEB_APP_URL = 'https://karos7777.github.io/morgen/'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton(text='Начать игру', web_app=types.WebAppInfo(url=WEB_APP_URL))
    keyboard.add(web_app_button)
    await message.answer("Привет! Нажми кнопку ниже, чтобы начать игру.", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
