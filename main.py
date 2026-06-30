from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("မင်္ဂလာပါ 👋 Auto Reply Bot ဖြစ်ပါတယ်။")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("Bot is running...")
app.run_polling()
