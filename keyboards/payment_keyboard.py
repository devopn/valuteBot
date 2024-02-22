from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_pay_keyboard(pay) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Вернуться", callback_data="menu:menu"))
    builder.row(InlineKeyboardButton(text="Оплатить", url=pay))
    return builder.as_markup()