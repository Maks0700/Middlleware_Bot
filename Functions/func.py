from aiogram import types

from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

async def cmd_start(message:types.Message)->None:
    
    
    ikb=types.InlineKeyboardMarkup(row_width=3,inline_keyboard=[
        [types.InlineKeyboardButton("Test message",callback_data=f"check {message.from_user.id}")]
    ])
    await message.answer(f"Test message",reply_markup=ikb)

async def cmd_query(callback:types.CallbackQuery)->None:
        
        await callback.message.answer("You are touching the button!!")
        
        
        
        
        
     

