from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text


async def register_handlers_start(dp:Dispatcher)->None:
     from Functions.func import cmd_start
     dp.register_message_handler(cmd_start,commands=["start"])
   
async def check_handler(dp:Dispatcher)->None:
     from Functions.func import cmd_query
     check_lambda_query=lambda callback:callback.data.startswith("check ")
     dp.register_callback_query_handler(cmd_query,check_lambda_query)
     
     
     
     
     
     
     

list_handlers=[register_handlers_start,check_handler]
