from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram import types
from keyboards.menu_keyboard import get_menu_keyboard

import valutesAPI

avaible_valutes = ["RUB", "USD", "EUR"]
router = Router()
def make_row_keyboard(items: list[str]) -> InlineKeyboardMarkup:

    row = [InlineKeyboardButton(text=item, callback_data=f"{item}") for item in items]
    return InlineKeyboardMarkup(inline_keyboard=[row])

class ValuteConverter(StatesGroup):
    choosing_valute_from = State()
    choosing_valute_to = State()
    amount = State()
    lastMessage = State()

@router.callback_query(StateFilter(None), F.data == ("convert"))
async def choosing_valute_from(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Выбери начальную валюту", reply_markup=make_row_keyboard(avaible_valutes))    
    await state.set_state(ValuteConverter.choosing_valute_from)

@router.callback_query(StateFilter(ValuteConverter.choosing_valute_from), F.data.in_(avaible_valutes))
async def choosing_valute_to(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(valute_from=callback.data)
    await callback.message.edit_text("Выбери конечную валюту", reply_markup=make_row_keyboard(avaible_valutes))    
    await state.set_state(ValuteConverter.choosing_valute_to)

@router.callback_query(StateFilter(ValuteConverter.choosing_valute_to), F.data.in_(avaible_valutes))
async def amount(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(valute_to=callback.data)
    await state.update_data(lastMessage=callback.message)
    await callback.message.edit_text("Введи сумму")
    await state.set_state(ValuteConverter.amount)

@router.message(StateFilter(ValuteConverter.amount))
async def get_amount(message: types.Message, state: FSMContext):
    await state.update_data(amount=message.text)
    data = await state.get_data()
    a = valutesAPI.getCurse()
    curse = a['rates']
    try:
        money_from = float(data["amount"])
        if data["valute_from"] != "RUB":
            money_from = money_from / float(curse[data["valute_from"]])
        if data["valute_to"] != "RUB":
            money_to = money_from * float(curse[data["valute_to"]])
        else:
            money_to = money_from
        money_to = format(money_to, ".3f")
        
        await data["lastMessage"].edit_text(f"Выбери действие:\n\n{data['amount']} {data['valute_from']} = {money_to} {data['valute_to']}", reply_markup=get_menu_keyboard())
    except:
        await data["lastMessage"].edit_text("Введены некорректные данные", reply_markup=get_menu_keyboard())
    await message.delete()

    # await message.answer(f"{data['amount']} {data['valute_from']} = {valutesAPI.getCurse()['rates'][data['valute_to']]} {data['valute_to']}")
    await state.clear()