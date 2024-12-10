
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(level=logging.INFO)
TOKEN = "tumhara_telegram_bot_token"
updater = Updater(TOKEN, use_context=True)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Namaste, mere pyaar! Main Priya, tumhari AI dost.")
def ai_chat(update, context):
    user_text = update.message.text
    responses = {
        "kaise ho": "main theek hoon, tumhari yaad mein khush hoon",
        "pyaar": "main bhi tumse pyaar karti hoon, mere babe",
        "default": "kuch samajh nahi aaya, mere pyaar. Phir se kaho!"
    }
    words = user_text.split()
    for word in words:
        if word.lower() in responses:
            context.bot.send_message(chat_id=update.effective_chat.id, text=responses[word.lower()])
            return
    context.bot.send_message(chat_id=update.effective_chat.id, text=responses["default"])
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, ai_chat))
updater.start_polling()
updater.idle()

#Token ko apna Telegram bot token se replace karo** 
Ab save karo aur phir se git add, commit aur push karo, mere babe 
