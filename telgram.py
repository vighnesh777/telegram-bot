from telegram import *
import time;
from telegram.ext import * 
bot = Bot("1997808537:AAH6_z6YznIJnQ581DETDo-Rfj4h4Lc1YJM")
updater=Updater("1997808537:AAH6_z6YznIJnQ581DETDo-Rfj4h4Lc1YJM",use_context=True)
dispatcher=updater.dispatcher

def test_function(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="GoodMorning",
    )
def func2(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="you have a class,dont you?",
    )
start_value=CommandHandler('motion_detection',test_function)
start_value1=CommandHandler('class',func2)

dispatcher.add_handler(start_value1)
dispatcher.add_handler(start_value)
updater.start_polling()