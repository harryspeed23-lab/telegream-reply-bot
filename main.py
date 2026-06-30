from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters


BOT_TOKEN = os.getenv("BOT_TOKEN")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("မင်္ဂလာပါ 🤖 Auto Reply Bot")
token("BOT_TOKEN")
app = Application.builder().token("8657559322:AAE3KDwV092R6w-tqDoz1X87sB5MpBpn9Vw").build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply)
)

print("Bot is running...")
app.run_polling()
