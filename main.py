from aiogram import Bot,Dispatcher,types
import asyncio
from icecream import ic
from dotenv import load_dotenv
import sys
from Handlers.hand import list_handlers #__init__ is writed path modules!!!!!!!!!!**
import os
from Middlewarries.mw import AdminMiddleware




load_dotenv(".env")

bot=Bot(os.getenv("API"))
dp=Dispatcher(bot)


        



async def register_handlers(dp: Dispatcher)->None:
    for part in list_handlers:
        
        await part(dp)

async def main()->None:
    await register_handlers(dp)
    try:
       await dp.start_polling()
       
    except Exception as _ex:
        ic(f"{_ex}")


if __name__=="__main__":
    dp.setup_middleware(AdminMiddleware())
    asyncio.run(main())