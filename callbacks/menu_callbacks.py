from aiogram import Router, F
from aiogram import types
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
import keyboards.menu_keyboard as menu_keyboard




router = Router()


@router.callback_query(F.data.startswith("menu"))
async def main_menu(callback: types.CallbackQuery):
    ask = callback.data.split(":")[1]
    # print(ask)
    match ask:
        case "menu":
            # await callback.message.edit_media(media=types.InputMediaPhoto(media=open("img/val.png", "rb")))

            await callback.message.edit_text("Выбери действие", reply_markup=menu_keyboard.get_menu_keyboard())