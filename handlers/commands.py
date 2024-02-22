from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types
router = Router()

@router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Привет, я создан чтобы конвертировать валюты по актуальному курсу.",
                         reply_markup=types.InlineKeyboardMarkup(
                             inline_keyboard=[[types.InlineKeyboardButton(text="Поехали", callback_data="menu:menu")]]

    ))