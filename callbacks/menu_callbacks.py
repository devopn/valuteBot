from aiogram import Router, F
from aiogram import types
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
import keyboards.menu_keyboard as menu_keyboard
from keyboards.delete_keyboard import get_delete_keyboard
import requests
from keyboards.payment_keyboard import get_pay_keyboard
import httpx



router = Router()


@router.callback_query(F.data.startswith("menu"))
async def main_menu(callback: types.CallbackQuery):
    ask = callback.data.split(":")[1]
    # print(ask)
    match ask:
        case "menu":
            await callback.message.edit_text("Выбери действие", reply_markup=menu_keyboard.get_menu_keyboard())
        case "rickroll":
            await callback.message.answer_animation("https://upload.wikimedia.org/wikipedia/ru/6/61/Rickrolling.gif", reply_markup=get_delete_keyboard() )
            await callback.message.edit_text("Выбери действие", reply_markup=menu_keyboard.get_menu_keyboard())
        case "pay":
            req = {
                "minPayment": 0.001,
                "numPayments": 0,
                "currency": "TONCOIN",
                "description": "best thing in the world, 1 item",
                "hiddenMessage": "thank you",
                "commentsEnabled": False,
                "callbackUrl": "https://t.me/ton_rocket",
                "payload": "some custom payload I want to see in webhook or when I request invoice",
                "expiredIn": 9999
                }
            async with httpx.AsyncClient() as client:
                r = await client.post("https://pay.ton-rocket.com/tg-invoices", json=req, headers={"Rocket-Pay-Key": "891cdb097a088bf6f9d19de24"})
            
            link = r.json()['data']['link']
            await callback.message.edit_reply_markup(reply_markup=get_pay_keyboard(link))
            print(link)
            
        case "delete":
            await callback.message.delete()