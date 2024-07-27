from telegram import Update
from telegram.ext import CallbackContext
from .gpt_service.py import get_gpt_response

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = get_gpt_response(user_message)
    update.message.reply_text(response)
