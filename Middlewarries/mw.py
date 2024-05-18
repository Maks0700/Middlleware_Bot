#pre-process update
#process update
#pre-process message
#filter
#process message
#handler
#post process message
#post process update
#####This is all layers middlewares
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler,current_handler
from dotenv import load_dotenv

#CancelHandler- It is  processing event in order to undo action user
#current_handler-It is object which contain the info about user or handler and state user
ADMIN="5528071947"


class AdminMiddleware(BaseMiddleware):
    async def on_process_callback_query(self,callback:types.CallbackQuery,data:dict):
        callback_id=callback.data[callback.data.find(" "):]
        if callback_id!=str(callback.from_user.id):
            raise CancelHandler()
    
        


    



        

               
            
            
            
            
            
            
            
        

    
        
        
                


        
    
    
    
        
    
    
    
    
    
                
    

