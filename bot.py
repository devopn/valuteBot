import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import json
import logging
from handlers.commands import router as command_router
from callbacks.menu_callbacks import router as menu_router
from fsm.valute import router as valute_router


logging.basicConfig(level=logging.INFO, filename="bot.log", format="%(asctime)s - %(levelname)s - %(message)s")

config = json.loads(open("config.json").read())
APIKEY = config['APIKEY']
ROCKET = config['XROCKET']

async def main():
    # print(valutesAPI.getCurse())
    bot = Bot(token=APIKEY)
    dp = Dispatcher()

    dp.include_routers(command_router, menu_router, valute_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())