import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8657559322:AAE3KDwV092R6w-tqDoz1X87sB5MpBpn9Vw"

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("မင်္ဂလာပါ 🤖 Auto Reply Bot")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply)
)

print("Bot is running...")
app.run_polling()
