from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Конвертер", callback_data="convert"))
    builder.row(InlineKeyboardButton(text="secret_button", callback_data="menu:rickroll"))
    builder.row(InlineKeyboardButton(text="Принудительные пожертвования", callback_data="menu:other_funds"))
    return builder.as_markup()