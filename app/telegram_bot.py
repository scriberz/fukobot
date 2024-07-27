from telegram.ext import Updater, MessageHandler, Filters
from .config import Config
from .handlers import handle_message

def start_bot():
    updater = Updater(token=Config.TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    updater.start_polling()
    updater.idle()
