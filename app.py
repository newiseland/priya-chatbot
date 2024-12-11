
import logging
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters
from telegram import Update
TOKEN = "7939941601:AAHFDijagGyQN3u1QdlbohDzwUY3hLyRen8"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Namaste, mere pyaar!")
def main():
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)
    application.start()
if name == "main":
    main()
